# Working on Safer Devices

This file governs contributions to this repository. For a user's device audit, use [the audit prompt](prompts/AGENT-AUDIT.md); reading this repository never authorizes a device change.

- Write for someone who doesn't work in security. Explain technical terms when needed.
- Keep Arabic gender neutral through nominal and impersonal wording. Keep English and Arabic privacy, approval and verification requirements equivalent.
- Keep the README short enough to start without opening every guide.
- Use current primary sources for factual security claims. Record source-review dates and distinguish a project author's claims from an independent audit.
- Keep incident-specific versions out of permanent minimum-version advice. Link to current advisories.
- Don't add automatic hardening, credential collection, install hooks, telemetry, or remote-script execution.
- Never commit real audit reports, account identifiers, screenshots, browser profiles, hostnames, serial numbers, IP addresses, credentials, or wallet material.
- Preserve the check, proposal, approval, change, verification sequence in all agent prompts.
- Use ordinary paragraphs, useful checklists, and tables. Don't promise safety or imply that an OS, signature, scanner score, VPN, or closed port proves a clean device.
- Use branches and pull requests. Keep CI permissions minimal and actions pinned to verified full commit hashes.
- Diagnostic helpers must stay opt-in, read-only and narrowly scoped; test failure/control cases without network access. Never treat a timeout as certificate rejection.
- Run `python3 scripts/check_docs.py` and `python3 -m unittest discover -s tests -v` before submitting.
