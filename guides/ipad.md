# Check an iPad, one setting at a time

[العربية](../ar/ipad.md) · [Practical audit](practical-audit.md)

Reviewed **23 October 2026**. An iPad is a separate audit target, not a Mac with a smaller screen. Confirm that this is the device being checked and whether it belongs to work/school. If the assistant can't read its settings, use the [guided chat route](chat-only.md); label evidence as owner-reported.

## Start with the update screen

Open **Settings > General > Software Update**. Record iPadOS version, any offered security update and a pending restart, without sharing the device name, serial number or Apple Account. Check the model's supported updates using [Apple's iPadOS guide](https://support.apple.com/guide/ipad/update-ipados-ipad9a74c576/ipados). Approve installation and save work before restarting. Reopen the screen afterward; a download isn't completion.

## Work through the remaining settings

| Check | Where/how | Finished evidence |
|---|---|---|
| Apps | App Store update screen; review installed apps and their publisher/source. | Approved updates completed; unfamiliar apps investigated, not automatically removed. |
| Passcode and biometrics | Face ID & Passcode or Touch ID & Passcode, depending on model. | A passcode is set; intended biometric access and lock-screen access are understood. No passcode or biometric data enters chat. |
| Lock timing | Settings > Display & Brightness > Auto-Lock, subject to policy/accessibility needs. | Intended lock delay confirmed, without disrupting necessary accessibility. |
| Backup | Settings > Apple Account > iCloud > iCloud Backup, or the actual computer-based backup method used. | Latest successful backup and included data confirmed; restore capability is separate. Never erase the iPad to test a backup. |
| Privacy permissions | Settings > Privacy & Security, including location, photos, contacts, camera, microphone, Bluetooth and local network where shown. | Apps and broad permissions recognized; each proposed reduction approved separately. |
| Safari/extensions | Search Settings for Safari and Extensions; review installed extensions and allowed website access. | Recognized extensions and their permissions. Never remove wallet/password-manager access under generic cleanup. |
| VPN and management | Settings > General > VPN & Device Management, where present. | Profiles/VPN are recognized or recorded for IT/specialist review. No removal or new root/profile installation by default. |
| Apple Account and other accounts | Official account-security screens, using the [account guide](accounts.md). | MFA explicitly enabled, recovery privately accessible, recognized sessions and reviewed connected apps. Owner handles sign-in. |
| Shared use and physical access | Ask whether others use this iPad and whether sensitive notifications appear on the locked screen. | An intentional access arrangement, without opening private messages or browsing history. |

For backup instructions use [Apple's iCloud guide](https://support.apple.com/en-us/108366). UI labels vary by iPadOS version and language: search Settings and verify the current Apple guide rather than claiming a missing option was checked.

## How incidents apply to an iPad

Follow [the dated incident-review list](../sources/INCIDENT-REVIEW.md). Ask whether affected apps or remotely hosted services are used. Keep iPadOS and affected apps on their supported vendor updates. A successful Safari certificate check doesn't clear every third-party app's trust behavior. Record app-specific vendor evidence or unknown coverage.

PHP on a website is repaired by its operator, not by running a Mac shell command on an iPad. A remote server, development environment or library used through an iPad is a separate system needing explicit scope. Don't install shell emulators, jailbreak, sideload diagnostic apps or add a management profile to imitate a laptop audit. Local Node/Bun/Java/Go checks generally don't apply to ordinary iPad use; any unusual environment must be assessed on its own evidence.

## Extra protection when risk warrants it

For targeted-risk work, review [Apple Lockdown Mode](https://support.apple.com/en-us/105120) and specialist support in [getting help](getting-help.md). Explain feature costs and ask before enabling restrictions. A routine settings review cannot rule out sophisticated spyware or establish attacker identity.

End with checked, owner-reported, independently observed, changed with approval, deferred and unknown. No promise of a complete device scan.
