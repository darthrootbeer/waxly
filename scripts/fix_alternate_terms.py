#!/usr/bin/env python3
"""
Fix terms that have alternate names in their titles or slugs.

Examples:
- "Banding (Groove Banding)" → "Banding" with aka: ["Groove Banding"]
- "slug: banding-groove-banding" → "slug: banding"
"""

import os
import re
import yaml
from pathlib import Path

# Common patterns of alternate terms in titles
ALTERNATE_PATTERNS = [
    r'^(.+?)\s*\((.+?)\)$',  # "Term (Alternate)"
    r'^(.+?)\s*/\s*(.+?)$',   # "Term / Alternate"
    r'^(.+?)\s*:\s*(.+?)$',   # "Term: Alternate"
    r'^(.+?)\s*-\s*(.+?)$',   # "Term - Alternate" (be careful with this one)
]

def extract_primary_and_alternate(term_title):
    """Extract primary term and alternate from title patterns."""
    for pattern in ALTERNATE_PATTERNS:
        match = re.match(pattern, term_title.strip())
        if match:
            primary = match.group(1).strip()
            alternate = match.group(2).strip()
            
            # Skip if alternate looks like a description rather than alternate name
            if len(alternate) > len(primary) * 2:
                continue
                
            return primary, alternate
    
    return None, None

def fix_term_file(file_path):
    """Fix a single term file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split frontmatter and content
    if not content.startswith('---'):
        return False
    
    parts = content.split('---', 2)
    if len(parts) < 3:
        return False
    
    frontmatter_text = parts[1]
    body_content = parts[2]
    
    try:
        frontmatter = yaml.safe_load(frontmatter_text)
    except yaml.YAMLError:
        return False
    
    if not frontmatter or 'term' not in frontmatter:
        return False
    
    original_term = frontmatter['term']
    primary, alternate = extract_primary_and_alternate(original_term)
    
    if not primary or not alternate:
        return False
    
    # Update the term title
    frontmatter['term'] = primary
    
    # Add aka field if it doesn't exist
    if 'aka' not in frontmatter:
        frontmatter['aka'] = []
    
    # Add alternate to aka list
    if alternate not in frontmatter['aka']:
        frontmatter['aka'].append(alternate)
    
    # Update slug if it contains the alternate term
    if 'slug' in frontmatter:
        old_slug = frontmatter['slug']
        # Create clean slug from primary term
        clean_slug = re.sub(r'[^a-z0-9]+', '-', primary.lower())
        clean_slug = re.sub(r'^-+|-+$', '', clean_slug)
        
        if old_slug != clean_slug:
            frontmatter['slug'] = clean_slug
    
    # Update the markdown heading in body
    new_body = body_content
    if body_content.startswith(f'# {original_term}'):
        new_body = body_content.replace(f'# {original_term}', f'# {primary}', 1)
    
    # Reconstruct the file
    new_frontmatter = yaml.dump(frontmatter, default_flow_style=False, sort_keys=False)
    new_content = f"---\n{new_frontmatter}---{new_body}"
    
    # Write back to file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"Fixed {file_path}: '{original_term}' → '{primary}' (aka: {alternate})")
    return True, original_term, primary, alternate

def main():
    """Fix all terms with alternate names in titles."""
    terms_dir = Path("docs/terms")
    
    if not terms_dir.exists():
        print("docs/terms directory not found")
        return
    
    fixed_files = []
    
    # Process all markdown files
    for md_file in terms_dir.rglob("*.md"):
        try:
            result = fix_term_file(md_file)
            if result:
                fixed_files.append(result)
        except Exception as e:
            print(f"Error processing {md_file}: {e}")
    
    # Move files if slugs changed
    for result in fixed_files:
        if isinstance(result, tuple) and len(result) == 4:
            file_path, old_term, new_term, alternate = result
            old_slug = Path(file_path).stem
            new_slug = re.sub(r'[^a-z0-9]+', '-', new_term.lower())
            new_slug = re.sub(r'^-+|-+$', '', new_slug)
            
            if old_slug != new_slug:
                old_path = Path(file_path)
                new_path = old_path.parent / f"{new_slug}.md"
                old_path.rename(new_path)
                print(f"Moved {file_path} → {new_path}")
    
    print(f"\nFixed {len(fixed_files)} terms with alternate names in titles")

if __name__ == "__main__":
    main()
