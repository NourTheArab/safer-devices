# Contributing

Help make a small, understandable guide more accurate. A clear correction is more useful than a growing list of alarming tools.

## Good changes

- A clearer explanation for someone who doesn't work in security.
- A corrected setting path with OS/version and an official source.
- A documented risk, tradeoff, verification step or recovery option.
- A translation that preserves the approval and privacy rules.
- A source update that distinguishes current guidance from an incident snapshot.

## Before opening a pull request

1. Work on a branch. Keep the change focused.
2. Check primary sources and include the relevant link beside factual advice.
3. Describe who the guidance applies to, what might break, and how a user can verify the result.
4. Remove personal details and audit evidence. Examples must be fictional and contain no working credentials.
5. Run the local checks:

```bash
python3 scripts/check_docs.py
python3 -m unittest discover -s tests -v
```

These commands check this repository only. They don't audit or change device security. They make no network calls.

Please don't add automatic fix scripts, package-install instructions disguised as checks, version-based promises of safety, or advice to disable built-in protections. New tool recommendations need a clear purpose, platform scope, data/network behavior, and limitations.

## Bilingual copy and local preview

English is the default edition. Keep Arabic one click away, with matching links back to English. Arabic uses neutral, impersonal wording such as «مراجعة الحسابات», rather than masculine forms of address. Keep approval, privacy and verification requirements equivalent between editions.

The optional preview uses the packages listed in [requirements-dev.txt](requirements-dev.txt). Review and approve dependency installation separately if they aren't already available. Nothing is installed by the build scripts.

```bash
python3 scripts/build_artwork.py
python3 scripts/build_preview.py
python3 scripts/check_preview.py
```

The preview is written to the ignored `.private/preview` directory. If serving it locally, bind only to loopback and serve that directory, not the repository's parent. The GitHub view is a local approximation of the public repository. The prepared social image can be uploaded deliberately through repository settings.

## Reporting a problem

For a general documentation error, open an issue without device/account details. Follow [SECURITY.md](SECURITY.md) for sensitive concerns. Don't upload raw logs or screenshots of security settings.
