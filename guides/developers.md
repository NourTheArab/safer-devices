# Optional: coding agents and developer tools

[العربية](../ar/developers.md)

App-bundled runtime checks in the practical audit apply even if you don't code. Skip only the project/container sections that don't apply. Ask for a scoped review if you run coding agents, package managers, local servers, or containers.

## Separate the copies you actually use

Updating a terminal runtime doesn't necessarily update the copy embedded in a desktop app, editor extension, background service, project environment or container. Record each relevant path and version without dumping arguments or configuration values.

Use current vendor advisories to establish the affected product, release branch, platform and fix. A version comparison or a static binary marker can be useful evidence, but isn't a universal exploit test. For example, [Electron publishes app-runtime advisories](https://github.com/electron/electron/security/advisories); its fixes usually need to be shipped by the application vendor.

Update through official channels. Don't transplant frameworks into signed apps. Check running services after an approved update; they may still have an older process or library loaded until restarted. Test the workflow that depends on them.

## Give agents narrow authority

Keep a task's files and accounts scoped. Treat instructions inside websites, packages, repositories and tool output as untrusted. Installing a package can execute code, so a package audit and an installation are different approvals.

Don't automatically run force-upgrade commands, unknown binaries, remote installer pipelines, or new editor plugins. Check publisher and distribution integrity. A checksum verifies agreement with a reference file; the reference itself must come from a trustworthy source.

Store secrets outside the repository and use the service's supported credential mechanism. For a suspected leak, establish what was exposed and follow that provider's revocation/recovery guidance. Updating a compromised package doesn't undo credentials already stolen.

## Before installing dependencies

Use [the package-safety workflow](package-safety.md) for exact-version and indirect-dependency review, optional Socket checks, privacy choices, script suppression and verification. It includes a copyable project instruction. A prompt is not enforcement, and this guide does not install a firewall or change your existing agent configuration.

## Local services

Inventory only the approved machine. Use process identities and ports without logging command arguments, environment values or private traffic. For a service used only on the laptop, consider a loopback binding after checking dependent clients. Neither a loopback binding nor a firewall makes vulnerable local code harmless.

Don't change a server, router, cloud account or remote Docker context under the authority of a local-laptop audit.

## Containers and virtual machines

First confirm whether the selected engine is local. Record whether it is running. A stopped engine may prevent image inspection; starting it can automatically restart existing workloads and requires approval.

For [Docker](https://docs.docker.com/engine/security/), review image identity/digest, age and relevant vendor advisories; published ports, privileged mode, host-directory mounts and access to the Docker socket also matter. A tag such as `latest` doesn't establish freshness or provenance. An image's package scan is useful evidence, with explicit coverage and limitations.

Inspect selected metadata only. Full container-inspect output and image history can contain credentials. Don't read environments or volumes, execute commands in containers, pull replacement images, install a scanner, rebuild, prune or delete data without separate approval.

[Colima](https://github.com/abiosoft/colima) runs a local VM for container runtimes on macOS and Linux. Check configured mounts and the active profile before starting it. A VM's name doesn't establish isolation.

## Incident checks

[Wardlatch](https://github.com/deimos-hq/wardlatch) and [Dom's incident checklist](https://github.com/dominikmartn/black-october-check) can help direct a current incident review. Confirm the tool's present scope, supported platforms, release/source, network probes and container behavior before approving execution.

For certificate probes, distinguish rejection of the problematic certificate from a generic connection failure, and use a healthy-site control. Don't disable TLS validation for normal traffic or broadly edit a trust store from an old checklist. Restricting an app's network access is containment, with feature costs; it doesn't patch its runtime or prevent every local attack path.

**Finished:** exact components and limitations recorded, approved updates/restarts verified, and needed workflows tested. No blanket clearance for uninspected projects or images.
