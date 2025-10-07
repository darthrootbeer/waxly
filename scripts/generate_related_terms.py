#!/usr/bin/env python3
"""
Generate related terms data for sidebar display.
"""

import json
from collections import defaultdict
from pathlib import Path
from typing import Any, Dict, List, Set

import click
import yaml


def load_term_data(terms_dir: Path) -> Dict[str, Dict[str, Any]]:
    """Load all term data from markdown files."""
    terms = {}

    for letter_dir in terms_dir.iterdir():
        if letter_dir.is_dir():
            for term_file in letter_dir.glob("*.md"):
                try:
                    with open(term_file, "r", encoding="utf-8") as f:
                        content = f.read()

                    # Extract front matter
                    if content.startswith("---"):
                        parts = content.split("---", 2)
                        if len(parts) >= 3:
                            front_matter = yaml.safe_load(parts[1])
                            if front_matter and "slug" in front_matter:
                                slug = front_matter["slug"]
                                terms[slug] = {
                                    "name": front_matter.get(
                                        "title", slug.replace("-", " ").title()
                                    ),
                                    "slug": slug,
                                    "tags": front_matter.get("tags", []),
                                    "genres": front_matter.get("genres", []),
                                    "related_terms": front_matter.get(
                                        "related_terms", []
                                    ),
                                    "path": f"terms/{letter_dir.name}/{term_file.stem}",
                                }
                except Exception as e:
                    print(f"Error processing {term_file}: {e}")

    return terms


def find_related_terms(
    term_slug: str, term_data: Dict[str, Any], all_terms: Dict[str, Dict[str, Any]]
) -> List[Dict[str, str]]:
    """Find related terms based on tags, genres, and manual relationships."""
    related = set()
    current_term = all_terms.get(term_slug, {})

    # Get current term's tags and genres
    current_tags = set(current_term.get("tags", []))
    current_genres = set(current_term.get("genres", []))
    manual_related = current_term.get("related_terms", [])

    # Add manual relationships
    for related_slug in manual_related:
        if related_slug in all_terms:
            related.add(related_slug)

    # Find terms with overlapping tags
    for other_slug, other_term in all_terms.items():
        if other_slug == term_slug:
            continue

        other_tags = set(other_term.get("tags", []))
        other_genres = set(other_term.get("genres", []))

        # Check for tag overlap
        tag_overlap = current_tags.intersection(other_tags)
        genre_overlap = current_genres.intersection(other_genres)

        # Add if there's significant overlap
        if len(tag_overlap) >= 2 or len(genre_overlap) >= 1:
            related.add(other_slug)

    # Convert to list with names and limit to 5 most relevant
    related_list = []
    for slug in list(related)[:5]:
        if slug in all_terms:
            related_list.append(
                {
                    "name": all_terms[slug]["name"],
                    "slug": slug,
                    "path": all_terms[slug]["path"],
                }
            )

    return related_list


def generate_related_terms_data(terms_dir: Path, output_file: Path) -> None:
    """Generate related terms data for all terms."""
    print("Loading term data...")
    all_terms = load_term_data(terms_dir)
    print(f"Loaded {len(all_terms)} terms")

    print("Generating related terms...")
    related_data = {}

    for term_slug, term_info in all_terms.items():
        related = find_related_terms(term_slug, term_info, all_terms)
        if related:
            related_data[term_slug] = {"name": term_info["name"], "related": related}

    print(f"Generated related terms for {len(related_data)} terms")

    # Save as JSON
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(related_data, f, indent=2, ensure_ascii=False)

    print(f"Saved related terms data to {output_file}")


@click.command()
@click.option(
    "--terms-dir", default="docs/terms", help="Directory containing term files"
)
@click.option(
    "--output-file",
    default="docs/data/related_terms.json",
    help="Output file for related terms data",
)
def main(terms_dir: str, output_file: str):
    """Generate related terms data for sidebar display."""
    terms_path = Path(terms_dir)
    output_path = Path(output_file)

    if not terms_path.exists():
        print(f"Error: Terms directory not found at {terms_path}")
        return

    # Ensure output directory exists
    output_path.parent.mkdir(parents=True, exist_ok=True)

    generate_related_terms_data(terms_path, output_path)


if __name__ == "__main__":
    main()
