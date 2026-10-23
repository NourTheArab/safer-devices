# Incident checks and runtime verification

[العربية](../ar/incident-checks.md) · [Practical audit](practical-audit.md)

Reviewed **23 October 2026**. This is an incident snapshot. Refresh primary advisories before each audit, record the review date, match the exact product/platform/branch and report newer or unresolved guidance. A source link isn't permission to run its code.

## eMudhra: test actual clients, not just a browser

Start with [Mozilla's report](https://blog.mozilla.org/security/2026/10/20/protecting-firefox-users-following-the-compromise-of-emudhra-intermediate-certificates/) and the [incident's host list](https://emudhra.we-have-a-problem.com/). Different clients can have different certificate stores and revocation behavior. The test asks whether a selected client accepts the incident's public certificate chains. It doesn't send an exploit.

This snapshot includes fourteen chains, including the two no-CT hosts. Do not assume an earlier repair covers every current chain or every app. Never copy that laptop's private audit or trust settings.

### Approve network probes separately

Read [the probe's scope](../checks/README.md) and its source first. Explain that DNS resolvers and the public test sites see connection metadata such as the source IP. No account secrets, cookies, custom headers, report uploads or telemetry are required. Direct Python/Node/Bun handshakes may not use an organization's HTTP proxy; don't bypass required network controls. Use the approved proxy-aware route or report unknown.

The helper needs an already installed, trusted Python 3.9+ to launch. Don't install a runtime just to use it without approval. Run from the repository root after network approval:

```bash
python3 -I -S checks/tls_probe.py --allow-network
python3 -I -S checks/tls_probe.py --allow-network --client curl --executable /usr/bin/curl
```

The first checks only the launching Python's default SSL context. The second checks that exact curl. On Windows, invoke the reviewed Python path and pass the actual approved absolute curl path, not `/usr/bin/curl`. An absent Python leads to manual checks or an approved tool, not an automatic install.

For each trusted Node/Bun executable, substitute its exact approved absolute path:

```bash
python3 -I -S checks/tls_probe.py --allow-network --client node --executable /absolute/approved/node
python3 -I -S checks/tls_probe.py --allow-network --client bun --executable /absolute/approved/bun
```

These examples aren't permission to run an unknown executable. The Python/Node/Bun probes perform TLS handshakes without fetching HTTP bodies. Curl sends HEAD requests, disables its startup configuration, follows no redirects and requests no compression. Never add `-k`, `--insecure` or a certificate-verification bypass.

### Interpret the evidence

Two healthy hosts must connect and a self-signed host must be rejected before the fourteen incident tests count. A timeout, DNS failure, generic TLS failure or blocked control is **unknown**. Exit codes:

| Code | Meaning | Response |
|---|---|---|
| 0 | All fourteen chains were rejected after controls passed. | Record `verified_for_tested_chains` for that exact client and network route only. |
| 1 | At least one incident chain was accepted after controls passed. | Needs attention; identify the client/store and prepare a repair proposal. |
| 2 | A control failed, a test was inconclusive, or invocation was invalid. | Unknown; check the reported reason. Never label this a pass. |

Certificate rejection can arise from expiry, routing/security products or a different presented chain, not only from the intended key block. This probe does not fingerprint the live peer chain. Compare surprising results with current vendor guidance and a second approved method. No result clears other programs or proves historical traffic was safe.

Record a separate row for OS curl, Apple URLSession, each used Python/environment, pip, uv, Node, Bun, Java/JDK, Go-built tool and relevant desktop app. Unsupported or untested rows remain unknown. The helper **does not test** pip's vendored store, requests/certifi, uv, Java, Go binaries, containers or Apple URLSession.

### Cover the other stores with an approved specialist tool

[Wardlatch](https://github.com/deimos-hq/wardlatch) supplies additional client probes. First inspect its current release/source and options. Agree an exact version and source with the owner; don't silently use `latest`. Its maintainer's README describes network probes and container/context behavior; that isn't an independent audit.

For a version whose package release and source the agent has actually verified, prepare this command by replacing `REVIEWED_VERSION` and the agreed existing folder. It is an installation/execution proposal requiring approval, not part of the initial read-only pass:

```bash
npx --yes wardlatch@REVIEWED_VERSION --incident emudhra-2026-10 --no-containers --paths /absolute/approved/folder --json
```

Don't run the placeholder. Confirm from that version's help/source that these flags constrain it as intended. `--no-containers` avoids reaching a selected remote engine or executing container tools. The selected incident avoids automatically opting into broader secret/header/repository scans. Review the actual coverage; don't assume it found every virtualenv, app JDK or binary. Don't launch a suspected compromised interpreter to test it; inspect distribution metadata and use specialist incident response instead.

For a client not covered, use its current upstream probe instructions, translated into a bounded proposal with healthy and rejection controls. A missing probe is an explicit gap, not a reason to declare the app secure.

## Brotli, Node and embedded Bun

The [Node security release](https://nodejs.org/en/blog/vulnerability/october-2026-security-releases) covers the bundled decoder and other issues. Match the installed release line to current fixes. An application containing the decoder needs its own vendor update even if terminal Node is current. For Bun and related tools, inspect [Bun's issue](https://github.com/oven-sh/bun/issues/46352) and current vendor releases before deciding exposure.

For one approved file, this offline clue does not execute the target. Replace the example path; don't recursively scan private folders:

```bash
python3 -I -S - '/absolute/approved/binary-or-library' <<'PY'
from pathlib import Path
import sys
data = Path(sys.argv[1]).read_bytes()
print('control_count', data.count(b'FORMAT_EXUBERANT_NIBBLE'))
print('fix_count', data.count(b'FORMAT_BLOCK_SWITCH'))
PY
```

This checks two upstream-related strings, not exploitable behavior. A stripped, compressed or unrelated file may lack both. A marker cannot clear an app; match package provenance, version, actual linked library and a vendor advisory. Cap file size or use a trusted streaming search for unusually large files. Do not fetch a malicious compressed test payload.

## Go, Java, Python and package tooling

| Component | Concrete audit | Repair and verification |
|---|---|---|
| Go | Read the exact trusted compiler's `go version`; compare with the [release history](https://go.dev/doc/devel/release). Inventory Go-built apps separately. | Upgrade the supported toolchain after approval. Existing binaries generally require the app publisher's rebuild/update; compiler installation alone doesn't replace them. |
| Java | Inventory registered and app-private JDKs, vendor, support status and each store's test result. Consult the [vendor alert](https://www.oracle.com/security-alerts/alert-cve-2026-91403.html). | Use that vendor's applicable update. Confirm the new JDK selection and restart-dependent JVMs. A recent version alone doesn't prove the trust-store incident is fixed. |
| Python/pip/uv | Record each used environment, interpreter and installer distribution. Read metadata before launching suspected software. Consult [pip changes](https://pip.pypa.io/en/stable/news/) and [uv releases](https://github.com/astral-sh/uv/releases). | Update only the approved environment through its owning manager. Updating certifi doesn't necessarily update pip's vendored trust. Retest the actual installer/client. |
| Tailscale or another Go-built network app | Read installed app/service metadata and the [vendor bulletins](https://tailscale.com/security-bulletins). | Update the application and its running service through supported channels, with restart approval. |

## Servers and software-supply-chain exposure

Check these only where the software is used. Local-laptop scope doesn't authorize a VPS or production server. Record an applicable advisory or a reason the check doesn't apply:

| Area | Evidence and source | Decision |
|---|---|---|
| PHP | Running web-worker/runtime metadata, vendor builds and [PHP announcements](https://www.php.net/archive/2026.php), including the 23 October follow-up. | The website operator updates the server and verifies restarted workers. CLI PHP alone doesn't establish the serving version. |
| Next.js/sharp and Storybook | Selected project's dependency/lockfile versions against [Next.js guidance](https://nextjs.org/blog/nextjs-security-update-october-14-2026) and [Storybook advisory](https://github.com/storybookjs/storybook/security/advisories/GHSA-f2ph-cmg5-wxc8). | Review an approved dependency update and test/redeploy the affected app. Don't run its install scripts merely to inspect it. |
| Self-managed GitLab/Ruby | Publisher's installation metadata against [GitLab release guidance](https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-5-1-released/) and [Ruby's advisory](https://www.ruby-lang.org/en/news/2026/10/23/regexp-fixes-for-gitlab-cves/). | Escalate to the named operator and maintenance plan; don't change a remote host implicitly. |
| Potentially malicious packages | Product/version/artifact identity against the vendor's incident notice, such as [OVHcloud CLI](https://github.com/ovh/ovhcloud-cli/security/advisories/GHSA-862f-55f5-vmvw) or [LiteLLM](https://docs.litellm.ai/blog/security-incident-oct-21-2026). | Never execute a suspected package to get its version. Preserve evidence and plan clean-device credential recovery if exposure is confirmed. |
| Breached services and repository automation | Ask which providers were used and what kinds of credentials were stored, without reading values. Review selected workflow permissions, new files and unpinned external actions. | Match the provider's dated advisory; approve each revocation/rotation with a recovery plan. Don't scan secret values or history without separate scope. |

These rows are prompts to investigate, not a claim that every installation is affected. Additional current incidents belong in a reviewed, dated update. [Dom's checklist](https://github.com/dominikmartn/black-october-check) inspired the operational approach; its commands remain third-party material to review, not blanket authorization.
