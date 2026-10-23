# Read-only certificate probe

[العربية](../ar/tls-probe.md) · [Incident runbook](../guides/incident-checks.md) · [Source](tls_probe.py)

This is a small diagnostic helper, not a hardening installer. It uses Python's standard library and optionally invokes one explicitly selected, trusted curl/Node/Bun executable. It performs no repairs, package installs, account access or file writes. It creates no report unless the owner separately chooses output redirection.

## Before running

- Read the source and current [incident host list](https://emudhra.we-have-a-problem.com/). Snapshot reviewed **23 October 2026**.
- Use an already installed trusted Python 3.9+; don't run an interpreter suspected of compromise. Launching Python with `-I -S` avoids Python startup/site customization, but also means this doesn't test those customizations or third-party packages.
- Agree network use. The public hosts and DNS resolver can observe source-IP/connection metadata. No secrets, cookies or report uploads are sent by this code.
- Python/Node/Bun make direct TLS connections and may not follow an HTTP proxy. Respect enterprise network policy; don't bypass a required proxy. Curl respects its environment/proxy route but ignores `.curlrc`; results have that narrower scope. Existing trust-related configuration can affect results.
- Don't add verification bypasses, arbitrary target URLs, client certificates, credentials or HTTP headers.

## Run one selected client

From the repo root, after network approval:

```bash
python3 -I -S checks/tls_probe.py --allow-network
python3 -I -S checks/tls_probe.py --allow-network --client curl --executable /usr/bin/curl
```

For Node/Bun, use `--client node` or `--client bun` and the exact approved absolute `--executable` path. On Windows, use the selected Python and client paths for that computer. Bun is launched with automatic dotenv loading and package installation disabled. Node startup/preload configuration can execute code; establish a trusted launch context or leave the check unknown. The helper never discovers or executes arbitrary installed programs. Missing dependencies stay unknown until an installation is separately approved.

Healthy controls: `github.com` and `emudhra.we-have-a-problem.com`. Rejection control: `self-signed.badssl.com`. Incident probes: twelve DV/OV/EV × G3B/G3C × direct/AAA-chain hosts, plus `dv-g3b-noct-emudhra.we-have-a-problem.com` and `dv-g3b-aaa-noct-emudhra.we-have-a-problem.com`. The complete fixed host list is visible in the source. Check it against the current advisory before use. Probe hosts can become unavailable or change with time.

Python and Node/Bun perform only TLS handshakes. Curl uses HEAD, no compression and no redirects. No HTTP body is needed. Each network operation has a timeout; OS DNS resolution can take longer. Expect up to a few minutes on slow networks. The JSON includes only fixed public hostnames, statuses and scope; child error text is never copied into it.

## Results and limits

- Exit 0: `verified_for_tested_chains`, all fourteen rejected after healthy and self-signed controls passed.
- Exit 1: `needs_attention`, at least one incident chain accepted after controls passed.
- Exit 2: `unknown`, incomplete/error/control-failed result, or invalid invocation.

It measures selected-client behavior on the current route, not historical compromise, universal key distrust or device security. It does not fingerprint live peer chains. Expiry and TLS-intercepting security products can explain rejection too. It doesn't cover Apple URLSession, pip/requests/certifi, uv, Java, Go apps or containers. Track those separately in the incident runbook.

Sources for the primitives: [Python SSL](https://docs.python.org/3/library/ssl.html), [Node TLS](https://nodejs.org/api/tls.html), [curl options](https://curl.se/docs/manpage.html). Bun compatibility is deliberately reported from actual probe behavior, not assumed from its version.

See [the dated validation record](VALIDATION.md) for actual client coverage and its limits.

## Offline tests

```bash
python3 -m unittest discover -s tests -v
```

Tests simulate certificate errors, timeouts, accepted chains, failed controls and missing network approval. They neither connect to test hosts nor certify the laptop. Additional real-client smoke-test coverage belongs in a dated, scoped release record.
