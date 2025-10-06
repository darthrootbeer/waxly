#!/usr/bin/env python3
"""
Autolinking script for cross-references in term files.
Scans term content and automatically creates links to other terms mentioned in the text.
"""

import re
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import click
import yaml


def load_term_file(term_file: Path) -> Optional[Dict[str, any]]:
    """Load a term file and extract front-matter and content."""
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
        body_content = content[end_marker + 5 :]

        try:
            frontmatter = yaml.safe_load(frontmatter_text)
        except yaml.YAMLError as e:
            print(f"YAML parsing error in {term_file}: {e}")
            return None

        return {
            "frontmatter": frontmatter,
            "body": body_content,
            "raw_frontmatter": frontmatter_text,
        }

    except Exception as e:
        print(f"Error loading {term_file}: {e}")
        return None


def build_term_index(terms_dir: Path) -> Dict[str, Dict[str, any]]:
    """Build an index of all terms for cross-referencing."""
    term_index = {}

    for letter_dir in terms_dir.iterdir():
        if letter_dir.is_dir():
            for term_file in letter_dir.glob("*.md"):
                data = load_term_file(term_file)
                if data:
                    frontmatter = data["frontmatter"]
                    term_name = frontmatter.get("term", term_file.stem)
                    slug = frontmatter.get("slug", term_file.stem)

                    # Index by term name and slug
                    term_index[term_name.lower()] = {
                        "slug": slug,
                        "path": str(term_file.relative_to(Path("docs"))),
                        "term": term_name,
                    }
                    term_index[slug.lower()] = {
                        "slug": slug,
                        "path": str(term_file.relative_to(Path("docs"))),
                        "term": term_name,
                    }

                    # Also index aliases
                    aliases = frontmatter.get("aliases", [])
                    if isinstance(aliases, str):
                        aliases = [aliases]

                    for alias in aliases:
                        if alias:
                            term_index[alias.lower()] = {
                                "slug": slug,
                                "path": str(term_file.relative_to(Path("docs"))),
                                "term": term_name,
                            }

    return term_index


def find_term_mentions(
    text: str, term_index: Dict[str, Dict[str, any]]
) -> List[Tuple[str, str, str]]:
    """Find mentions of other terms in the text."""
    mentions = []

    # Common words that shouldn't be linked (too generic)
    skip_words = {
        "the",
        "and",
        "or",
        "but",
        "in",
        "on",
        "at",
        "to",
        "for",
        "of",
        "with",
        "by",
        "from",
        "up",
        "about",
        "into",
        "through",
        "during",
        "before",
        "after",
        "above",
        "below",
        "between",
        "among",
        "under",
        "over",
        "across",
        "around",
        "this",
        "that",
        "these",
        "those",
        "a",
        "an",
        "is",
        "are",
        "was",
        "were",
        "be",
        "been",
        "being",
        "have",
        "has",
        "had",
        "do",
        "does",
        "did",
        "will",
        "would",
        "could",
        "should",
        "may",
        "might",
        "must",
        "can",
        "shall",
        "i",
        "you",
        "he",
        "she",
        "it",
        "we",
        "they",
        "me",
        "him",
        "her",
        "us",
        "them",
        "my",
        "your",
        "his",
        "her",
        "its",
        "our",
        "their",
        "mine",
        "yours",
        "hers",
        "ours",
        "theirs",
        "plain",
        "back",
        "front",
        "top",
        "bottom",
        "left",
        "right",
        "center",
        "middle",
        "new",
        "old",
        "good",
        "bad",
        "big",
        "small",
        "high",
        "low",
        "long",
        "short",
        "first",
        "last",
        "next",
        "previous",
        "same",
        "different",
        "other",
        "another",
        "some",
        "any",
        "all",
        "each",
        "every",
        "many",
        "much",
        "few",
        "little",
        "more",
        "most",
        "less",
        "least",
        "better",
        "best",
        "worse",
        "worst",
    }

    # Split text into words and phrases
    # Look for potential term matches (case-insensitive)
    words = re.findall(r"\b\w+(?:\s+\w+)*\b", text)

    for word in words:
        word_lower = word.lower()

        # Skip common words
        if word_lower in skip_words:
            continue

        # Skip single letters
        if len(word_lower) <= 1:
            continue

        if word_lower in term_index:
            term_info = term_index[word_lower]
            mentions.append((word, term_info["slug"], term_info["term"]))

    # Remove duplicates while preserving order
    seen = set()
    unique_mentions = []
    for mention in mentions:
        if mention[1] not in seen:  # Use slug as unique identifier
            seen.add(mention[1])
            unique_mentions.append(mention)

    return unique_mentions


def create_autolinks(
    text: str, term_index: Dict[str, Dict[str, any]], current_slug: str
) -> str:
    """Create autolinks in the text content."""
    # Find all term mentions
    mentions = find_term_mentions(text, term_index)

    # Sort by length (longest first) to avoid partial matches
    mentions.sort(key=lambda x: len(x[0]), reverse=True)

    # Create links
    for original_text, target_slug, target_term in mentions:
        # Skip self-references
        if target_slug == current_slug:
            continue

        # Create the link path for MkDocs structure
        # Terms are organized as terms/{letter}/{slug}.md
        first_letter = target_slug[0].lower()
        link_path = f"../{first_letter}/{target_slug}.md"
        link_text = f"[{original_text}]({link_path})"

        # Replace the original text with the link
        # Use word boundaries to avoid partial matches
        pattern = r"\b" + re.escape(original_text) + r"\b"
        text = re.sub(pattern, link_text, text, count=1)

    return text


def process_term_file(term_file: Path, term_index: Dict[str, Dict[str, any]]) -> bool:
    """Process a single term file to add autolinks."""
    data = load_term_file(term_file)
    if not data:
        return False

    frontmatter = data["frontmatter"]
    body = data["body"]
    raw_frontmatter = data["raw_frontmatter"]

    current_slug = frontmatter.get("slug", term_file.stem)

    # Process the body content
    new_body = create_autolinks(body, term_index, current_slug)

    # Check if any changes were made
    if new_body != body:
        # Reconstruct the file
        new_content = f"---\n{raw_frontmatter}---\n{new_body}"

        # Write back to file
        with open(term_file, "w", encoding="utf-8") as f:
            f.write(new_content)

        return True

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
    "--dry-run", is_flag=True, help="Show what would be changed without making changes"
)
@click.option("--max-links", default=10, help="Maximum number of links to add per term")
def main(terms_dir: str, dry_run: bool, max_links: int):
    """Add autolinks to cross-references in term files."""
    terms_dir = Path(terms_dir)

    if not terms_dir.exists():
        print(f"Terms directory not found: {terms_dir}")
        return

    print(f"Building term index from {terms_dir}")
    term_index = build_term_index(terms_dir)
    print(f"Indexed {len(term_index)} terms and aliases")

    if dry_run:
        print("DRY RUN MODE - No changes will be made")

    term_files = find_term_files(terms_dir)
    print(f"Processing {len(term_files)} term files")

    processed_count = 0
    linked_count = 0
    error_count = 0

    for term_file in term_files:
        try:
            if dry_run:
                # Just check what would be linked
                data = load_term_file(term_file)
                if data:
                    body = data["body"]
                    current_slug = data["frontmatter"].get("slug", term_file.stem)
                    mentions = find_term_mentions(body, term_index)

                    # Filter out self-references
                    external_mentions = [m for m in mentions if m[1] != current_slug]

                    if external_mentions:
                        print(
                            f"Would add {len(external_mentions)} links to {term_file.name}:"
                        )
                        for original, slug, term in external_mentions[:max_links]:
                            print(f"  '{original}' -> {term} ({slug})")
                        linked_count += 1
            else:
                if process_term_file(term_file, term_index):
                    linked_count += 1

            processed_count += 1

        except Exception as e:
            print(f"Error processing {term_file}: {e}")
            error_count += 1

    print(f"\nResults:")
    print(f"Files processed: {processed_count}")
    print(f"Files with links added: {linked_count}")
    print(f"Errors: {error_count}")

    if dry_run and linked_count > 0:
        print(f"\nRun without --dry-run to apply these autolinks")


if __name__ == "__main__":
    main()
