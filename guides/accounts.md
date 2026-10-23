# Accounts: start with your email

[العربية](../ar/accounts.md)

Your main email account often controls recovery for other accounts. Start there, then review your password manager, cloud storage, financial accounts, and important work services.

## Check authentication

Open the provider's security page directly. Check the selected account, especially if you use several Google or Microsoft accounts.

- Use a unique password. Let your existing password manager generate and store it privately.
- Prefer passkeys or hardware security keys where supported. An authenticator is another second-step option.
- Confirm that two-step verification actually shows **enabled**. An authenticator can be registered before activation is complete. Passkey sign-in may already provide strong protection, but check what happens when using a password instead.
- Keep a recovery method you can access. Privately check your recovery-code backup. Don't show codes to an agent, and don't remove your only working sign-in method.

Follow your provider's instructions for [Google](https://support.google.com/accounts/answer/185839?hl=en), [Apple](https://support.apple.com/en-us/102660), [Microsoft](https://support.microsoft.com/en-us/accounts-billing/security/how-to-use-two-step-verification-with-your-microsoft-account), [GitHub](https://docs.github.com/en/authentication/securing-your-account-with-two-factor-authentication-2fa/configuring-two-factor-authentication), or [Proton](https://proton.me/support/two-factor-authentication-2fa). An agent can verify the final status while you handle sign-in and enrollment.

## Review sessions

A session is a browser or app's signed-in access. One device can have several sessions. Syncing, VPNs, and travel can explain unfamiliar times or locations.

Review device type, browser/app, last activity, and whether you still own it. Sign out a lost, retired, or genuinely unrecognized device after checking the effect. Keep a recognized current session available so you don't lock yourself out. [Google explains device sessions here](https://support.google.com/accounts/answer/3067630).

An activity log and a session list aren't the same. For example, [Microsoft's recent-activity page](https://support.microsoft.com/en-us/accounts-billing/security/what-is-the-recent-activity-page?ns=MSFTTEAMS) covers selected events, not every access.

## Review connected apps

Signing in to a website with Google isn't automatically permission to read Gmail. Check the individual grant:

| Access shown | What to consider |
|---|---|
| Basic name/email/profile | Do I still use this login? |
| Read calendar | Does this scheduling or note-taking app still need it? |
| Read/send email | Do I still trust and use this mail integration? |
| Read/write/delete files | Which workflow needs this broad access? |

Remove only the unused permission you intend to revoke. Where supported, keep basic sign-in while removing data access. Removing a grant can break an integration and doesn't erase information already held by the service. [Google's linked-app controls](https://support.google.com/accounts/answer/13533235) explain the difference.

**Finished:** protection explicitly enabled, recovery privately checked, devices recognized, unnecessary grants removed with approval, and an ordinary sign-in still works.
