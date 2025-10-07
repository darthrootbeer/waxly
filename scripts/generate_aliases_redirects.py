#!/usr/bin/env python3
"""
Generate redirects from individual term files' aliases field.
This script reads all term files, extracts their aliases field,
and creates redirect pages for each alias.
"""

import re
from pathlib import Path
from typing import Any, Dict, List, Set

import click
import yaml


def slugify(text: str) -> str:
    """Convert text to URL-friendly slug."""
    # Convert to lowercase and replace spaces/special chars with hyphens
    slug = text.lower()
    slug = re.sub(
        r"[^\w\s-]", "", slug
    )  # Remove special chars except spaces and hyphens
    slug = re.sub(
        r"[-\s]+", "-", slug
    )  # Replace spaces and multiple hyphens with single hyphen
    return slug.strip("-")


def load_term_frontmatter(term_file: Path) -> Dict[str, Any]:
    """Load YAML frontmatter from a term file."""
    try:
        with open(term_file, "r", encoding="utf-8") as f:
            content = f.read()

        # Extract frontmatter between --- markers
        if content.startswith("---"):
            parts = content.split("---", 2)
            if len(parts) >= 3:
                frontmatter_text = parts[1].strip()
                return yaml.safe_load(frontmatter_text) or {}
    except Exception as e:
        print(f"Error loading {term_file}: {e}")

    return {}


def create_redirect_page(alias_name: str, target_slug: str, target_name: str) -> str:
    """Create a redirect page for an alias."""
    # Determine the target path based on the first letter
    first_letter = target_slug[0].lower()
    target_path = f"../terms/{first_letter}/{target_slug}/"

    return f"""---
title: {alias_name}
redirect: {target_path}
template: redirect.html
---

# {alias_name}

This term redirects to [{target_name}]({target_path}).

*This is an alias for the main term. Click the link above to view the full definition.*
"""


def process_term_files(
    terms_dir: Path, redirects_dir: Path, dry_run: bool = False
) -> Dict[str, List[str]]:
    """Process all term files and generate redirects from aliases field."""
    aliases_data = {}
    processed_count = 0
    redirect_count = 0

    # Get all markdown files in terms directory
    term_files = list(terms_dir.rglob("*.md"))

    print(f"Processing {len(term_files)} term files...")

    for term_file in term_files:
        # Skip if it's in a redirects directory
        if "redirects" in str(term_file):
            continue

        frontmatter = load_term_frontmatter(term_file)

        if not frontmatter:
            continue

        term_name = frontmatter.get("term", "")
        term_slug = frontmatter.get("slug", "")

        if not term_slug:
            continue

        # Get aliases from frontmatter
        aliases = frontmatter.get("aliases", [])
        if isinstance(aliases, str):
            aliases = [aliases]

        # Get aka field as well
        aka = frontmatter.get("aka", [])
        if isinstance(aka, str):
            aka = [aka]

        # Combine aliases and aka
        all_aliases = aliases + aka

        if all_aliases:
            # Store for aliases.yml generation
            aliases_data[term_slug] = [alias for alias in all_aliases if alias]

            # Create redirect directory for this term
            term_redirect_dir = redirects_dir / term_slug
            if not dry_run:
                term_redirect_dir.mkdir(parents=True, exist_ok=True)

            # Create redirect files for each alias
            for alias in all_aliases:
                if not alias:
                    continue

                alias_slug = slugify(alias)

                # Skip if alias slug is the same as term slug
                if alias_slug == term_slug:
                    continue

                redirect_file = term_redirect_dir / f"{alias_slug}.md"
                redirect_content = create_redirect_page(alias, term_slug, term_name)

                if not dry_run:
                    with open(redirect_file, "w", encoding="utf-8") as f:
                        f.write(redirect_content)

                redirect_count += 1
                print(f"Created redirect: {alias} -> {term_slug}")

        processed_count += 1

    print(f"\nProcessed {processed_count} term files")
    print(f"Generated {redirect_count} redirect pages")

    return aliases_data


def update_aliases_yml(
    aliases_data: Dict[str, List[str]], aliases_file: Path, dry_run: bool = False
) -> None:
    """Update the aliases.yml file with data from term files."""
    if not aliases_data:
        print("No aliases data to update")
        return

    # Load existing aliases.yml
    existing_data = {}
    if aliases_file.exists():
        try:
            with open(aliases_file, "r", encoding="utf-8") as f:
                existing_data = yaml.safe_load(f) or {}
        except Exception as e:
            print(f"Error loading existing aliases.yml: {e}")

    # Merge with existing data
    existing_aliases = existing_data.get("aliases", {})

    # Add new aliases, preserving existing ones
    for term_slug, aliases in aliases_data.items():
        if term_slug in existing_aliases:
            # Merge with existing aliases
            existing_set = set(existing_aliases[term_slug])
            new_set = set(aliases)
            existing_aliases[term_slug] = sorted(list(existing_set.union(new_set)))
        else:
            existing_aliases[term_slug] = sorted(aliases)

    # Write updated aliases.yml
    updated_data = {"aliases": existing_aliases}

    if not dry_run:
        with open(aliases_file, "w", encoding="utf-8") as f:
            yaml.dump(updated_data, f, default_flow_style=False, sort_keys=True)

    print(f"Updated aliases.yml with {len(existing_aliases)} terms")


@click.command()
@click.option(
    "--terms-dir", default="docs/terms", help="Directory containing term files"
)
@click.option(
    "--redirects-dir",
    default="docs/redirects",
    help="Output directory for redirect pages",
)
@click.option(
    "--aliases-file", default="docs/data/aliases.yml", help="Path to aliases.yml file"
)
@click.option(
    "--dry-run", is_flag=True, help="Show what would be created without making changes"
)
def main(terms_dir: str, redirects_dir: str, aliases_file: str, dry_run: bool):
    """Generate redirects from term files' aliases field."""
    terms_path = Path(terms_dir)
    redirects_path = Path(redirects_dir)
    aliases_path = Path(aliases_file)

    if not terms_path.exists():
        print(f"Error: Terms directory not found at {terms_path}")
        return

    if dry_run:
        print("DRY RUN MODE - No files will be created")

    # Process term files and generate redirects
    aliases_data = process_term_files(terms_path, redirects_path, dry_run)

    # Update aliases.yml file
    update_aliases_yml(aliases_data, aliases_path, dry_run)

    print("\nAliases → Redirects system setup complete!")


if __name__ == "__main__":
    main()
