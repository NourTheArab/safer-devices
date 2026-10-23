"""Exercise broken documentation cases without network or device access."""

import tempfile
import unittest
from pathlib import Path

from scripts.check_docs import check_document


class DocumentationTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        self.document = self.root / "README.md"

    def check(self, content):
        self.document.write_text(content, encoding="utf-8")
        return check_document(self.document, self.root)

    def test_valid_relative_link_and_fragment(self):
        (self.root / "guide.md").write_text("# Guide\n\n## Check it\n")
        self.assertEqual(self.check("# Start\n[Go](guide.md#check-it)\n"), [])

    def test_missing_file(self):
        errors = self.check("# Start\n[Go](missing.md)\n")
        self.assertTrue(any("missing target" in error for error in errors))

    def test_missing_fragment(self):
        errors = self.check("# Start\n[Go](#not-a-heading)\n")
        self.assertTrue(any("missing heading" in error for error in errors))

    def test_duplicate_headings(self):
        self.assertEqual(self.check("# Start\n## Again\n## Again\n[Go](#again-1)\n"), [])

    def test_link_outside_repository(self):
        errors = self.check("# Start\n[Go](../outside.md)\n")
        self.assertTrue(any("outside repository" in error for error in errors))

    def test_symlink_outside_repository(self):
        with tempfile.TemporaryDirectory() as outside:
            target = Path(outside) / "outside.md"
            target.write_text("# Outside\n")
            (self.root / "link.md").symlink_to(target)
            errors = self.check("# Start\n[Go](link.md)\n")
            self.assertTrue(any("outside repository" in error for error in errors))

    def test_code_examples_are_not_checked_as_links(self):
        content = "# Start\n```text\n[Example](absent.md)\n```\n`[Example](absent.md)`\n"
        self.assertEqual(self.check(content), [])

    def test_unclosed_code_block(self):
        self.assertTrue(self.check("# Start\n```text\nexample\n"))

    def test_external_links_are_not_fetched(self):
        self.assertEqual(self.check("# Start\n[Source](https://example.com/guide)\n"), [])


if __name__ == "__main__":
    unittest.main()
