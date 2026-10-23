# When the assistant cannot inspect your device

[العربية](../ar/chat-only.md) · [Practical audit](practical-audit.md)

Reading a repository doesn't give a chat access to laptop files, phone settings, account sessions or an administrator prompt. Tools and permissions determine what can be checked. The assistant must describe its actual access, not infer it from the app or device used to send a message.

## A useful first reply

The assistant should say which access is missing, ask which device is being checked and begin one useful manual check. Avoid a long intake questionnaire. If the device and scope were already stated, don't ask again. A good next step for an iPhone/iPad is:

> I can guide these checks, but can't read this device's settings from this chat. Let's start with updates. On the device you want checked, open Settings > General > Software Update. Tell me only whether an update is offered, a restart is pending, or it says up to date, plus the version if visible. Don't share your Apple Account, serial number or passcode.

Don't call that an automated scan. A result the owner reads from the UI is **owner-reported** evidence, not independent inspection. Questions/forms in a chat are optional ways to collect nonsensitive answers, not a scanner or a new security permission.

## Walk through the actual settings

Work one item at a time, using current manufacturer instructions for the device version. No screenshot is required; redacted setting states suffice. If a screenshot would expose account identifiers or recovery material, use a short description instead.

| Check | iPhone/iPad | Android | Evidence to request |
|---|---|---|---|
| OS update | Settings > General > Software Update. | Settings, then search for software/security updates; labels depend on vendor. | Version/date, offered update and restart state. |
| App updates | App Store account/update screen. | Play Store app-update screen and vendor store if used. | Pending/completed state, without account details. |
| Lock and recovery | Settings > Face ID/Touch ID & Passcode; never reveal the passcode. | Screen lock and biometric settings. | Lock configured; recovery access privately available. |
| Backup | Settings > Apple Account > iCloud > iCloud Backup, where used. | Settings, then search Backup for the chosen provider. | Latest successful date and included data; restore remains untested until an approved test. |
| App permissions | Settings > Privacy & Security. | Privacy/Permission manager. | Recognized apps and broad permissions, no personal content. |
| Management/VPN | Settings > General > VPN & Device Management. | Search VPN, device admin and work-profile settings. | Whether recognized management exists; don't remove it automatically. |
| Accounts | Official account-security pages for chosen providers. | Same. | MFA enabled state, recognized sessions and app-access scope; never codes/keys. |

Apple sources: [updates](https://support.apple.com/en-us/118575), [iCloud backup](https://support.apple.com/en-us/108366), [app permissions](https://support.apple.com/guide/iphone/control-access-to-information-in-apps-iph251e92810/ios). Android sources: [updates](https://support.google.com/android/answer/7680439), [permissions](https://support.google.com/android/answer/9431959). Paths may change; verify before guiding.

No profiles, side-loaded apps, certificate installers or “remote scanner” links are needed for this walkthrough. An unfamiliar profile needs investigation with the owner/IT; don't erase it as a shortcut. Targeted-risk options and specialist support are in [phone guidance](phones.md).

## For a laptop audit from a phone chat

Ask whether the owner wants manual laptop instructions or to open the guide in an agent actually connected to that laptop. Never tell them a phone chat has acquired desktop access. Any new agent installation or permission expansion is a separate decision; unrestricted access isn't required.

Copy this to the chosen laptop assistant with the repository URL:

```text
Read README.md, prompts/AGENT-AUDIT.md and guides/practical-audit.md.
First state whether your tools actually run on my laptop or in a remote sandbox.
Perform the authorized read-only checks you can, including applicable app-bundled
runtimes and current incident checks. Report inaccessible items as unknown.
Explain and ask before each change or additional installation. Verify each
approved change and keep my AI apps, passwords and wallets untouched.
```

For iPad specifically, use [the iPad checklist](ipad.md), including Safari extensions and management profiles.

## Finish honestly

Summarize what the owner reported, what the assistant independently observed and what remains unknown. A settings walkthrough can't rule out spyware or inspect hidden app runtimes. Keep those gaps visible and continue the checks that are possible.
