#!/usr/bin/env python3
"""
Generate Discogs genre/style reference mappings.
"""

import json
from pathlib import Path
from typing import Any, Dict, List, Set

import click
import yaml


def load_discogs_taxonomy(taxonomy_file: Path) -> Dict[str, Dict[str, List[str]]]:
    """Load the Discogs taxonomy from YAML file."""
    try:
        with open(taxonomy_file, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)
    except Exception as e:
        print(f"Error loading taxonomy: {e}")
        return {}


def create_discogs_urls(genres: Dict[str, List[str]]) -> Dict[str, Dict[str, Any]]:
    """Create Discogs URL mappings for genres and styles."""
    discogs_refs = {}

    for genre, styles in genres.items():
        # Create genre URL
        genre_slug = genre.lower().replace(" ", "-").replace("&", "and")
        genre_url = f"https://www.discogs.com/genre/{genre_slug}"

        # Create genre reference
        discogs_refs[genre] = {
            "type": "genre",
            "name": genre,
            "slug": genre_slug,
            "url": genre_url,
            "styles": [],
        }

        # Create style references
        for style in styles:
            style_slug = style.lower().replace(" ", "-").replace("&", "and")
            style_url = f"https://www.discogs.com/style/{style_slug}"

            discogs_refs[style] = {
                "type": "style",
                "name": style,
                "slug": style_slug,
                "url": style_url,
                "parent_genre": genre,
            }

            # Add style to genre's styles list
            discogs_refs[genre]["styles"].append(
                {"name": style, "slug": style_slug, "url": style_url}
            )

    return discogs_refs


def generate_discogs_pages(
    discogs_refs: Dict[str, Dict[str, Any]], output_dir: Path
) -> None:
    """Generate individual pages for each genre and style."""
    genres_dir = output_dir / "genres"
    styles_dir = output_dir / "styles"

    genres_dir.mkdir(parents=True, exist_ok=True)
    styles_dir.mkdir(parents=True, exist_ok=True)

    for name, ref_data in discogs_refs.items():
        if ref_data["type"] == "genre":
            # Generate genre page
            genre_file = genres_dir / f"{ref_data['slug']}.md"
            content = f"""---
title: {name}
type: genre
discogs_url: {ref_data['url']}
styles: {len(ref_data['styles'])}
---

# {name}

**Genre** | [View on Discogs]({ref_data['url']})

{name} is one of the official genres in the Discogs music taxonomy.

## Styles

This genre includes the following styles:

"""
            for style in ref_data["styles"]:
                content += f"- [{style['name']}](../styles/{style['slug']}.md)\n"

            content += f"""
## Related Terms

Browse terms in the Vinyl Lexicon related to {name}:

- [Browse by Genre](../tags/genres.md)

---

*This page references the [Discogs]({ref_data['url']}) music database as an authoritative source for genre classification.*
"""

            with open(genre_file, "w", encoding="utf-8") as f:
                f.write(content)

        elif ref_data["type"] == "style":
            # Generate style page
            style_file = styles_dir / f"{ref_data['slug']}.md"
            content = f"""---
title: {name}
type: style
parent_genre: {ref_data['parent_genre']}
discogs_url: {ref_data['url']}
---

# {name}

**Style** | Parent Genre: [{ref_data['parent_genre']}](../genres/{discogs_refs[ref_data['parent_genre']]['slug']}.md) | [View on Discogs]({ref_data['url']})

{name} is a style within the {ref_data['parent_genre']} genre according to the Discogs music taxonomy.

## Related Terms

Browse terms in the Vinyl Lexicon related to {name}:

- [Browse by Genre](../tags/genres.md)

---

*This page references the [Discogs]({ref_data['url']}) music database as an authoritative source for style classification.*
"""

            with open(style_file, "w", encoding="utf-8") as f:
                f.write(content)


def generate_discogs_references(taxonomy_file: Path, output_dir: Path) -> None:
    """Generate Discogs reference system."""
    print("Loading Discogs taxonomy...")
    taxonomy = load_discogs_taxonomy(taxonomy_file)

    if not taxonomy:
        print("No taxonomy data found.")
        return

    genres = taxonomy.get("genres", {})
    print(f"Found {len(genres)} genres with styles")

    print("Creating Discogs URL mappings...")
    discogs_refs = create_discogs_urls(genres)

    print("Generating reference pages...")
    generate_discogs_pages(discogs_refs, output_dir)

    # Save reference data as JSON
    refs_file = output_dir / "discogs_references.json"
    with open(refs_file, "w", encoding="utf-8") as f:
        json.dump(discogs_refs, f, indent=2, ensure_ascii=False)

    print(f"Generated {len(discogs_refs)} Discogs references")
    print(f"Created genre and style pages in {output_dir}")
    print(f"Saved reference data to {refs_file}")


@click.command()
@click.option(
    "--taxonomy-file",
    default="docs/data/taxonomy.yml",
    help="Path to taxonomy YAML file",
)
@click.option(
    "--output-dir",
    default="docs/discogs",
    help="Output directory for Discogs references",
)
def main(taxonomy_file: str, output_dir: str):
    """Generate Discogs genre/style reference system."""
    taxonomy_path = Path(taxonomy_file)
    output_path = Path(output_dir)

    if not taxonomy_path.exists():
        print(f"Error: Taxonomy file not found at {taxonomy_path}")
        return

    generate_discogs_references(taxonomy_path, output_path)


if __name__ == "__main__":
    main()
