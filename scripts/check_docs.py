"""Offline checks for this repo's simple Markdown subset, not a security audit.

Checks titles, fenced blocks and inline local links/heading anchors. External
links and reference-style links aren't validated. Uses only the Python stdlib.
"""

import re
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
IGNORED = {".git", ".private", ".venv", "__pycache__", "local-reports"}
LINK = re.compile(r"!?\[[^\]\n]*\]\(([^)\n]+)\)")


def prose_lines(content):
    """Preserve line numbers while excluding fenced and inline code examples."""
    fence = None
    result = []
    for number, line in enumerate(content.splitlines(), 1):
        marker = re.match(r"^\s{0,3}(`{3,}|~{3,})", line)
        if marker:
            value = marker.group(1)
            if fence is None:
                fence = value
            elif value[0] == fence[0] and len(value) >= len(fence):
                fence = None
            continue
        if fence is None:
            result.append((number, re.sub(r"`[^`]*`", "", line)))
    return result, fence is not None


def heading_ids(content):
    seen = set()
    for _, line in prose_lines(content)[0]:
        heading = re.match(r"^#{1,6}\s+(.+?)\s*#*\s*$", line)
        if not heading:
            continue
        base = re.sub(r"[^\w\- ]", "", heading.group(1).lower()).replace(" ", "-")
        identifier = base
        suffix = 0
        while identifier in seen:
            suffix += 1
            identifier = f"{base}-{suffix}"
        seen.add(identifier)
    return seen


def check_document(path, root):
    root = root.resolve()
    path = path.resolve()
    name = path.relative_to(root)
    content = path.read_text(encoding="utf-8")
    lines, unclosed = prose_lines(content)
    errors = []
    if not any(re.match(r"^#\s+\S", line) for _, line in lines):
        errors.append(f"{name}: missing document title")
    if unclosed:
        errors.append(f"{name}: unclosed fenced code block")
    for number, line in lines:
        for match in LINK.finditer(line):
            destination = match.group(1).strip().strip("<>")
            parsed = urlsplit(destination)
            if parsed.scheme or parsed.netloc:
                continue
            target = (path.parent / unquote(parsed.path)).resolve() if parsed.path else path
            if not target.is_relative_to(root):
                errors.append(f"{name}:{number}: link outside repository")
            elif not target.is_file():
                errors.append(f"{name}:{number}: missing target")
            elif parsed.fragment and target.suffix == ".md":
                headings = heading_ids(target.read_text(encoding="utf-8"))
                if unquote(parsed.fragment) not in headings:
                    errors.append(f"{name}:{number}: missing heading")
    return errors


def main():
    paths = sorted(path for path in ROOT.rglob("*.md") if not IGNORED.intersection(path.relative_to(ROOT).parts))
    errors = []
    for path in paths:
        try:
            errors.extend(check_document(path, ROOT))
        except (OSError, UnicodeError, ValueError):
            errors.append(f"{path.relative_to(ROOT)}: unable to check document")
    if errors:
        print("\n".join(errors))
        return 1
    print(f"Checked {len(paths)} Markdown documents: local links, titles and fenced blocks passed.")
    print("No external sites or device settings were checked.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
