#!/usr/bin/env python3
"""
Generate JSON-LD structured data for semantic web compatibility.
"""

import json
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List

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
                                    "path": f"terms/{letter_dir.name}/{term_file.stem}",
                                    "updated": front_matter.get(
                                        "updated", datetime.now().isoformat()
                                    ),
                                    "ai_metadata": front_matter.get("ai_metadata", {}),
                                }
                except Exception as e:
                    print(f"Error processing {term_file}: {e}")

    return terms


def generate_json_ld(
    term_data: Dict[str, Any], base_url: str = "https://vinyl-lexicon.com"
) -> Dict[str, Any]:
    """Generate JSON-LD structured data for a term."""
    json_ld = {
        "@context": {
            "@vocab": "https://schema.org/",
            "vinyl": "https://vinyl-lexicon.com/vocab/",
            "discogs": "https://www.discogs.com/",
        },
        "@type": "DefinedTerm",
        "@id": f"{base_url}/{term_data['path']}/",
        "name": term_data["name"],
        "description": term_data.get("summary", ""),
        "url": f"{base_url}/{term_data['path']}/",
        "dateModified": term_data.get("updated"),
        "identifier": term_data["slug"],
        "inDefinedTermSet": {
            "@type": "DefinedTermSet",
            "@id": f"{base_url}/",
            "name": "Vinyl Lexicon",
            "description": "Comprehensive digital reference for vinyl record culture, terminology, and collecting",
        },
    }

    # Add alternative names if available
    if "aliases" in term_data:
        json_ld["alternateName"] = term_data["aliases"]

    # Add genre information
    if term_data.get("genres"):
        json_ld["about"] = []
        for genre in term_data["genres"]:
            json_ld["about"].append(
                {
                    "@type": "MusicGenre",
                    "name": genre,
                    "url": f"{base_url}/discogs/genres/{genre.lower().replace(' ', '-')}/",
                }
            )

    # Add tags as keywords
    if term_data.get("tags"):
        json_ld["keywords"] = term_data["tags"]

    # Add related terms
    if term_data.get("related_terms"):
        json_ld["relatedTerms"] = []
        for related_slug in term_data["related_terms"]:
            json_ld["relatedTerms"].append(
                {
                    "@type": "DefinedTerm",
                    "@id": f"{base_url}/terms/{related_slug[0]}/{related_slug}/",
                }
            )

    # Add AI metadata if available
    ai_metadata = term_data.get("ai_metadata", {})
    if ai_metadata:
        json_ld["vinyl:complexityLevel"] = ai_metadata.get("complexity_level")
        json_ld["vinyl:domainExpertise"] = ai_metadata.get("domain_expertise")
        json_ld["vinyl:usageFrequency"] = ai_metadata.get("usage_frequency")
        json_ld["vinyl:temporalRelevance"] = ai_metadata.get("temporal_relevance")
        json_ld["vinyl:culturalSignificance"] = ai_metadata.get("cultural_significance")
        json_ld["vinyl:technicalAccuracy"] = ai_metadata.get("technical_accuracy")

        if ai_metadata.get("context_domains"):
            json_ld["vinyl:contextDomains"] = ai_metadata["context_domains"]

        if ai_metadata.get("learning_objectives"):
            json_ld["vinyl:learningObjectives"] = ai_metadata["learning_objectives"]

    # Add popularity information
    popularity = term_data.get("popularity")
    if popularity is not None:
        if isinstance(popularity, dict):
            popularity_value = popularity.get("current", 0)
        else:
            popularity_value = popularity
        json_ld["vinyl:popularity"] = {
            "@type": "QuantitativeValue",
            "value": popularity_value,
            "maxValue": 10,
            "minValue": 0,
        }

    # Add complexity information
    if term_data.get("complexity"):
        json_ld["vinyl:complexity"] = term_data["complexity"]

    # Add era information
    if term_data.get("era"):
        json_ld["vinyl:era"] = term_data["era"]

    # Add region information
    if term_data.get("region"):
        json_ld["vinyl:region"] = term_data["region"]

    return json_ld


def generate_all_json_ld(
    terms_dir: Path, output_dir: Path, base_url: str = "https://vinyl-lexicon.com"
) -> None:
    """Generate JSON-LD structured data for all terms."""
    print("Loading term data...")
    terms = load_term_data(terms_dir)
    print(f"Loaded {len(terms)} terms")

    print("Generating JSON-LD structured data...")

    # Create output directory
    output_dir.mkdir(parents=True, exist_ok=True)

    # Generate JSON-LD for each term
    for slug, term_data in terms.items():
        json_ld = generate_json_ld(term_data, base_url)

        # Save individual JSON-LD file
        output_file = output_dir / f"{slug}.jsonld"
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(json_ld, f, indent=2, ensure_ascii=False)

    # Generate master JSON-LD file with all terms
    master_json_ld = {
        "@context": {
            "@vocab": "https://schema.org/",
            "vinyl": "https://vinyl-lexicon.com/vocab/",
        },
        "@type": "DefinedTermSet",
        "@id": f"{base_url}/",
        "name": "Vinyl Lexicon",
        "description": "Comprehensive digital reference for vinyl record culture, terminology, and collecting",
        "url": f"{base_url}/",
        "dateModified": datetime.now().isoformat(),
        "hasDefinedTerm": [],
    }

    for slug, term_data in terms.items():
        json_ld = generate_json_ld(term_data, base_url)
        master_json_ld["hasDefinedTerm"].append(json_ld)

    # Save master JSON-LD file
    master_file = output_dir / "vinyl-lexicon.jsonld"
    with open(master_file, "w", encoding="utf-8") as f:
        json.dump(master_json_ld, f, indent=2, ensure_ascii=False)

    print(f"Generated JSON-LD for {len(terms)} terms")
    print(f"Saved individual files to {output_dir}")
    print(f"Saved master file to {master_file}")


@click.command()
@click.option(
    "--terms-dir", default="docs/terms", help="Directory containing term files"
)
@click.option(
    "--output-dir", default="docs/jsonld", help="Output directory for JSON-LD files"
)
@click.option(
    "--base-url", default="https://vinyl-lexicon.com", help="Base URL for the site"
)
def main(terms_dir: str, output_dir: str, base_url: str):
    """Generate JSON-LD structured data for semantic web compatibility."""
    terms_path = Path(terms_dir)
    output_path = Path(output_dir)

    if not terms_path.exists():
        print(f"Error: Terms directory not found at {terms_path}")
        return

    generate_all_json_ld(terms_path, output_path, base_url)


if __name__ == "__main__":
    main()
