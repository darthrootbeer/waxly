#!/usr/bin/env python3
"""
Validate term front-matter against schema.

This script validates all term files to ensure they conform to the
term schema and have complete, accurate metadata.
"""

import json
import os
from pathlib import Path
from typing import Any, Dict, List, Optional

import click
import jsonschema
import yaml
from jsonschema import ValidationError, validate


def load_schema(schema_path: Path) -> Dict[str, Any]:
    """Load the term schema from JSON file."""
    with open(schema_path, "r") as f:
        return json.load(f)


def load_term_file(term_file: Path) -> Optional[Dict[str, Any]]:
    """Load a term file and extract front-matter."""
    try:
        with open(term_file, "r", encoding="utf-8") as f:
            content = f.read()

        # Extract front-matter
        if not content.startswith("---\n"):
            return None

        # Find the end of front-matter
        end_marker = content.find("\n---\n", 4)
        if end_marker == -1:
            return None

        frontmatter_text = content[4:end_marker]
        frontmatter = yaml.safe_load(frontmatter_text)

        return frontmatter

    except Exception as e:
        print(f"Error loading {term_file}: {e}")
        return None


def validate_term(
    term_data: Dict[str, Any], schema: Dict[str, Any], term_file: Path
) -> List[str]:
    """Validate a single term against the schema."""
    errors = []

    try:
        validate(instance=term_data, schema=schema)
    except ValidationError as e:
        errors.append(f"Schema validation error: {e.message}")
    except Exception as e:
        errors.append(f"Validation error: {e}")

    # Additional custom validations
    errors.extend(validate_custom_rules(term_data, term_file))

    return errors


def validate_custom_rules(term_data: Dict[str, Any], term_file: Path) -> List[str]:
    """Apply custom validation rules beyond schema."""
    errors = []

    # Check required fields
    required_fields = ["term", "slug", "pos", "summary", "updated"]
    for field in required_fields:
        if field not in term_data or not term_data[field]:
            errors.append(f"Missing required field: {field}")

    # Check slug matches filename
    expected_slug = term_file.stem
    if term_data.get("slug") != expected_slug:
        errors.append(
            f"Slug '{term_data.get('slug')}' doesn't match filename '{expected_slug}'"
        )

    # Check see_also links exist
    see_also = term_data.get("see_also", [])
    for link in see_also:
        if not is_valid_slug(link):
            errors.append(f"Invalid see_also slug: {link}")

    # Check aliases are valid slugs
    aliases = term_data.get("aliases", [])
    for alias in aliases:
        if not is_valid_slug(alias):
            errors.append(f"Invalid alias slug: {alias}")

    # Check popularity is in valid range
    popularity = term_data.get("popularity")
    if popularity is not None and (popularity < 1 or popularity > 10):
        errors.append(f"Popularity {popularity} must be between 1 and 10")

    # Check complexity is valid
    valid_complexities = ["beginner", "intermediate", "advanced", "expert"]
    complexity = term_data.get("complexity")
    if complexity and complexity not in valid_complexities:
        errors.append(f"Invalid complexity: {complexity}")

    # Check status is valid
    valid_statuses = ["active", "archaic", "obsolete", "revived"]
    status = term_data.get("status")
    if status and status not in valid_statuses:
        errors.append(f"Invalid status: {status}")

    # Check verification is valid
    valid_verifications = ["verified", "unverified", "contested", "needs_research"]
    verification = term_data.get("verification")
    if verification and verification not in valid_verifications:
        errors.append(f"Invalid verification: {verification}")

    return errors


def is_valid_slug(slug: str) -> bool:
    """Check if a slug is valid (lowercase, hyphens, alphanumeric)."""
    import re

    return bool(re.match(r"^[a-z0-9-]+$", slug))


def find_term_files(terms_dir: Path) -> List[Path]:
    """Find all term files in the terms directory."""
    term_files = []

    for letter_dir in terms_dir.iterdir():
        if letter_dir.is_dir():
            for term_file in letter_dir.glob("*.md"):
                term_files.append(term_file)

    return sorted(term_files)


def validate_all_terms(terms_dir: Path, schema_path: Path) -> Dict[str, Any]:
    """Validate all term files."""
    schema = load_schema(schema_path)
    term_files = find_term_files(terms_dir)

    results = {
        "total_files": len(term_files),
        "valid_files": 0,
        "invalid_files": 0,
        "errors": [],
        "warnings": [],
    }

    for term_file in term_files:
        term_data = load_term_file(term_file)

        if term_data is None:
            results["errors"].append(f"Could not load {term_file}")
            results["invalid_files"] += 1
            continue

        errors = validate_term(term_data, schema, term_file)

        if errors:
            results["errors"].extend([f"{term_file}: {error}" for error in errors])
            results["invalid_files"] += 1
        else:
            results["valid_files"] += 1

    return results


def print_results(results: Dict[str, Any]) -> None:
    """Print validation results."""
    print(f"\nValidation Results:")
    print(f"Total files: {results['total_files']}")
    print(f"Valid files: {results['valid_files']}")
    print(f"Invalid files: {results['invalid_files']}")

    if results["errors"]:
        print(f"\nErrors ({len(results['errors'])}):")
        for error in results["errors"]:
            print(f"  ❌ {error}")

    if results["warnings"]:
        print(f"\nWarnings ({len(results['warnings'])}):")
        for warning in results["warnings"]:
            print(f"  ⚠️  {warning}")

    if results["invalid_files"] == 0:
        print("\n✅ All term files are valid!")
    else:
        print(f"\n❌ {results['invalid_files']} files have validation errors")


@click.command()
@click.option(
    "--terms-dir", default="docs/terms", help="Directory containing term files"
)
@click.option(
    "--schema-path", default="schema/term.schema.json", help="Path to term schema"
)
@click.option("--fix", is_flag=True, help="Attempt to fix common issues")
def main(terms_dir: str, schema_path: str, fix: bool):
    """Validate term files against schema."""
    terms_dir = Path(terms_dir)
    schema_path = Path(schema_path)

    if not terms_dir.exists():
        print(f"Terms directory not found: {terms_dir}")
        return

    if not schema_path.exists():
        print(f"Schema file not found: {schema_path}")
        return

    print(f"Validating terms in {terms_dir}")
    print(f"Using schema from {schema_path}")

    results = validate_all_terms(terms_dir, schema_path)
    print_results(results)

    if results["invalid_files"] > 0:
        exit(1)


if __name__ == "__main__":
    main()
