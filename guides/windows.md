# Check a Windows laptop

[العربية](../ar/windows.md)

Use Windows Settings and Windows Security first. A managed work or school device may have policies you shouldn't override.

## Update and restart

Open **Settings > Windows Update**. Install applicable security updates after saving work and checking your backup. Complete the restart and check again. Update the browser and other apps too.

Confirm that your Windows edition and version still receive security updates. An older release may require a supported upgrade or a specific support program. Check [Microsoft's release and lifecycle information](https://learn.microsoft.com/en-us/windows/release-health/); don't rely on an old checklist's version numbers.

## Check Windows Security

Open **Windows Security** and review:

- **Virus & threat protection:** check protection status and any warnings. Some organizations use another managed provider; don't install competing security software automatically.
- **Firewall & network protection:** confirm protection for the active network. Use the appropriate profile for a trusted home network or an untrusted public one.
- **Device security:** review reported hardware protections. Changes involving firmware, Secure Boot or recovery access need a separate plan.

Use Microsoft's guides to [Windows Security](https://support.microsoft.com/en-us/windows/help-protect-my-device-with-windows-security-1a5b8102-c93d-0573-8fd3-b2d33a1e5386), [firewall settings](https://support.microsoft.com/en-us/windows/security/windows-security/firewall-and-network-protection-in-the-windows-security-app), and [device security](https://support.microsoft.com/en-us/windows/security/windows-security/device-security-in-the-windows-security-app). Don't turn protection off to make a download or script run.

## Encryption and recovery

Search Settings for **Device encryption** or **BitLocker**. Availability depends on hardware, edition and account setup. Check actual state rather than assuming it is enabled.

Before enabling encryption or changing recovery settings, privately confirm where the recovery key is kept and whether you can access it from another trusted device. An agent should verify the state without displaying the key. [Microsoft's encryption guide](https://support.microsoft.com/en-us/windows/security/encryption/device-encryption-in-windows) explains the supported options.

## Everyday access

Require authentication when the laptop locks or wakes. Review Remote Desktop, sharing features, startup apps and browser extensions. Keep services you rely on; disable unused ones only after understanding the effect. Don't remove workplace management software because its name is unfamiliar.

Check the latest backup, confirm important folders are included, and recover a harmless test file. A synced folder alone doesn't establish that deleted or overwritten files can be recovered. [NCSC's backup guide](https://www.ncsc.gov.uk/collection/top-tips-for-staying-secure-online/always-back-up-your-most-important-data) covers choosing and testing a separate copy.

**Finished:** update/restart completed, security warnings understood, firewall/encryption state checked, recovery privately available, and a restore test passed.
