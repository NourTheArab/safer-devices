# Sources and optional tools

[العربية](../ar/sources.md)

Reviewed **23 October 2026**. Follow the current vendor page for your device and release. A source appearing here doesn't mean its software has been independently audited or that every recommendation fits your situation.

## Start with these

| Source | Useful for |
|---|---|
| [EFF: Your Security Plan](https://ssd.eff.org/module/your-security-plan) | Choosing protections around your actual needs and risks. |
| [NCSC: Backing up your data](https://www.ncsc.gov.uk/collection/top-tips-for-staying-secure-online/always-back-up-your-most-important-data) | Planning separate copies and checking recovery. |
| [Access Now Digital Security Helpline](https://www.accessnow.org/help/) | Specialist support for civil society, journalists and human-rights defenders. Check current eligibility/contact guidance. |

## Accounts and browsers

| Provider | Official guidance |
|---|---|
| Google | [Two-step verification](https://support.google.com/accounts/answer/185839?hl=en), [device sessions](https://support.google.com/accounts/answer/3067630), [linked apps and data access](https://support.google.com/accounts/answer/13533235). |
| Apple | [Account two-factor authentication](https://support.apple.com/en-us/102660). |
| Microsoft | [Two-step verification](https://support.microsoft.com/en-us/accounts-billing/security/how-to-use-two-step-verification-with-your-microsoft-account), [recent activity](https://support.microsoft.com/en-us/accounts-billing/security/what-is-the-recent-activity-page?ns=MSFTTEAMS). |
| GitHub | [Configure two-factor authentication](https://docs.github.com/en/authentication/securing-your-account-with-two-factor-authentication-2fa/configuring-two-factor-authentication). |
| Proton | [Two-factor authentication options](https://proton.me/support/two-factor-authentication-2fa). |
| Chrome | [Manage extensions and website access](https://support.google.com/chrome/answer/2664769?hl=en). |
| Firefox | [Extension permissions](https://support.mozilla.org/en-US/kb/permission-request-messages-firefox-extensions), [private-window access](https://support.mozilla.org/en-US/kb/extensions-private-browsing). |
| OpenAI | [Browser extension capabilities and site permissions](https://learn.chatgpt.com/docs/chrome-extension). |

## Devices

| Platform | Official guidance |
|---|---|
| Mac | [Software updates](https://support.apple.com/en-us/108382), [FileVault](https://support.apple.com/guide/mac-help/protect-data-on-your-mac-with-filevault-mh11785/mac), [firewall](https://support.apple.com/guide/mac-help/block-connections-to-your-mac-with-a-firewall-mh34041/mac), [Time Machine](https://support.apple.com/en-us/104984). |
| Windows | [Windows Security](https://support.microsoft.com/en-us/windows/help-protect-my-device-with-windows-security-1a5b8102-c93d-0573-8fd3-b2d33a1e5386), [firewall](https://support.microsoft.com/en-us/windows/security/windows-security/firewall-and-network-protection-in-the-windows-security-app), [device security](https://support.microsoft.com/en-us/windows/security/windows-security/device-security-in-the-windows-security-app), [device encryption](https://support.microsoft.com/en-us/windows/security/encryption/device-encryption-in-windows), [release health](https://learn.microsoft.com/en-us/windows/release-health/). |
| iPhone/iPad | [System updates](https://support.apple.com/en-us/118575). |
| Android | [OS, security and Google Play system updates](https://support.google.com/android/answer/7680439). |
| Higher-risk Apple users | [Genuine threat notifications](https://support.apple.com/en-us/102174), [Lockdown Mode and its tradeoffs](https://support.apple.com/en-us/105120). |

## Optional projects

For dated incident explanations, reporting links and preparation as AI capabilities change, see [recent incidents, explained](../guides/why-this-matters.md).

Read the project's current documentation and inspect the exact release/source before approving installation or execution. We reviewed the linked documentation; this isn't a full code audit, endorsement, or guarantee. Start with your device's built-in controls.

| Project | Scope and useful limits |
|---|---|
| [Wardlatch](https://github.com/deimos-hq/wardlatch) | Incident-specific checks, including runtime TLS probes. Its documentation currently targets macOS/Linux and says Windows checks are incomplete/unsupported. Probes contact public hosts; default container discovery can reach the active engine, including a remote context. Review the current `--no-containers` option for a local-only scope. A result covers only the tested incident and components. |
| [fort](https://github.com/djadmin/fort) | macOS settings audit. The publisher describes the audit as local/offline, and documents a preview mode. Fix options can change system settings. Its reports may include machine identity and serial numbers; keep reports private. A score isn't a forensic or compliance certification. |
| [LuLu](https://github.com/objective-see/LuLu) | An additional macOS firewall with app-connection controls. Installing it or changing rules needs a deliberate decision; blocking an app may break syncing, updates or other features. Read [the publisher's usage guide](https://objective-see.org/products/lulu.html). |
| [Dom's Black October checklist](https://github.com/dominikmartn/black-october-check) | Technical checks and fixes for incidents current in October 2026. Inspiration for this guide, not a timeless list of safe versions. Individual fixes may need administrator access, service restarts or trust-store changes. Use fresh vendor advisories. [Original gist](https://gist.github.com/dominikmartn/629ef73b1ebca67a0d0d4938a932a371). |
| [Docker Engine security](https://docs.docker.com/engine/security/) | Container/daemon isolation and configuration considerations. Inspect the actual deployment. |
| [Colima](https://github.com/abiosoft/colima) | Local VM management for container runtimes. Starting an existing VM can restart its configured workloads. |

Package runners such as `npx` may fetch and execute software. An apparently convenient one-liner is still an installation/execution decision. This guide intentionally doesn't include a remote-script installer.

## Incidents, impact and AI

These primary sources were checked on **23 October 2026**:

- [PHP's dated announcements](https://www.php.net/archive/2026.php) and [critical advisories](https://github.com/php/php-src/security/advisories/GHSA-w8hw-w9fx-j79w): applicable fixes and follow-up guidance.
- [WordPress's response](https://wordpress.org/news/2026/10/critical-php-security-release/) and [Wikimedia's service notice](https://diff.wikimedia.org/2026/10/21/impact-of-php-vulnerabilities-on-wikimedia-tools-and-services/): product responsibility and operational impact.
- [Mozilla's eMudhra response](https://blog.mozilla.org/security/2026/10/20/protecting-firefox-users-following-the-compromise-of-emudhra-intermediate-certificates/): the certificate-trust incident.
- [GitHub's Shai-Hulud report](https://github.blog/security/supply-chain-security/our-plan-for-a-more-secure-npm-supply-chain/): an explicitly older, September 2025 example.
- [NCSC's patch-wave analysis](https://www.ncsc.gov.uk/blogs/prepare-for-vulnerability-patch-wave) and [agentic-AI guidance](https://www.ncsc.gov.uk/blogs/managing-the-cyber-risk-of-agentic-ai): preparedness and bounded autonomy.
- [OpenAI's PHP disclosure account](https://openai.com/index/coordinated-disclosure-of-critical-vulnerabilities/): a participant's account, not independent proof of every future-risk prediction.

The explainer separately labels journalism. The reader-suggested CNN Arabic page couldn't be retrieved during review and isn't the evidence for technical claims. Publication dates, observed harm and predictions must remain distinct.

## Freshness and provenance

Prefer the vendor's advisory or original research over a social post summarizing an incident. Match the product, platform and release branch. Source updates can change scope, test hosts, permissions and fixed versions.

When revising a guide, record which pages were actually read and update the review date only for material rechecked. The local maintenance script checks document structure and links inside this repository. It doesn't contact external sites, validate every security claim or scan a laptop.

No text or scripts from linked projects are bundled here. Their licenses and responsibility for their releases remain with their authors.
