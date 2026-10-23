# Check a Mac

[العربية](../ar/mac.md)

Start in System Settings. You don't need a terminal or another security app for these checks. On a managed Mac, coordinate changes with your IT team.

## Updates and backup

Search System Settings for **Software Update**. Check installed apps through their official updater or the App Store too. Save work, make a backup, and complete required restarts. [Apple's update instructions](https://support.apple.com/en-us/108382) cover supported versions.

Search for **Time Machine**. Check the latest completed backup and whether the destination is connected. A configured destination isn't evidence of a recent backup. Recover a harmless file to confirm the restore process. Enabling a new backup may require formatting a disk, so check what is on it first. [Apple's Time Machine guide](https://support.apple.com/en-us/104984) explains setup and recovery.

## Protect a lost laptop

- Check **FileVault** under Privacy & Security. It protects access to the startup disk. Before changing encryption, privately confirm how you would recover access. Never paste the recovery key into chat. [Apple's FileVault guide](https://support.apple.com/guide/mac-help/protect-data-on-your-mac-with-filevault-mh11785/mac) explains the options.
- Require authentication after sleep or screen lock. Choose a delay that fits how and where you work.
- Review whether automatic login is enabled. Preserve accessibility arrangements and any managed policy.

## Network and remote access

Search settings for **Firewall** and review its state. A firewall helps control incoming connections; it doesn't inspect every app for theft or malware. Don't block every service without checking what you use. [Apple's firewall guide](https://support.apple.com/guide/mac-help/block-connections-to-your-mac-with-a-firewall-mh34041/mac) explains the controls.

Under **General > Sharing**, review Remote Login, Screen Sharing, Remote Management and File Sharing. Disable only services you don't need, after approval. Incoming Remote Login lets another computer connect into your Mac; turning it off is different from removing your ability to SSH out to a server.

An agent can identify local listening ports and the owning program without dumping process arguments. It must distinguish local-only bindings from broader ones. Actual reachability also depends on firewall, router and VPN rules. A port number alone doesn't identify spying.

## App permissions

Review Accessibility, Screen Recording, Full Disk Access, Camera and Microphone permissions. Recognize the apps with access. Don't automatically remove an accessibility tool or agent permission that you rely on. Don't grant broad access just to make an audit easier.

Keep built-in signature, malware and system-integrity protections enabled. If a command reports a surprising state, check the normal settings screen too: a restricted agent environment may not see the actual host state. Optional settings auditors are listed in [Sources and tools](../sources/README.md).

**Finished:** the settings you checked are recorded, backup recovery works, updates have taken effect, and normal work still functions. This isn't a forensic clearance.
