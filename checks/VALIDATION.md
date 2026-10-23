# Probe validation record

[العربية](../ar/probe-validation.md) · [Probe scope](README.md)

Date: **23 October 2026**. This records development validation of this helper, not a security assessment of a person or device. No private audit reports, account data, host identifiers or network addresses are published.

## Automated tests

The full suite passed **24 tests**: documentation validation plus TLS control/verdict behavior, timeouts, certificate-error classification, execution/network gates, Bun startup restrictions and an offline Node event adapter harness. Transport responses are mocked; the Node harness replaces the TLS module and opens no sockets. CI runs these offline tests.

## Public-host smoke tests

Selected clients on a macOS development environment were tested with approved network access. Each completed suite required both healthy hosts to connect, the self-signed control to be rejected, and all fourteen incident chains to be rejected:

| Selected client | Tested version | Observed result |
|---|---|---|
| Python default SSL | 3.13.2 | Controls passed; 14 rejected, 0 accepted, 0 unknown. |
| OS curl | 8.7.1 | Controls passed; 14 rejected, 0 accepted, 0 unknown. |
| Standalone Node | 26.12.1 | First run: healthy control inconclusive, incident hosts skipped and exit 2. A later healthy-control check connected; full retest passed with 14 rejected. No cause was established for the initial failure. |
| Standalone Bun | 1.4.4 | Final adapter with `--no-env-file --no-install`: controls passed; 14 rejected, 0 accepted, 0 unknown. |

The records show observed behavior on that route and date. The probe does not fingerprint the presented chains, so rejection isn't independent proof of the intended key block. No malware payload was downloaded and no security settings were changed by the helper.

## Untested and out of scope

No live Windows/Linux, iPadOS, alternative client versions, proxy-enforced enterprise network, Java, Go binary, pip/uv, Apple URLSession, app-bundled runtime or container probe was validated by these smoke tests. The runbooks require those checks or explicit unknown/not-applicable results as relevant. A newer release, changed endpoint or network route needs a new review and test.

The agent acceptance scenarios are authored review cases, not an automated benchmark showing that every assistant follows them. Document checks verify local links and structure; they don't prove that external advisories remain available or that a friend's audit occurred.
