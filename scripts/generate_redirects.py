#!/usr/bin/env python3
"""
Generate redirect pages for aliases to main terms.
"""

from pathlib import Path
from typing import Any, Dict, List

import click
import yaml


def load_aliases(aliases_file: Path) -> Dict[str, List[str]]:
    """Load aliases from YAML file."""
    try:
        with open(aliases_file, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
        return data.get("aliases", {})
    except Exception as e:
        print(f"Error loading aliases: {e}")
        return {}


def create_redirect_page(
    alias_slug: str, target_slug: str, alias_name: str, target_name: str
) -> str:
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


def generate_redirects(
    aliases_file: Path, output_dir: Path, dry_run: bool = False
) -> None:
    """Generate redirect pages for all aliases."""
    aliases = load_aliases(aliases_file)

    if not aliases:
        print("No aliases found to process.")
        return

    print(f"Generating redirects for {len(aliases)} terms...")

    created_count = 0

    for main_term, alias_list in aliases.items():
        # Create redirect directory for main term
        main_term_dir = output_dir / main_term
        if not dry_run:
            main_term_dir.mkdir(parents=True, exist_ok=True)

        for alias in alias_list:
            # Convert alias to slug format
            alias_slug = (
                alias.lower().replace(" ", "-").replace("&", "and").replace("/", "-")
            )
            alias_slug = "".join(c for c in alias_slug if c.isalnum() or c in "-")

            # Create redirect file
            redirect_file = main_term_dir / f"{alias_slug}.md"
            redirect_content = create_redirect_page(
                alias_slug, main_term, alias, main_term.replace("-", " ").title()
            )

            if not dry_run:
                with open(redirect_file, "w", encoding="utf-8") as f:
                    f.write(redirect_content)

            created_count += 1
            print(f"Created redirect: {alias} -> {main_term}")

    print(f"\nGenerated {created_count} redirect pages")


@click.command()
@click.option(
    "--aliases-file", default="docs/data/aliases.yml", help="Path to aliases YAML file"
)
@click.option(
    "--output-dir", default="docs/redirects", help="Output directory for redirect pages"
)
@click.option(
    "--dry-run", is_flag=True, help="Show what would be created without making changes"
)
def main(aliases_file: str, output_dir: str, dry_run: bool):
    """Generate redirect pages for aliases."""
    aliases_path = Path(aliases_file)
    output_path = Path(output_dir)

    if not aliases_path.exists():
        print(f"Error: Aliases file not found at {aliases_path}")
        return

    if dry_run:
        print("DRY RUN MODE - No files will be created")

    generate_redirects(aliases_path, output_path, dry_run)


if __name__ == "__main__":
    main()
