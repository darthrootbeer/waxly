#!/usr/bin/env python3
"""
Fix validation issues in term files.
- Rename genre_association to genres
- Fix slug mismatches to match filenames
- Fix YAML parsing errors
"""

import os
import yaml
from pathlib import Path
from typing import Dict, List, Optional, Any
import click


def load_term_file(term_file: Path) -> Optional[Dict[str, Any]]:
    """Load a term file and extract front-matter and content."""
    try:
        with open(term_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract front-matter
        if not content.startswith('---\n'):
            return None
        
        # Find the end of front-matter
        end_marker = content.find('\n---\n', 4)
        if end_marker == -1:
            return None
        
        frontmatter_text = content[4:end_marker]
        body_content = content[end_marker + 5:]
        
        try:
            frontmatter = yaml.safe_load(frontmatter_text)
        except yaml.YAMLError as e:
            print(f"YAML parsing error in {term_file}: {e}")
            return None
        
        return {
            'frontmatter': frontmatter,
            'body': body_content,
            'raw_frontmatter': frontmatter_text
        }
    
    except Exception as e:
        print(f"Error loading {term_file}: {e}")
        return None


def fix_term_file(term_file: Path) -> bool:
    """Fix validation issues in a single term file."""
    data = load_term_file(term_file)
    if not data:
        return False
    
    frontmatter = data['frontmatter']
    body = data['body']
    raw_frontmatter = data['raw_frontmatter']
    
    changes_made = False
    
    # Fix genre_association -> genres
    if 'genre_association' in frontmatter:
        frontmatter['genres'] = frontmatter.pop('genre_association')
        changes_made = True
        print(f"  Fixed genre_association -> genres in {term_file.name}")
    
    # Fix slug to match filename
    expected_slug = term_file.stem
    if frontmatter.get('slug') != expected_slug:
        frontmatter['slug'] = expected_slug
        changes_made = True
        print(f"  Fixed slug '{frontmatter.get('slug', 'None')}' -> '{expected_slug}' in {term_file.name}")
    
    # Fix genre case sensitivity
    if 'genres' in frontmatter and isinstance(frontmatter['genres'], list):
        genre_mapping = {
            'hip_hop': 'Hip Hop',
            'rock': 'Rock',
            'electronic': 'Electronic',
            'jazz': 'Jazz',
            'classical': 'Classical',
            'pop': 'Pop',
            'blues': 'Blues',
            'folk': 'Folk, World, & Country',
            'country': 'Folk, World, & Country',
            'funk': 'Funk / Soul',
            'soul': 'Funk / Soul',
            'reggae': 'Reggae',
            'latin': 'Latin',
            'non_music': 'Non-Music',
            'children': "Children's",
            'brass': 'Brass & Military',
            'military': 'Brass & Military',
            'stage': 'Stage & Screen',
            'screen': 'Stage & Screen'
        }
        
        fixed_genres = []
        for genre in frontmatter['genres']:
            if isinstance(genre, str):
                # Convert snake_case to proper case
                if genre in genre_mapping:
                    fixed_genres.append(genre_mapping[genre])
                    changes_made = True
                else:
                    # Keep original if not in mapping
                    fixed_genres.append(genre)
            else:
                fixed_genres.append(genre)
        
        if changes_made:
            frontmatter['genres'] = fixed_genres
            print(f"  Fixed genre case sensitivity in {term_file.name}")
    
    # Fix YAML parsing issues (unclosed quotes, etc.)
    if "'" in raw_frontmatter and raw_frontmatter.count("'") % 2 != 0:
        # Fix unclosed single quotes in summary field
        if 'summary' in frontmatter and isinstance(frontmatter['summary'], str):
            if frontmatter['summary'].endswith("'"):
                frontmatter['summary'] = frontmatter['summary'].rstrip("'")
                changes_made = True
                print(f"  Fixed unclosed quote in summary for {term_file.name}")
    
    if changes_made:
        # Reconstruct the file
        new_frontmatter = yaml.dump(frontmatter, default_flow_style=False, allow_unicode=True, sort_keys=False)
        new_content = f"---\n{new_frontmatter}---\n{body}"
        
        # Write back to file
        with open(term_file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        return True
    
    return False


def find_term_files(terms_dir: Path) -> List[Path]:
    """Find all term files in the terms directory."""
    term_files = []
    
    for letter_dir in terms_dir.iterdir():
        if letter_dir.is_dir():
            for term_file in letter_dir.glob('*.md'):
                term_files.append(term_file)
    
    return sorted(term_files)


@click.command()
@click.option('--terms-dir', default='docs/terms', help='Directory containing term files')
@click.option('--dry-run', is_flag=True, help='Show what would be changed without making changes')
def main(terms_dir: str, dry_run: bool):
    """Fix validation issues in term files."""
    terms_dir = Path(terms_dir)
    
    if not terms_dir.exists():
        print(f"Terms directory not found: {terms_dir}")
        return
    
    print(f"Fixing validation issues in {terms_dir}")
    if dry_run:
        print("DRY RUN MODE - No changes will be made")
    
    term_files = find_term_files(terms_dir)
    print(f"Found {len(term_files)} term files")
    
    fixed_count = 0
    error_count = 0
    
    for term_file in term_files:
        try:
            if dry_run:
                # Just check what would be fixed
                data = load_term_file(term_file)
                if data:
                    frontmatter = data['frontmatter']
                    changes = []
                    
                    if 'genre_association' in frontmatter:
                        changes.append("genre_association -> genres")
                    
                    expected_slug = term_file.stem
                    if frontmatter.get('slug') != expected_slug:
                        changes.append(f"slug '{frontmatter.get('slug')}' -> '{expected_slug}'")
                    
                    if changes:
                        print(f"Would fix {term_file.name}: {', '.join(changes)}")
                        fixed_count += 1
            else:
                if fix_term_file(term_file):
                    fixed_count += 1
        except Exception as e:
            print(f"Error processing {term_file}: {e}")
            error_count += 1
    
    print(f"\nResults:")
    print(f"Files processed: {len(term_files)}")
    print(f"Files fixed: {fixed_count}")
    print(f"Errors: {error_count}")
    
    if dry_run and fixed_count > 0:
        print(f"\nRun without --dry-run to apply these fixes")


if __name__ == '__main__':
    main()
