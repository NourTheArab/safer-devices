# Recent incidents, explained

[العربية](../ar/why-this-matters.md) · [Back to the checklist](../README.md)

**Reviewed 23 October 2026.** This is a dated explanation, not a live incident feed. Links lead to current advisories; exposure depends on the actual software, configuration and updates in use.

Security headlines matter because the same software and trust systems sit underneath many services. One weakness can create urgent work for thousands of organizations at once. A vulnerability is a weakness; exploitation is its use in an attack; a confirmed breach requires evidence of unauthorized access. Those are different claims.

## Three incidents, three different problems

| When | What happened | Why it matters |
|---|---|---|
| 21 October 2026 | PHP disclosed two critical remote-code-execution flaws. | A vulnerable web server may run an attacker's code without a login. [PHP advisories](https://github.com/php/php-src/security/advisories/GHSA-w8hw-w9fx-j79w). |
| 17 October 2026, reported by Mozilla on 20 October | Eight eMudhra intermediate-certificate keys were compromised. | Forged certificates can enable website impersonation when an attacker can intercept a connection. [Mozilla's response](https://blog.mozilla.org/security/2026/10/20/protecting-firefox-users-following-the-compromise-of-emudhra-intermediate-certificates/). |
| September 2025, an earlier example | Shai-Hulud spread through compromised npm publisher accounts. | A familiar package name can deliver malicious code through the software supply chain. [GitHub's account](https://github.blog/security/supply-chain-security/our-plan-for-a-more-secure-npm-supply-chain/). |

The older example is included for its lesson. This page doesn't claim that AI caused every incident.

## PHP: why a server bug became a worldwide issue

**What happened:** PHP is software used to run websites. The project disclosed CVE-2026-109618 and CVE-2026-109619 on 21 October. Both are rated critical, with a CVSS v4 score of 9.2. Exploitation depends on the build and execution path. [First advisory](https://github.com/php/php-src/security/advisories/GHSA-w8hw-w9fx-j79w), [second advisory](https://github.com/php/php-src/security/advisories/GHSA-6wmf-4rv5-p3rp).

**Why the headline says “70%”:** that describes PHP's prevalence, not the number of breached websites. On our review date, W3Techs reported 69.3% among sites whose server-side language it could identify. Its survey denominator matters. It isn't a count of attacks or all internet-connected devices. [W3Techs methodology and current figure](https://w3techs.com/technologies/details/pl-php).

**What it means for the world:** shared infrastructure connects everyday services to the same maintenance emergency. Wikimedia described precautionary shutdowns of supporting services and acknowledged wiki outages while patching. A service going offline can be a protective decision; downtime alone doesn't establish data theft. [Wikimedia's service notice](https://diff.wikimedia.org/2026/10/21/impact-of-php-vulnerabilities-on-wikimedia-tools-and-services/).

**Who can fix it:** the website operator, hosting provider or product vendor must address the server runtime. WordPress says these are PHP issues and don't require a WordPress release to fix them. Updating a plugin or a visitor's browser doesn't establish that the site's PHP is patched. [WordPress guidance](https://wordpress.org/news/2026/10/critical-php-security-release/).

**What to do:** operators should inventory exposed PHP systems, apply vendor fixes, verify the running services and follow the advisory if patching is blocked. NCSC recommends considering temporary withdrawal of systems that cannot be updated or mitigated. That is an operator decision with service costs. [NCSC alert](https://www.ncsc.gov.uk/news/critical-security-issue-affecting-php).

**Why the date matters:** PHP published additional configuration-specific session guidance on 23 October. Keep following updates rather than treating an earlier version number as permanent clearance. [PHP's dated announcements](https://www.php.net/archive/2026.php).

## eMudhra: the trust layer also needs updates

HTTPS certificates help software recognize the site it is connecting to. Mozilla reported compromised intermediate keys and distributed certificate blocks. That response protects Firefox within its documented scope; other software can have different trust stores and update paths. [Mozilla's incident report](https://blog.mozilla.org/security/2026/10/20/protecting-firefox-users-following-the-compromise-of-emudhra-intermediate-certificates/).

**Practical lesson:** update affected apps through their vendors and verify the relevant runtime or trust-store response. A successful browser update doesn't clear every application. Avoid improvised certificate removal or disabling certificate checks. The [developer guide](developers.md) explains scoped runtime checks.

## Shai-Hulud: a trusted name can carry an untrusted update

GitHub described a worm delivered through malicious install scripts after publisher-account compromise. It could steal multiple kinds of secrets and replicate. This was an actual malicious-package incident, rather than only a newly disclosed software weakness. [GitHub's September 2025 report](https://github.blog/security/supply-chain-security/our-plan-for-a-more-secure-npm-supply-chain/).

**Practical lesson:** installing a package is permission to run software. Check the source and release, limit the credentials available to build tools and agents, and follow the incident-specific response if an affected package ran. Replacing a package doesn't recover stolen credentials. Keep that work within the [approved developer-tool scope](developers.md).

## What stronger AI changes

AI can help uncover weaknesses and develop attacks faster, and can help defenders investigate them. OpenAI describes its role in the PHP research and coordinated response; that is a participant's account. Discovery still needs human validation, fixes and deployment. [OpenAI's disclosure account](https://openai.com/index/coordinated-disclosure-of-critical-vulnerabilities/).

NCSC's May 2026 assessment warns organizations to prepare for a wave of vulnerability patches. It recommends prioritizing exposed systems and improving update capacity. This is a planning assessment, not proof of an inevitable collapse or a timetable for the next attack. [NCSC's patch-wave analysis](https://www.ncsc.gov.uk/blogs/prepare-for-vulnerability-patch-wave).

Our practical conclusion: prepare for more frequent security work and a shorter time to respond. An increasingly capable assistant also needs bounded access. NCSC recommends layered safeguards, oversight and a way to stop an agent; prompts alone don't enforce those controls. [Agentic-AI guidance](https://www.ncsc.gov.uk/blogs/managing-the-cyber-risk-of-agentic-ai).

## Preparation that remains useful after today's headlines

| For | Useful preparation | Evidence to look for |
|---|---|---|
| Everyone | Work through the [six starting checks](../README.md#start-here). Protect recovery and test a backup restore. | Enabled settings, completed updates and a recovered test file. |
| People using online services | Follow the provider's official incident notices and recovery instructions when relevant. | A statement covering the particular service and any action required of customers. |
| Teams running websites | Keep a software inventory, named ownership, an update/restart procedure and a service-continuity plan. Include embedded runtimes and containers. | The applicable vendor advisory, evidence of the deployed fix and a normal workflow test. |
| Teams using agents | Limit tools, files, accounts and network access to the task. Preserve approval gates and private reports. | Technical boundaries and observable actions, in addition to the [agent prompt](../prompts/AGENT-AUDIT.md). |

The checklist is a starting point, not protection against every attack. For a suspected compromise, use [getting help](getting-help.md) before cleanup destroys evidence.

## Articles to read and share

- [CNN Arabic: the reader-suggested PHP story](https://arabic.cnn.com/world/article/2026/10/22/global-websites-shut-down-after-ai-found-a-flaw-affecting-70-of-the-internet). Arabic context. This page couldn't be retrieved during review, so it isn't the evidence for our technical claims.
- [Axios: PHP and the security response](https://www.axios.com/2026/10/22/php-vulnerability-security-update-websites). News context.
- [The Guardian: PHP explained](https://www.theguardian.com/technology/2026/oct/22/what-is-php-computer-language-flaw-causing-global-website-shutdowns). News explainer.
- [The PHP Foundation: discovery, fixes and maintenance capacity](https://thephp.foundation/blog/2026/10/21/todays-php-security-release-and-how-were-strengthening-php-security/). First-party account of the work behind the response.

Reporting explains the stakes. Current product advisories determine the applicable response. When sharing a new incident, include its date, the affected component, confirmed impact, unresolved questions and the specific next action.
