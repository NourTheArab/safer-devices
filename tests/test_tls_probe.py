"""Exercise verdicts and privacy boundaries without contacting any host."""

import contextlib
import io
import json
import shutil
import ssl
import subprocess
import unittest
from unittest.mock import Mock, patch

from checks import tls_probe as probe


class TLSProbeTests(unittest.TestCase):
    def test_all_fourteen_chains_are_required(self):
        self.assertEqual(len(probe.BAD_HOSTS), 14)
        self.assertEqual(len(set(probe.BAD_HOSTS)), 14)
        self.assertEqual(sum("noct" in host for host in probe.BAD_HOSTS), 2)

    def test_failed_healthy_control_stops_incident_probes(self):
        transport = Mock(return_value="unknown")
        report = probe.run_suite(transport)
        self.assertEqual(report["verdict"], "unknown")
        self.assertEqual(transport.call_count, 2)

    def test_accepting_self_signed_control_is_unknown(self):
        transport = Mock(return_value="accepted")
        report = probe.run_suite(transport)
        self.assertEqual(report["verdict"], "unknown")
        self.assertEqual(transport.call_count, 3)

    def transport(self, override=None):
        def call(host):
            if override and host in override:
                return override[host]
            return "accepted" if host in probe.GOOD_HOSTS else "certificate_rejected"
        return call

    def test_complete_rejection_is_scoped_verification(self):
        report = probe.run_suite(self.transport())
        self.assertEqual(report["verdict"], "verified_for_tested_chains")
        self.assertEqual(report["rejected"], 14)

    def test_one_accepted_chain_needs_attention(self):
        report = probe.run_suite(self.transport({probe.BAD_HOSTS[0]: "accepted"}))
        self.assertEqual(report["verdict"], "needs_attention")
        self.assertEqual(report["accepted"], 1)

    def test_timeout_is_never_rejection(self):
        report = probe.run_suite(self.transport({probe.BAD_HOSTS[-1]: "unknown"}))
        self.assertEqual(report["verdict"], "unknown")
        self.assertEqual(report["rejected"], 13)

    def test_python_certificate_error_classified_without_error_text(self):
        with patch.object(probe.ssl, "create_default_context"), patch.object(
            probe.socket, "create_connection", side_effect=ssl.SSLCertVerificationError("private text")
        ):
            self.assertEqual(probe.python_probe(probe.BAD_HOSTS[0]), "certificate_rejected")

    def test_python_network_error_stays_unknown(self):
        with patch.object(probe.ssl, "create_default_context"), patch.object(
            probe.socket, "create_connection", side_effect=TimeoutError("private text")
        ):
            self.assertEqual(probe.python_probe(probe.BAD_HOSTS[0]), "unknown")

    def test_curl_timeout_and_certificate_codes_differ(self):
        for code, expected in ((60, "certificate_rejected"), (28, "unknown"), (0, "accepted")):
            with patch.object(probe.subprocess, "run", return_value=Mock(returncode=code)) as run:
                self.assertEqual(probe.command_probe("curl", "/trusted/curl", probe.GOOD_HOSTS[0]), expected)
                command = run.call_args.args[0]
                self.assertEqual(command[1], "-q")
                self.assertIn("--head", command)
                self.assertNotIn("--insecure", command)
                self.assertFalse(run.call_args.kwargs.get("shell", False))

    def test_child_errors_do_not_leak_output(self):
        with patch.object(probe.subprocess, "run", side_effect=subprocess.TimeoutExpired("private", 10)):
            self.assertEqual(probe.command_probe("node", "/trusted/node", probe.GOOD_HOSTS[0]), "unknown")

    def test_bun_does_not_autoload_env_files_or_install_packages(self):
        with patch.object(probe.subprocess, "run", return_value=Mock(returncode=0, stdout="accepted")) as run:
            probe.command_probe("bun", "/trusted/bun", probe.GOOD_HOSTS[0])
            self.assertIn("--no-env-file", run.call_args.args[0])
            self.assertIn("--no-install", run.call_args.args[0])

    @unittest.skipUnless(shutil.which("node"), "Node is not installed; no installation performed")
    def test_node_adapter_events_without_any_network(self):
        harness = r"""
const vm = require('node:vm');
const assert = require('node:assert/strict');
const source = SOURCE;
for (const [event, value, expected] of [
  ['secureConnect', null, 'accepted'],
  ['error', {code:'CERT_REVOKED'}, 'certificate_rejected'],
  ['error', {code:'ECONNREFUSED'}, 'unknown'],
  ['timeout', null, 'unknown']
]) {
  const handlers = {}; const output = []; let timeout;
  const socket = {authorized:true, destroy(){}, once(name, callback){handlers[name] = callback;}};
  vm.runInNewContext(source, {
    require(name){ assert.equal(name, 'node:tls'); return {connect(options){
      assert.equal(options.rejectUnauthorized, true);
      assert.equal(options.servername, 'example.com');
      return socket;
    }}; },
    process:{argv:['node','example.com']},
    console:{log(value){output.push(value);}},
    setTimeout(callback){timeout = callback; return 1;}, clearTimeout(){}
  });
  if (event === 'timeout') timeout(); else handlers[event](value);
  assert.equal(output.join(''), expected);
}
""".replace("SOURCE", json.dumps(probe.NODE_PROBE))
        result = subprocess.run([shutil.which("node"), "-e", harness], capture_output=True, timeout=10)
        self.assertEqual(result.returncode, 0, "Offline Node adapter event test failed")

    def test_missing_network_acknowledgment_never_connects(self):
        with patch.object(probe, "run_suite") as run, contextlib.redirect_stderr(io.StringIO()):
            with self.assertRaises(SystemExit):
                probe.main([])
            run.assert_not_called()

    def test_relative_executable_refused_before_network(self):
        with patch.object(probe, "run_suite") as run, contextlib.redirect_stderr(io.StringIO()):
            with self.assertRaises(SystemExit):
                probe.main(["--allow-network", "--client", "node", "--executable", "node"])
            run.assert_not_called()

    def test_output_and_exit_code_match_unknown(self):
        output = io.StringIO()
        with patch.object(probe, "run_suite", return_value={"verdict": "unknown"}), contextlib.redirect_stdout(output):
            self.assertEqual(probe.main(["--allow-network"]), 2)
        self.assertEqual(json.loads(output.getvalue())["client"], "python")


if __name__ == "__main__":
    unittest.main()
