#!/usr/bin/env python3
"""
Generate individual lexicon entries for Discogs genres and styles.
This creates separate term files for each genre and style rather than using them as fields.
"""

import re
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List

import yaml


def slugify(text: str) -> str:
    """Convert text to URL-friendly slug."""
    slug = text.lower()
    slug = re.sub(
        r"[^\w\s-]", "", slug
    )  # Remove special chars except spaces and hyphens
    slug = re.sub(
        r"[-\s]+", "-", slug
    )  # Replace spaces and multiple hyphens with single hyphen
    return slug.strip("-")


def create_genre_entry(genre_name: str, styles: List[str] = None) -> Dict[str, Any]:
    """Create a genre entry with proper frontmatter."""
    slug = slugify(genre_name)
    now = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%fZ")

    entry = {
        "term": genre_name,
        "slug": slug,
        "pos": "noun",
        "summary": f"**{genre_name}** - A broad musical genre classification from the Discogs taxonomy.",
        "created": now,
        "updated": now,
        "tags": ["genre", "discogs", "classification"],
        "domains": ["cultural"],
        "regions": ["global"],
        "eras": ["modern"],
        "popularity": 8,
        "complexity": "beginner",
        "status": "active",
        "context": "formal",
        "verification": "verified",
        "equipment_association": [],
        "genres": ["all"],
        "sources": [{"label": "Discogs", "url": "https://www.discogs.com/"}],
        "discussion": "This is an official genre classification from Discogs, the world's largest music database.",
    }

    if styles:
        entry["see_also"] = [
            slugify(style) for style in styles[:5]
        ]  # Limit to first 5 styles

    return entry


def create_style_entry(style_name: str, parent_genre: str) -> Dict[str, Any]:
    """Create a style entry with proper frontmatter."""
    slug = slugify(style_name)
    now = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%fZ")

    entry = {
        "term": style_name,
        "slug": slug,
        "pos": "noun",
        "summary": f"**{style_name}** - A musical style within the {parent_genre} genre, classified according to Discogs taxonomy.",
        "created": now,
        "updated": now,
        "tags": ["style", "discogs", "classification"],
        "domains": ["cultural"],
        "regions": ["global"],
        "eras": ["modern"],
        "popularity": 6,
        "complexity": "intermediate",
        "status": "active",
        "context": "formal",
        "verification": "verified",
        "equipment_association": [],
        "genres": ["all"],
        "sources": [{"label": "Discogs", "url": "https://www.discogs.com/"}],
        "relationships": {"parent_concept": slugify(parent_genre)},
        "discussion": f"This is an official style classification from Discogs within the {parent_genre} genre.",
    }

    return entry


def write_term_file(entry: Dict[str, Any], output_dir: Path) -> None:
    """Write a term entry to a markdown file."""
    # Determine directory based on first letter
    first_letter = entry["slug"][0].lower()
    term_dir = output_dir / first_letter
    term_dir.mkdir(parents=True, exist_ok=True)

    term_file = term_dir / f"{entry['slug']}.md"

    # Create markdown content
    content = "---\n"
    content += yaml.dump(entry, default_flow_style=False, sort_keys=False)
    content += "---\n\n"
    content += f"# {entry['term']}\n\n"

    if entry["term"] in [
        "Electronic",
        "Rock",
        "Jazz",
        "Pop",
        "Blues",
        "Country",
        "Folk",
        "Classical",
        "Hip Hop",
        "Funk",
        "Soul",
        "Reggae",
        "Latin",
        "World",
        "Experimental",
        "Soundtrack",
    ]:
        content += f"**Definition:** A broad musical genre classification used in the Discogs database system.\n\n"
        content += f"**Context:** {entry['term']} is one of the primary genre categories that encompasses various musical styles and subgenres. This classification helps organize and categorize music releases in the world's largest music database.\n\n"
        content += f"**Usage:** Genre classifications like {entry['term']} are used by collectors, DJs, and music enthusiasts to categorize and discover music across different platforms and databases.\n\n"
    else:
        content += f"**Definition:** A specific musical style within the broader {entry.get('relationships', {}).get('parent_concept', 'music')} genre classification.\n\n"
        content += f"**Context:** {entry['term']} represents a distinct approach to music within its parent genre, characterized by specific musical elements, cultural influences, or historical development.\n\n"
        content += f"**Usage:** Style classifications like {entry['term']} help music enthusiasts identify and categorize specific sounds and approaches within broader genre categories.\n\n"

    content += "**Source:** This classification is based on the official Discogs taxonomy, ensuring consistency with the world's largest music database.\n\n"
    content += "**Note:** For the most up-to-date definitions and classifications, refer to the official Discogs database at [discogs.com](https://www.discogs.com/)."

    with open(term_file, "w", encoding="utf-8") as f:
        f.write(content)


def main():
    """Generate Discogs genre and style entries."""
    # Load current Discogs data
    discogs_file = Path("docs/data/discogs_genres.yml")
    if not discogs_file.exists():
        print(f"Error: {discogs_file} not found")
        return

    with open(discogs_file, "r", encoding="utf-8") as f:
        discogs_data = yaml.safe_load(f)

    terms_dir = Path("docs/terms")
    terms_dir.mkdir(parents=True, exist_ok=True)

    print("Generating Discogs genre and style entries...")

    created_count = 0

    # Create genre entries
    for genre_name, styles in discogs_data["genres"].items():
        if genre_name == "all":  # Skip the "all" meta-genre
            continue

        entry = create_genre_entry(genre_name, styles)
        write_term_file(entry, terms_dir)
        created_count += 1
        print(f"Created genre entry: {genre_name}")

    # Create style entries
    for genre_name, styles in discogs_data["genres"].items():
        if genre_name == "all":  # Skip the "all" meta-genre
            continue

        for style_name in styles:
            entry = create_style_entry(style_name, genre_name)
            write_term_file(entry, terms_dir)
            created_count += 1
            print(f"Created style entry: {style_name} (under {genre_name})")

    print(f"\nGenerated {created_count} Discogs genre and style entries")
    print("Next steps:")
    print("1. Update schema to reference these entries instead of enum fields")
    print("2. Set up Discogs API integration for v3.0 sync")
    print("3. Test the new structure with existing terms")


if __name__ == "__main__":
    main()
