#!/usr/bin/env python3
"""
Fix common issues in migrated term files.

This script fixes validation errors in the migrated term files:
- Adds missing summary fields
- Fixes invalid see_also slugs
- Truncates overly long summaries
"""

import os
import re
from pathlib import Path
from typing import Dict, List, Optional

import click
import yaml


def slugify(text: str) -> str:
    """Convert text to URL-friendly slug."""
    # Remove special characters and convert to lowercase
    slug = re.sub(r"[^\w\s-]", "", text.lower())
    # Replace spaces and multiple hyphens with single hyphens
    slug = re.sub(r"[-\s]+", "-", slug)
    # Remove leading/trailing hyphens
    return slug.strip("-")


def fix_see_also_links(see_also: List[str]) -> List[str]:
    """Fix see_also links by converting them to valid slugs."""
    fixed_links = []
    for link in see_also:
        # Convert to slug format
        fixed_link = slugify(link)
        if fixed_link and fixed_link not in fixed_links:
            fixed_links.append(fixed_link)
    return fixed_links


def generate_summary(definition: str, max_length: int = 200) -> str:
    """Generate a summary from the definition."""
    if not definition:
        return ""

    # Clean up the definition
    summary = re.sub(r"\s+", " ", definition).strip()

    # Remove markdown formatting
    summary = re.sub(r"\*\*([^*]+)\*\*", r"\1", summary)
    summary = re.sub(r"\*([^*]+)\*", r"\1", summary)

    # Truncate if too long
    if len(summary) > max_length:
        summary = summary[: max_length - 3] + "..."

    return summary


def fix_term_file(term_file: Path) -> bool:
    """Fix a single term file."""
    try:
        with open(term_file, "r", encoding="utf-8") as f:
            content = f.read()

        # Extract front-matter
        if not content.startswith("---\n"):
            return False

        end_marker = content.find("\n---\n", 4)
        if end_marker == -1:
            return False

        frontmatter_text = content[4:end_marker]
        frontmatter = yaml.safe_load(frontmatter_text)

        if not frontmatter:
            return False

        # Fix issues
        fixed = False

        # Fix missing summary
        if "summary" not in frontmatter or not frontmatter["summary"]:
            # Try to get definition from content
            definition = frontmatter.get("term", "")
            if definition:
                frontmatter["summary"] = generate_summary(definition)
                fixed = True

        # Fix overly long summary
        if "summary" in frontmatter and len(frontmatter["summary"]) > 200:
            frontmatter["summary"] = generate_summary(frontmatter["summary"])
            fixed = True

        # Fix see_also links
        if "see_also" in frontmatter:
            original_links = frontmatter["see_also"]
            fixed_links = fix_see_also_links(original_links)
            if fixed_links != original_links:
                frontmatter["see_also"] = fixed_links
                fixed = True

        # Fix aliases
        if "aliases" in frontmatter:
            original_aliases = frontmatter["aliases"]
            fixed_aliases = fix_see_also_links(original_aliases)
            if fixed_aliases != original_aliases:
                frontmatter["aliases"] = fixed_aliases
                fixed = True

        # Write back if fixed
        if fixed:
            # Reconstruct the file
            new_content = "---\n"
            new_content += yaml.dump(
                frontmatter, default_flow_style=False, allow_unicode=True
            )
            new_content += "---\n"
            new_content += content[end_marker + 5 :]  # Skip the original front-matter

            with open(term_file, "w", encoding="utf-8") as f:
                f.write(new_content)

            return True

        return False

    except Exception as e:
        print(f"Error fixing {term_file}: {e}")
        return False


def find_term_files(terms_dir: Path) -> List[Path]:
    """Find all term files in the terms directory."""
    term_files = []

    for letter_dir in terms_dir.iterdir():
        if letter_dir.is_dir():
            for term_file in letter_dir.glob("*.md"):
                term_files.append(term_file)

    return sorted(term_files)


@click.command()
@click.option(
    "--terms-dir", default="docs/terms", help="Directory containing term files"
)
@click.option(
    "--dry-run", is_flag=True, help="Show what would be fixed without making changes"
)
def main(terms_dir: str, dry_run: bool):
    """Fix common issues in term files."""
    terms_dir = Path(terms_dir)

    if not terms_dir.exists():
        print(f"Terms directory not found: {terms_dir}")
        return

    term_files = find_term_files(terms_dir)
    print(f"Found {len(term_files)} term files")

    fixed_count = 0
    error_count = 0

    for term_file in term_files:
        if dry_run:
            # Just check if file needs fixing
            try:
                with open(term_file, "r", encoding="utf-8") as f:
                    content = f.read()

                if not content.startswith("---\n"):
                    continue

                end_marker = content.find("\n---\n", 4)
                if end_marker == -1:
                    continue

                frontmatter_text = content[4:end_marker]
                frontmatter = yaml.safe_load(frontmatter_text)

                if not frontmatter:
                    continue

                needs_fixing = False
                issues = []

                # Check for missing summary
                if "summary" not in frontmatter or not frontmatter["summary"]:
                    needs_fixing = True
                    issues.append("missing summary")

                # Check for overly long summary
                if "summary" in frontmatter and len(frontmatter["summary"]) > 200:
                    needs_fixing = True
                    issues.append("summary too long")

                # Check for invalid see_also links
                if "see_also" in frontmatter:
                    for link in frontmatter["see_also"]:
                        if not re.match(r"^[a-z0-9-]+$", link):
                            needs_fixing = True
                            issues.append("invalid see_also links")
                            break

                if needs_fixing:
                    print(f"  {term_file}: {', '.join(issues)}")
                    fixed_count += 1

            except Exception as e:
                print(f"  {term_file}: Error - {e}")
                error_count += 1
        else:
            # Actually fix the file
            if fix_term_file(term_file):
                fixed_count += 1
                print(f"  Fixed {term_file}")

    if dry_run:
        print(f"\nDry run complete:")
        print(f"  Files that need fixing: {fixed_count}")
        print(f"  Files with errors: {error_count}")
    else:
        print(f"\nFix complete:")
        print(f"  Files fixed: {fixed_count}")
        print(f"  Files with errors: {error_count}")


if __name__ == "__main__":
    main()
