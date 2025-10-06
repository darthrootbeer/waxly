#!/usr/bin/env python3
"""
Split the vinyl lexicon into individual chapter files by letter.
"""

import re
import os
from pathlib import Path

def split_lexicon():
    """Split the main lexicon file into chapter files."""

    # Define the project paths
    project_root = Path(__file__).parent.parent
    source_file = project_root / "vinyl_lexicon.md"
    chapters_dir = project_root / "content" / "books" / "vinyl-lexicon" / "chapters"

    print(f"Looking for source file: {source_file}")
    print(f"Source file exists: {source_file.exists()}")

    # Create chapters directory if it doesn't exist
    chapters_dir.mkdir(parents=True, exist_ok=True)

    # Read the source file
    with open(source_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find all letter sections
    letter_pattern = r'^# ([A-Z])$'
    letters = re.findall(letter_pattern, content, re.MULTILINE)

    print(f"Found letters: {letters}")

    # Split content by letter sections
    sections = re.split(letter_pattern, content, flags=re.MULTILINE)

    # Process each section (skip the first empty section)
    for i in range(1, len(sections), 2):
        if i + 1 < len(sections):
            letter = sections[i]
            letter_content = sections[i + 1]

            # Create chapter filename
            chapter_file = chapters_dir / f"chapter-{letter.lower()}.md"

            # Create chapter content with proper header
            chapter_content = f"""# Chapter {letter}

> **Terms beginning with '{letter}'**

{letter_content.strip()}

---

*[Back to Lexicon](../README.md) | [Next Chapter](../chapters/chapter-{get_next_letter(letter, letters).lower()}.md)*
"""

            # Write chapter file
            with open(chapter_file, 'w', encoding='utf-8') as f:
                f.write(chapter_content)

            print(f"Created {chapter_file}")

def get_next_letter(current_letter, letters):
    """Get the next letter in the alphabet from the letters list."""
    try:
        current_index = letters.index(current_letter)
        if current_index + 1 < len(letters):
            return letters[current_index + 1]
        else:
            return letters[0]  # Wrap around to first letter
    except ValueError:
        return letters[0]

def create_index():
    """Create an index file listing all chapters."""

    project_root = Path(__file__).parent.parent
    chapters_dir = project_root / "content" / "books" / "vinyl-lexicon" / "chapters"
    index_file = chapters_dir / "index.md"

    # Get all chapter files
    chapter_files = sorted(chapters_dir.glob("chapter-*.md"))

    # Create index content
    index_content = """# Vinyl Lexicon - Chapter Index

## Quick Navigation

"""

    for chapter_file in chapter_files:
        letter = chapter_file.stem.split('-')[1].upper()
        index_content += f"- **[Chapter {letter}]({chapter_file.name})** - Terms beginning with '{letter}'\n"

    index_content += """

## About This Index

This index provides quick access to all chapters of the Vinyl Lexicon. Each chapter contains all terms beginning with a specific letter of the alphabet.

For the complete lexicon experience, start with [Chapter A](chapter-a.md) and work your way through, or use this index to jump directly to terms of interest.

---

*[Back to Main Lexicon](../README.md)*
"""

    # Write index file
    with open(index_file, 'w', encoding='utf-8') as f:
        f.write(index_content)

    print(f"Created {index_file}")

if __name__ == "__main__":
    print("Splitting vinyl lexicon into chapters...")
    split_lexicon()
    print("\nCreating chapter index...")
    create_index()
    print("\nDone!")
