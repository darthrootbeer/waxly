#!/usr/bin/env python3
"""
Fix remaining issues after alternate term cleanup:
1. Update markdown headings to match clean term names
2. Fix any remaining slug issues
"""

import os
import re
import yaml
from pathlib import Path

def fix_file_issues(file_path):
    """Fix remaining issues in a single file."""
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
    
    if not frontmatter:
        return False
    
    changes_made = False
    
    # Fix markdown heading to match clean term name
    if 'term' in frontmatter:
        clean_term = frontmatter['term']
        # Find the current heading
        heading_match = re.search(r'^# (.+)$', body_content, re.MULTILINE)
        if heading_match:
            current_heading = heading_match.group(1)
            if current_heading != clean_term:
                # Replace the heading
                new_body = re.sub(r'^# .+$', f'# {clean_term}', body_content, flags=re.MULTILINE)
                body_content = new_body
                changes_made = True
    
    # Fix slug if it still contains alternate terms
    if 'slug' in frontmatter and 'aka' in frontmatter:
        current_slug = frontmatter['slug']
        clean_term = frontmatter['term']
        clean_slug = re.sub(r'[^a-z0-9]+', '-', clean_term.lower())
        clean_slug = re.sub(r'^-+|-+$', '', clean_slug)
        
        if current_slug != clean_slug:
            frontmatter['slug'] = clean_slug
            changes_made = True
    
    if changes_made:
        # Reconstruct the file
        new_frontmatter = yaml.dump(frontmatter, default_flow_style=False, sort_keys=False)
        new_content = f"---\n{new_frontmatter}---{body_content}"
        
        # Write back to file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"Fixed {file_path}")
        return True
    
    return False

def main():
    """Fix remaining issues in all term files."""
    terms_dir = Path("docs/terms")
    
    if not terms_dir.exists():
        print("docs/terms directory not found")
        return
    
    fixed_count = 0
    
    # Process all markdown files
    for md_file in terms_dir.rglob("*.md"):
        try:
            if fix_file_issues(md_file):
                fixed_count += 1
        except Exception as e:
            print(f"Error processing {md_file}: {e}")
    
    print(f"\nFixed {fixed_count} files")

if __name__ == "__main__":
    main()
