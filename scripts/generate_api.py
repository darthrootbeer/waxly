#!/usr/bin/env python3
"""
Generate JSON API export of all terms.
"""

import json
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List

import click
import yaml


def load_term_data(terms_dir: Path) -> List[Dict[str, Any]]:
    """Load all term data from markdown files."""
    terms = []

    for letter_dir in terms_dir.iterdir():
        if letter_dir.is_dir():
            for term_file in letter_dir.glob("*.md"):
                try:
                    with open(term_file, "r", encoding="utf-8") as f:
                        content = f.read()

                    # Extract front matter and content
                    if content.startswith("---"):
                        parts = content.split("---", 2)
                        if len(parts) >= 3:
                            front_matter = yaml.safe_load(parts[1])
                            markdown_content = parts[2].strip()

                            if front_matter and "slug" in front_matter:
                                term_data = {
                                    "slug": front_matter["slug"],
                                    "name": front_matter.get(
                                        "title",
                                        front_matter["slug"].replace("-", " ").title(),
                                    ),
                                    "summary": front_matter.get("summary", ""),
                                    "definition": front_matter.get("definition", ""),
                                    "tags": front_matter.get("tags", []),
                                    "genres": front_matter.get("genres", []),
                                    "related_terms": front_matter.get(
                                        "related_terms", []
                                    ),
                                    "popularity": front_matter.get("popularity", {}),
                                    "complexity": front_matter.get("complexity", ""),
                                    "era": front_matter.get("era", ""),
                                    "region": front_matter.get("region", ""),
                                    "content": markdown_content,
                                    "path": f"terms/{letter_dir.name}/{term_file.stem}",
                                    "letter": letter_dir.name,
                                    "updated": datetime.now().isoformat(),
                                }
                                terms.append(term_data)
                except Exception as e:
                    print(f"Error processing {term_file}: {e}")

    return terms


def generate_api_export(terms_dir: Path, output_file: Path) -> None:
    """Generate JSON API export of all terms."""
    print("Loading term data...")
    terms = load_term_data(terms_dir)
    print(f"Loaded {len(terms)} terms")

    # Create API response structure
    api_data = {
        "meta": {
            "version": "1.0.0",
            "total_terms": len(terms),
            "generated_at": datetime.now().isoformat(),
            "description": "Vinyl Lexicon API - Comprehensive vinyl record terminology database",
        },
        "terms": terms,
    }

    # Save as JSON
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(api_data, f, indent=2, ensure_ascii=False)

    print(f"Generated API export with {len(terms)} terms")
    print(f"Saved to {output_file}")


@click.command()
@click.option(
    "--terms-dir", default="docs/terms", help="Directory containing term files"
)
@click.option(
    "--output-file", default="docs/api/terms.json", help="Output file for API export"
)
def main(terms_dir: str, output_file: str):
    """Generate JSON API export of all terms."""
    terms_path = Path(terms_dir)
    output_path = Path(output_file)

    if not terms_path.exists():
        print(f"Error: Terms directory not found at {terms_path}")
        return

    # Ensure output directory exists
    output_path.parent.mkdir(parents=True, exist_ok=True)

    generate_api_export(terms_path, output_path)


if __name__ == "__main__":
    main()
