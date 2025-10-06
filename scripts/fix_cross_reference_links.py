#!/usr/bin/env python3
"""
Fix cross-reference links in term files to use proper .md extensions.
"""

import os
import re
from pathlib import Path

import click


def fix_links_in_file(file_path: Path, dry_run: bool = False) -> bool:
    """Fix cross-reference links in a single file."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        original_content = content

        # Fix links with trailing slashes to .md extensions
        # Pattern: [text](../path/to/term/) -> [text](../path/to/term.md)
        content = re.sub(r"(\[([^\]]+)\]\(([^)]+)/\))", r"[\2](\3.md)", content)

        # Fix links that are missing .md extension
        # Pattern: [text](../path/to/term) -> [text](../path/to/term.md)
        content = re.sub(
            r"(\[([^\]]+)\]\(([^)]+)\))(?!\.md)",
            lambda m: (
                f"[{m.group(2)}]({m.group(3)}.md)"
                if not m.group(3).endswith(".md")
                and not m.group(3).startswith("http")
                and not m.group(3).startswith("#")
                else m.group(0)
            ),
            content,
        )

        if content != original_content:
            if not dry_run:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(content)
            return True

        return False

    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False


@click.command()
@click.option(
    "--terms-dir", default="docs/terms", help="Directory containing term files"
)
@click.option("--dry-run", is_flag=True, help="Run without making any changes")
def main(terms_dir: str, dry_run: bool):
    """Fix cross-reference links in term files."""
    terms_path = Path(terms_dir)
    if not terms_path.exists():
        print(f"Error: Terms directory not found at {terms_path}")
        return

    print(f"Fixing cross-reference links in {terms_path}")
    if dry_run:
        print("DRY RUN MODE - No changes will be made")

    fixed_count = 0
    total_files = 0

    for letter_dir in terms_path.iterdir():
        if letter_dir.is_dir():
            for term_file in letter_dir.glob("*.md"):
                total_files += 1
                if fix_links_in_file(term_file, dry_run):
                    fixed_count += 1
                    print(f"Fixed links in {term_file.name}")

    print(f"\nResults:")
    print(f"Files processed: {total_files}")
    print(f"Files fixed: {fixed_count}")


if __name__ == "__main__":
    main()
