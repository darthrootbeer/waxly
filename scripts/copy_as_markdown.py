#!/usr/bin/env python3
"""
Generate copy-as-markdown functionality for easy AI training data extraction.
"""

import json
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List

import click
import markdown
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

                    # Extract front matter and content
                    if content.startswith("---"):
                        parts = content.split("---", 2)
                        if len(parts) >= 3:
                            front_matter = yaml.safe_load(parts[1])
                            markdown_content = parts[2].strip()

                            if front_matter and "slug" in front_matter:
                                slug = front_matter["slug"]
                                terms[slug] = {
                                    "name": front_matter.get(
                                        "title", slug.replace("-", " ").title()
                                    ),
                                    "slug": slug,
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
                                    "updated": front_matter.get(
                                        "updated", datetime.now().isoformat()
                                    ),
                                    "ai_metadata": front_matter.get("ai_metadata", {}),
                                }
                except Exception as e:
                    print(f"Error processing {term_file}: {e}")

    return terms


def format_term_as_markdown(
    term_data: Dict[str, Any], include_metadata: bool = True
) -> str:
    """Format a term as clean markdown for AI training."""
    markdown_lines = []

    # Title
    markdown_lines.append(f"# {term_data['name']}")
    markdown_lines.append("")

    # Summary
    if term_data.get("summary"):
        markdown_lines.append(f"**Summary:** {term_data['summary']}")
        markdown_lines.append("")

    # Definition
    if term_data.get("definition"):
        markdown_lines.append(f"**Definition:** {term_data['definition']}")
        markdown_lines.append("")

    # Tags
    if term_data.get("tags"):
        markdown_lines.append(f"**Tags:** {', '.join(term_data['tags'])}")
        markdown_lines.append("")

    # Genres
    if term_data.get("genres"):
        markdown_lines.append(f"**Genres:** {', '.join(term_data['genres'])}")
        markdown_lines.append("")

    # Related Terms
    if term_data.get("related_terms"):
        markdown_lines.append(
            f"**Related Terms:** {', '.join(term_data['related_terms'])}"
        )
        markdown_lines.append("")

    # Content
    if term_data.get("content"):
        markdown_lines.append("## Content")
        markdown_lines.append("")
        markdown_lines.append(term_data["content"])
        markdown_lines.append("")

    # Metadata (if requested)
    if include_metadata:
        markdown_lines.append("## Metadata")
        markdown_lines.append("")

        if term_data.get("complexity"):
            markdown_lines.append(f"- **Complexity:** {term_data['complexity']}")

        if term_data.get("era"):
            markdown_lines.append(f"- **Era:** {term_data['era']}")

        if term_data.get("region"):
            markdown_lines.append(f"- **Region:** {term_data['region']}")

        if term_data.get("popularity"):
            markdown_lines.append(f"- **Popularity:** {term_data['popularity']}")

        ai_metadata = term_data.get("ai_metadata", {})
        if ai_metadata:
            markdown_lines.append("- **AI Metadata:**")
            for key, value in ai_metadata.items():
                if value:
                    markdown_lines.append(f"  - {key}: {value}")

        markdown_lines.append("")

    return "\n".join(markdown_lines)


def generate_markdown_exports(
    terms_dir: Path, output_dir: Path, include_metadata: bool = True
) -> None:
    """Generate markdown exports for all terms."""
    print("Loading term data...")
    terms = load_term_data(terms_dir)
    print(f"Loaded {len(terms)} terms")

    print("Generating markdown exports...")

    # Create output directory
    output_dir.mkdir(parents=True, exist_ok=True)

    # Generate individual markdown files
    for slug, term_data in terms.items():
        markdown_content = format_term_as_markdown(term_data, include_metadata)

        # Save individual markdown file
        output_file = output_dir / f"{slug}.md"
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(markdown_content)

    # Generate master markdown file with all terms
    master_content = []
    master_content.append("# Vinyl Lexicon - Complete Markdown Export")
    master_content.append("")
    master_content.append(f"Generated: {datetime.now().isoformat()}")
    master_content.append(f"Total Terms: {len(terms)}")
    master_content.append("")
    master_content.append("---")
    master_content.append("")

    for slug, term_data in sorted(terms.items()):
        term_markdown = format_term_as_markdown(term_data, include_metadata)
        master_content.append(term_markdown)
        master_content.append("")
        master_content.append("---")
        master_content.append("")

    # Save master markdown file
    master_file = output_dir / "vinyl-lexicon-complete.md"
    with open(master_file, "w", encoding="utf-8") as f:
        f.write("\n".join(master_content))

    # Generate JSON export for easy processing
    json_export = {
        "metadata": {
            "generated_at": datetime.now().isoformat(),
            "total_terms": len(terms),
            "description": "Vinyl Lexicon markdown export for AI training",
        },
        "terms": {},
    }

    for slug, term_data in terms.items():
        json_export["terms"][slug] = {
            "markdown": format_term_as_markdown(term_data, include_metadata),
            "metadata": {
                "name": term_data["name"],
                "tags": term_data.get("tags", []),
                "genres": term_data.get("genres", []),
                "complexity": term_data.get("complexity", ""),
                "era": term_data.get("era", ""),
                "region": term_data.get("region", ""),
                "popularity": term_data.get("popularity", {}),
                "ai_metadata": term_data.get("ai_metadata", {}),
            },
        }

    # Save JSON export
    json_file = output_dir / "vinyl-lexicon-markdown.json"
    with open(json_file, "w", encoding="utf-8") as f:
        json.dump(json_export, f, indent=2, ensure_ascii=False)

    print(f"Generated markdown exports for {len(terms)} terms")
    print(f"Saved individual files to {output_dir}")
    print(f"Saved master file to {master_file}")
    print(f"Saved JSON export to {json_file}")


@click.command()
@click.option(
    "--terms-dir", default="docs/terms", help="Directory containing term files"
)
@click.option(
    "--output-dir",
    default="docs/markdown-export",
    help="Output directory for markdown exports",
)
@click.option(
    "--no-metadata", is_flag=True, help="Exclude metadata from markdown output"
)
def main(terms_dir: str, output_dir: str, no_metadata: bool):
    """Generate copy-as-markdown functionality for easy AI training data extraction."""
    terms_path = Path(terms_dir)
    output_path = Path(output_dir)

    if not terms_path.exists():
        print(f"Error: Terms directory not found at {terms_path}")
        return

    include_metadata = not no_metadata
    generate_markdown_exports(terms_path, output_path, include_metadata)


if __name__ == "__main__":
    main()
