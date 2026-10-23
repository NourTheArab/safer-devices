"""Check only generated preview files. No network requests or device inspection."""

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1] / ".private" / "preview"


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.targets = []
        self.ids = set()
        self.language = None
        self.direction = None
        self.has_main = False

    def handle_starttag(self, tag, attributes):
        attrs = dict(attributes)
        if tag == "html":
            self.language = attrs.get("lang")
            self.direction = attrs.get("dir")
        if "id" in attrs:
            self.ids.add(attrs["id"])
        self.has_main |= tag == "main"
        if tag in {"a", "link"} and "href" in attrs:
            self.targets.append(attrs["href"])
        if tag in {"img", "script"} and "src" in attrs:
            self.targets.append(attrs["src"])


def main():
    pages = {}
    for path in ROOT.rglob("*.html"):
        page = Page()
        page.feed(path.read_text(encoding="utf-8"))
        pages[path.resolve()] = page
    errors = []
    count = 0
    if not pages:
        errors.append("Build the local preview first.")
    for path, page in pages.items():
        name = path.relative_to(ROOT)
        if not page.has_main:
            errors.append(f"{name}: missing main landmark")
        if page.language == "ar" and page.direction != "rtl":
            errors.append(f"{name}: Arabic page missing RTL")
        for target in page.targets:
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc:
                continue
            count += 1
            destination = (ROOT / unquote(parsed.path).lstrip("/")) if parsed.path.startswith("/") else (path.parent / unquote(parsed.path)) if parsed.path else path
            destination = destination.resolve()
            if not destination.is_relative_to(ROOT) or not destination.is_file():
                errors.append(f"{name}: unavailable local target")
            elif parsed.fragment and destination in pages:
                if unquote(parsed.fragment) not in pages[destination].ids:
                    errors.append(f"{name}: missing local anchor")
    if errors:
        print("\n".join(errors))
        return 1
    print(f"Checked {len(pages)} rendered pages and {count} local links/assets: passed.")
    print("Arabic page directions and main landmarks passed. No external sites were checked.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
