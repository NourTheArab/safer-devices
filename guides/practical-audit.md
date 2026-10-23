# Practical audit: start here with your agent

[العربية](../ar/practical-audit.md) · [Main guide](../README.md)

This is the working checklist, not just reading material. It combines device checks, incident-specific tests and follow-through. Reviewed **23 October 2026**. Run only applicable, authorized checks. Never copy a fix from someone else's laptop without checking this device.

## Establish access and scope once

Read [the agent contract](../prompts/AGENT-AUDIT.md). Ask one short set of questions: which device and OS, personal or managed, which browser profiles/accounts, any suspected incident, backup availability, and apps that must stay untouched. Keep passwords, wallets and existing AI apps protected by default. Updating an AI app also needs separate approval.

Declare actual capabilities: local shell, settings UI, browser, network probes, administrator access. A remote sandbox isn't the user's laptop. A phone screenshot doesn't prove which device is in scope. If local access is missing, use [the chat-only walkthrough](chat-only.md) immediately; use [the iPad checklist](ipad.md) for iPad. Don't keep asking the user to grant access the product doesn't support.

For a suspected active compromise or targeted attack, read [getting help](getting-help.md) before cleanup. Preserve evidence; don't begin mass upgrades or removal.

## Complete the coverage table

Give every row a result: **verified**, **needs attention**, **unknown**, or **not applicable**, with evidence and the exact scope. Verified means the stated check passed, not that the whole item is invulnerable. Missing access stays unknown. An item is not applicable only with a stated reason. Continue other authorized checks when one is blocked.

| Check | Action and evidence | Follow-through |
|---|---|---|
| OS and app updates | Record OS/build and installed versions of browsers, messaging apps, meeting tools, VPN and AI apps. Check official security releases and whether a restart is pending. | Update the affected installation, restart with approval, re-read its version and test use. |
| Encryption and lock | Confirm encryption state, authentication after sleep, automatic login and privately available recovery. | Propose settings individually; never display a recovery key. |
| Firewall and remote access | Check incoming firewall, SSH/Remote Login, desktop/screen sharing and file sharing. | Ask what is needed before disabling a service. |
| Listening services | Identify TCP and UDP listeners, owner process and binding. Separate loopback, all interfaces and actual reachability. | Review necessity, software updates and binding; don't kill unknown processes. |
| Backup and restore | Record latest completed backup, connected destination and whether a harmless restore test succeeded. | A restore writes a file and needs approval. Disconnected or untested stays unknown. |
| Browser profiles | Review each used profile, browser version, extensions, publisher, broad permissions and need. | Propose disabling one extension with a re-enable plan; protect password managers and wallets. |
| Accounts | Offer Apple, Google, GitHub, Microsoft and Proton, plus others the owner names. Confirm MFA enabled, recovery availability, sessions and connected-app scopes. | The owner handles sign-in and secrets. Recognized foreign locations alone aren't suspicious. Revoke only an approved grant/session. |
| Installed apps | Inventory versions and publishers, unused software and unsupported releases. | Explain data/dependency effects; move an approved app to recoverable Trash first. |
| Sensitive permissions | Review accessibility, screen capture, full-disk access, location, camera and microphone. | Preserve necessary accessibility and managed controls. |
| Startup and persistence | Review Login Items/background apps or Startup Apps/Task Scheduler. Match entries to known software and publisher. | Unfamiliar isn't malicious. Don't delete tasks or unload services automatically. |
| Bundled runtimes | Check applicable app copies of Electron/Node/Bun/Python/Java/Go-built tools, even when the owner doesn't code. | Terminal updates don't patch an app's embedded copy. Use its vendor's update. |
| Certificate trust | Follow [incident checks](incident-checks.md) for affected clients and controls. | Record each client/store separately. Recheck after approved OS/runtime updates. |
| Projects and containers | Ask whether projects, local servers or containers are used. If yes, agree folders and a local engine before inspection. | No VM starts, container exec, remote context access, image pulls, rebuilds or pruning without approval. |
| Dependency installation policy | For agreed development projects, use [package safety](package-safety.md): exact versions, indirect dependencies, scripts, provenance and scanner data disclosure. | No installs or external scans by default. Separate setup/install approvals; warnings, unknowns and cache gaps pause the proposed operation. |
| Tool and agent access | Review enabled plugins/MCP servers, network/tools/file scope and permission settings through safe metadata. | No reading credential values or config dumps. Propose narrower access with its feature cost. |
| Exposure and incident evidence | Match applicable current advisories and provenance records; investigate unsupported or affected software. | A vulnerable version isn't proof of exploitation. Confirmed malicious-package exposure needs a credential/recovery plan, not just an update. |

## Mac: local read-only checks

Commands below are individual checks for a local agent, not a script to paste wholesale. Use trusted OS tools. No `sudo` in the initial pass; permission errors are coverage limits. Don't print raw paths, device names or addresses in a public report. Inspect private output locally and summarize only relevant states.

```bash
/usr/bin/sw_vers -productVersion
/usr/bin/sw_vers -buildVersion
/usr/bin/fdesetup status
/usr/libexec/ApplicationFirewall/socketfilterfw --getglobalstate
/usr/bin/csrutil status
/usr/sbin/spctl --status
```

Expect FileVault enabled, the incoming firewall enabled where appropriate, SIP enabled and assessments enabled. Managed exceptions require IT review. Cross-check unexpected states in System Settings or the supported recovery UI; restricted shells can mislead.

```bash
/usr/sbin/lsof -nP -iTCP -sTCP:LISTEN
/usr/sbin/lsof -nP -iUDP
```

UDP output describes open sockets, not necessarily listening servers. Record program identity, PID, local port and binding without process arguments or peer histories. `127.0.0.1`/`::1` are loopback; `*`, `0.0.0.0` and `::` include broader interfaces. Router, VPN and firewall rules determine reachability. Don't scan the LAN or internet. Check **System Settings > General > Sharing** for Remote Login and sharing states; TCP 22 alone isn't proof of exposure. [Apple Remote Login](https://support.apple.com/guide/mac-help/allow-a-remote-computer-to-access-your-mac-mchlp1066/mac).

```bash
/usr/bin/tmutil latestbackup
```

This can reveal a private destination path; summarize the date and success only. A missing/mount error doesn't prove backups were deleted. Confirm in Time Machine. Don't mount disks automatically. For lock timing, permissions, Login Items and background items, use System Settings rather than dumping preference databases. [Mac guidance](mac.md) links the vendor instructions.

For one selected app, replace the example with its verified location, keeping quotes:

```bash
/usr/bin/plutil -extract CFBundleShortVersionString raw -o - '/Applications/Example.app/Contents/Info.plist'
/usr/bin/codesign --verify --deep --strict '/Applications/Example.app'
/usr/sbin/spctl --assess --type execute '/Applications/Example.app'
```

Don't execute the app to inventory it. A valid signature establishes neither freshness nor harmlessness. Retain publisher/version metadata privately. Read-only signature checks can fail for legitimate reasons; investigate before removal.

## Windows: local read-only PowerShell

Use a normal local PowerShell session first. Select fields to avoid hardware identifiers and command lines. Missing cmdlets or denied access stay unknown. These aren't Linux-shell commands.

```powershell
Get-CimInstance Win32_OperatingSystem | Select-Object Caption,Version,BuildNumber
Get-MpComputerStatus | Select-Object AMRunningMode,AntivirusEnabled,RealTimeProtectionEnabled,AntivirusSignatureLastUpdated
Get-NetFirewallProfile | Select-Object Name,Enabled
Get-BitLockerVolume | Select-Object MountPoint,VolumeStatus,ProtectionStatus
Get-Service sshd,TermService,WinRM -ErrorAction SilentlyContinue | Select-Object Name,Status,StartType
Get-NetTCPConnection -State Listen | Select-Object LocalAddress,LocalPort,OwningProcess
Get-NetUDPEndpoint | Select-Object LocalAddress,LocalPort,OwningProcess
```

Resolve a selected PID without command-line disclosure:

```powershell
Get-Process -Id 1234 | Select-Object Id,ProcessName
```

Replace the example PID. A running service isn't proof it accepts remote connections. Review **Settings > System > Remote Desktop**, sharing, firewall rules and the active network profile. Defender may be passive under another managed antivirus; check Windows Security before calling that a failure. The encryption query may need elevation: ask before rerunning it as administrator, or use Settings. Never select key-protector fields.

For one selected app executable:

```powershell
Get-AuthenticodeSignature -LiteralPath 'C:\Program Files\Example\Example.exe' | Select-Object Status
(Get-Item -LiteralPath 'C:\Program Files\Example\Example.exe').VersionInfo | Select-Object ProductVersion,FileVersion
```

Check updates, restart state, startup apps, scheduled tasks and privacy permissions in the normal UI. Don't dump task action arguments. A `Get-HotFix` list alone isn't an up-to-date verdict. Sources: [Defender status](https://learn.microsoft.com/en-us/powershell/module/defender/get-mpcomputerstatus), [TCP metadata](https://learn.microsoft.com/en-us/powershell/module/nettcpip/get-nettcpconnection), [Windows guidance](windows.md).

## Runtimes and projects: inventory before execution

List locations first; don't run an unfamiliar binary to discover its version. Version managers, old virtual environments, apps and running services can use different copies. On Unix, location lookup doesn't execute these programs:

```bash
command -v node bun python3 uv java go php ruby tailscale
```

After provenance is established, query the exact approved path using its documented version flag. For Python use `-I -S --version`; for Java use `-version`; for Go use `version`. Version-manager shims can launch initialization code, so resolve their target first. Don't invoke `npx`, `npm install`, `pip`, `uv run` or a project task as an inventory shortcut.

On macOS, `/usr/libexec/java_home -V` lists registered JDKs. Also inspect the agreed IDE/app bundles for private JDKs. Record only versions and coverage, not user paths. For a chosen trusted process, `ps -p 1234 -o pid=,comm=,lstart=` identifies executable and start time without command arguments. Compare the running executable and mapped library with the updated installation; a package update alone doesn't restart a process.

For an approved app, inspect metadata and filenames under its bundle for `Electron Framework.framework`, `node`, `bun`, Python or a JDK. Read a version resource where available. Don't launch helpers, recursively print package/config files or transplant frameworks. Missing embedded-version evidence stays unknown.

For an agreed project, inspect only package/version metadata and lockfile entries relevant to current advisories. Include PHP, Next.js/sharp, Storybook, Ruby/self-managed GitLab where present. Don't open `.env`, package credentials or git remotes. Use [incident checks](incident-checks.md) and [developer guidance](developers.md).

For containers, first inspect the selected context endpoint privately and confirm it is a local engine. Don't print it. A stopped engine stays stopped. Then, only within that scope:

```bash
docker ps --format '{{.ID}}\t{{.Image}}\t{{.Ports}}'
docker image ls --digests --format '{{.ID}}\t{{.Repository}}:{{.Tag}}\t{{.Digest}}'
docker inspect --format '{{.HostConfig.Privileged}} {{.HostConfig.NetworkMode}} {{json .HostConfig.PortBindings}}' CONTAINER_ID
```

Replace the chosen ID. Inspect mounts only as private metadata: report broad host access or Docker-socket access without exposing paths. Don't dump full inspect/history/environment/labels. Versions and digests need comparison with the publisher's advisory; a tag is insufficient. Image package scanning, rebuilding and `docker exec` require separate approval. [Docker security](https://docs.docker.com/engine/security/).

## From findings to verified repairs

Use [the repair playbook](repairs.md). Prioritize known exposure and unsupported software, then unnecessary access and recovery gaps. Don't let a blocked account or permission check stall the rest.

End with a coverage table plus **changed, verified, unknown, deferred, blocked, rollback**. Name pending reboots, restart-dependent services, disconnected backups and apps awaiting a vendor fix. Schedule nothing and revoke nothing without approval. Use [the acceptance scenarios](agent-verification.md) to check the agent's behavior, not just its wording.
