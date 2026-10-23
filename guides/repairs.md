# One finding, one approved repair, one retest

[العربية](../ar/repairs.md) · [Practical audit](practical-audit.md)

Finding an issue isn't the finish line. Prepare the exact change for this device, ask for approval, preserve recovery, apply it and recheck the outcome. Never use the examples below as a bulk-fix script. They don't authorize changes by themselves.

## Prepare a reviewable proposal

Use [the approval template](../prompts/APPROVE-ONE-CHANGE.md). Include the selected path/product/account, current evidence, dated vendor advisory, exact command or UI action, permissions, service impact, backup and rollback, and the independent verification. Resolve examples and placeholders before asking; don't ask the owner to approve an unspecified fix.

Prefer official updates. Confirm publisher/signature and a checksum from a trustworthy source where available. A checksum beside an untrusted download doesn't establish provenance. A managed device or uncertain recovery path needs its administrator's decision.

## Update the installation that is actually affected

These are **proposal examples**, only after confirming this package belongs to Homebrew and checking the current vendor fix. Choose the exact formula already installed; names can differ by release line. Don't run both commands or upgrade unrelated packages by default:

```bash
brew upgrade bun
brew upgrade node
```

A non-Homebrew installation needs its own supported updater. Updating terminal Node doesn't update a desktop app's embedded Node/Bun/Electron. Update that signed app as a whole. Existing AI tools stay untouched unless their specific update is approved.

For Go or Java, choose the supported vendor/distribution and architecture, verify the official artifact, preserve the old installation outside active discovery if needed, and show the installation command before approval. Don't blindly copy an old archive URL. After approval, verify compiler/JDK selection, compile/run a harmless test where appropriate, repeat TLS checks and identify dependent services needing restart. Don't expose Java system-property dumps or Go environment values.

For an old or unsupported runtime, propose migration to a supported branch and test dependencies. A newer compiler doesn't rebuild existing applications. Keep a private inventory of which app binaries remain unresolved.

## Repair certificate trust with evidence

1. Identify the failing client and its actual store. Save the pre-change probe result privately, including controls.
2. Prefer an applicable OS, app, runtime or trust-package update. Update only the packages owned by that manager. For Homebrew-managed trust packages, `brew upgrade ca-certificates certifi` is a possible proposal after confirming applicability; it doesn't cover every client.
3. Retest that client. A failing test after an update needs investigation, not a fabricated pass.
4. If the vendor has no working fix, explain containment and feature costs. A temporary network block doesn't patch code; keeping the app online is an owner decision.
5. If a narrowly scoped trust-store intervention is necessary, prepare it for review using current upstream fingerprints and instructions. Back up the current bundle and existing trust entries. Build and validate a candidate before replacement, preserve unrelated entries, check exact changes, retain rollback, and require administrator approval. No bulk certificate deletion or trust-settings replacement from a borrowed laptop.
6. Repeat positive, self-signed and every applicable incident-chain test after the change, plus ordinary HTTPS workflows. Record any app-specific gaps and recheck after OS updates.

No universal certificate-fix script is bundled: trust implementations, enterprise roots and current revocation coverage vary. This is a requirement to prepare a device-specific, reviewable repair when warranted, not an instruction to stop at “update your computer.” Specialist upstream scripts still need source review and explicit execution approval.

## Close unnecessary incoming access

On Mac, show **System Settings > General > Sharing > Remote Login**, explain that it controls incoming SSH, and ask whether it is needed. If disabling is approved, the owner completes any macOS authentication. Recheck the UI and the listener table. Preserve outgoing SSH configuration and keys. Review screen/file sharing separately.

On Windows, separately review Remote Desktop, OpenSSH Server and WinRM with their firewall rules and dependencies. Don't treat stopping `TermService` as a universal safe fix. Use the supported settings action for the specific service, then recheck service/listener state and normal work. [Windows guidance](windows.md).

For a local development server that only needs local clients, propose changing its configured bind address to loopback. Confirm VPN/mobile/container clients before doing so. Recheck the binding after its approved restart. Don't merely close a port by killing a process.

## Accounts, extensions and app cleanup

| Finding | Approved action | Verification and recovery |
|---|---|---|
| MFA not enabled | Owner enrolls a supported method on the official account page and privately secures recovery. | Page explicitly says enabled; registration alone is insufficient. Preserve an available recovery route. |
| Unused connected app | Name the app, exact permissions and breakage; revoke only that approved grant. | Grant disappears or the intended scope changes. Reconnection may require owner sign-in. |
| Unrecognized session | Ask about device, travel and VPN first; preserve current trusted access. | Approved session is revoked; review provider recovery if compromise is suspected. |
| Unneeded extension | Identify publisher, profile and permissions; propose disabling before removal. | It is disabled in the correct profile; normal browsing/password-manager functions still work. |
| Unwanted app | Explain background components, dependencies and local data; propose recoverable removal. | App and agreed background entries are inactive; retained data/rollback location documented. Don't empty Trash. |
| Unneeded sensitive permission | Explain what stops working before changing one permission. | UI shows the intended state and necessary accessibility/agent features still work. |
| Backup disconnected or untested | Owner reconnects destination; propose restoring a harmless file to an agreed separate folder. | File content is correct. Preserve originals; cleanup of the test copy needs scope. |

Never remove a password manager, wallet, authenticator or AI tool under a generic cleanup approval. A suspected malicious app/package needs evidence preservation and a specialist plan before removal. An update doesn't recover stolen credentials.

## Containers and credentials need their own decisions

Agree local engine/context and affected workload. Show the replacement image publisher, digest, relevant advisory, changed dependencies, backup of persistent data, downtime and rollback. Then ask before pulling, rebuilding, starting or replacing anything. Never use `docker system prune` as security cleanup. Verify the deployed digest, selected security settings, dependency result and a normal application workflow after an approved restart.

For credentials, the owner handles values. Scope which service, permission and dependent integrations need changes. Confirm a new working access/recovery path before revoking an old one where safe; for a confirmed leak, follow the provider's incident instructions from a trusted device. Don't paste keys into a report or silently rotate everything.

## Finish with evidence and gaps

Use a private table: **finding, exact approved action, before, after, ordinary workflow, rollback, remaining gap**. Say whether a running app still needs restart, a store is untested, a backup remains disconnected, an account is signed out or a vendor patch is pending. Keep the report private. Propose any later recheck; don't create reminders or monitoring without permission.
