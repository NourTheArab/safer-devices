"""Scoped eMudhra TLS checks. No installs, repairs, telemetry or report files.

Requires Python 3.9+. Review the dated host list before each use. Network use
needs --allow-network; alternate clients need an approved absolute executable.
"""

import argparse
import json
import os
from pathlib import Path
import socket
import ssl
import subprocess
import sys


REVIEWED = "2026-10-23"
ADVISORY = "https://emudhra.we-have-a-problem.com/"
GOOD_HOSTS = ("github.com", "emudhra.we-have-a-problem.com")
SELF_SIGNED_HOST = "self-signed.badssl.com"
BAD_HOSTS = tuple(
    f"{kind}-{group}{suffix}-emudhra.we-have-a-problem.com"
    for kind in ("dv", "ov", "ev")
    for group in ("g3b", "g3c")
    for suffix in ("", "-aaa")
) + (
    "dv-g3b-noct-emudhra.we-have-a-problem.com",
    "dv-g3b-aaa-noct-emudhra.we-have-a-problem.com",
)
TIMEOUT = 10
CLIENT_TIMEOUT = TIMEOUT + 3
NODE_PROBE = r"""
const tls = require('node:tls');
const host = process.argv[1];
const certificateErrors = new Set([
  'CERT_HAS_EXPIRED', 'CERT_NOT_YET_VALID', 'CERT_REVOKED',
  'CERT_REJECTED', 'CERT_UNTRUSTED', 'CERT_SIGNATURE_FAILURE',
  'DEPTH_ZERO_SELF_SIGNED_CERT', 'SELF_SIGNED_CERT_IN_CHAIN',
  'UNABLE_TO_GET_ISSUER_CERT', 'UNABLE_TO_GET_ISSUER_CERT_LOCALLY',
  'UNABLE_TO_VERIFY_LEAF_SIGNATURE', 'ERR_TLS_CERT_ALTNAME_INVALID'
]);
let done = false;
const socket = tls.connect({host, port:443, servername:host, rejectUnauthorized:true});
const timer = setTimeout(() => finish('unknown'), 10000);
function finish(status) {
  if (done) return;
  done = true; clearTimeout(timer); console.log(status); socket.destroy();
}
socket.once('secureConnect', () => finish(socket.authorized ? 'accepted' : 'unknown'));
socket.once('error', error => finish(certificateErrors.has(error.code) ? 'certificate_rejected' : 'unknown'));
"""


def python_probe(host):
    """Handshake only: default Python SSL trust, no HTTP content or headers."""
    try:
        context = ssl.create_default_context()
        with socket.create_connection((host, 443), timeout=TIMEOUT) as connection:
            with context.wrap_socket(connection, server_hostname=host):
                return "accepted"
    except ssl.SSLCertVerificationError:
        return "certificate_rejected"
    except (OSError, ValueError):
        return "unknown"


def command_probe(client, executable, host):
    """Do not log subprocess output: even failure messages can hold private data."""
    if client == "curl":
        command = [executable, "-q", "--head", "--silent", "--show-error",
                   "--connect-timeout", "5", "--max-time", str(TIMEOUT),
                   "--max-redirs", "0", "--output", os.devnull, f"https://{host}/"]
    elif client == "bun":
        command = [executable, "--no-env-file", "--no-install", "-e", NODE_PROBE, host]
    else:
        command = [executable, "-e", NODE_PROBE, host]
    try:
        result = subprocess.run(command, capture_output=True, text=True,
                                timeout=CLIENT_TIMEOUT, check=False)
    except (OSError, subprocess.TimeoutExpired, UnicodeError):
        return "unknown"
    if client == "curl":
        return {0: "accepted", 60: "certificate_rejected"}.get(result.returncode, "unknown")
    status = result.stdout.strip()
    if result.returncode == 0 and status in {"accepted", "certificate_rejected"}:
        return status
    return "unknown"


def run_suite(probe):
    controls = [{"host": host, "result": probe(host)} for host in GOOD_HOSTS]
    report = {"reviewed": REVIEWED, "advisory": ADVISORY, "controls": controls,
              "chains": [], "verdict": "unknown"}
    if any(item["result"] != "accepted" for item in controls):
        report["reason"] = "Healthy control failed; incident tests skipped."
        return report
    negative = {"host": SELF_SIGNED_HOST, "result": probe(SELF_SIGNED_HOST)}
    controls.append(negative)
    if negative["result"] != "certificate_rejected":
        report["reason"] = "Self-signed control was not rejected; incident tests skipped."
        return report
    chains = [{"host": host, "result": probe(host)} for host in BAD_HOSTS]
    report["chains"] = chains
    report["accepted"] = sum(item["result"] == "accepted" for item in chains)
    report["rejected"] = sum(item["result"] == "certificate_rejected" for item in chains)
    report["unknown"] = len(chains) - report["accepted"] - report["rejected"]
    if report["accepted"]:
        report["verdict"] = "needs_attention"
    elif report["rejected"] == len(BAD_HOSTS):
        report["verdict"] = "verified_for_tested_chains"
    return report


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--allow-network", action="store_true",
                        help="Acknowledge connections to the documented public test hosts.")
    parser.add_argument("--client", choices=("python", "curl", "node", "bun"), default="python")
    parser.add_argument("--executable", help="Approved absolute curl, node or bun path.")
    args = parser.parse_args(argv)
    if not args.allow_network:
        parser.error("No connections made. Review the hosts and approve network probes first.")
    if args.client == "python":
        if args.executable:
            parser.error("Select another Python by invoking this file with that interpreter.")
        probe = python_probe
    else:
        executable = Path(args.executable) if args.executable else None
        if not executable or not executable.is_absolute() or not executable.is_file():
            parser.error("An approved, existing absolute executable path is required.")
        probe = lambda host: command_probe(args.client, str(executable), host)
    report = run_suite(probe)
    report["client"] = args.client
    report["scope"] = "Selected client, test hosts, current network route; not device clearance."
    print(json.dumps(report, indent=2))
    return {"verified_for_tested_chains": 0, "needs_attention": 1, "unknown": 2}[report["verdict"]]


if __name__ == "__main__":
    sys.exit(main())
