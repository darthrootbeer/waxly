#!/usr/bin/env python3
"""
Clean up term slugs by removing extra descriptive information.

The slug should contain only the primary term name, with additional
context (slang, collector terms, etc.) moved to the content.
"""

import os
import re
import yaml
from pathlib import Path

# Mapping of current slugs to clean slugs
SLUG_CLEANUP_MAP = {
    # DJ slang terms
    'auxiliary-weight-dj-slang-slug': 'auxiliary-weight',
    'groovebox-djproducer-slang': 'groovebox',
    
    # Collector slang terms
    'fig-leaf-sleeve-collector-slang': 'fig-leaf-sleeve',
    'hard-bop-pressing-collector-slang': 'hard-bop-pressing',
    'j-cut-single-collector-slang': 'j-cut-single',
    'seam-stress-ring-wear-humorous-slang': 'seam-stress-ring-wear',
    
    # Defect/quality terms
    'non-fill-pressing-defect': 'non-fill',
    'foam-rot-aging-defect': 'foam-rot',
    'fish-eye-label-pressing-defect': 'fish-eye-label',
    'j-cut-groove-pressing-defect': 'j-cut-groove',
    'pressing-defect': 'pressing-defect',  # Keep this one as is
    
    # Effect/technique terms
    'flanging-tape-vinyl-effect': 'flanging',
    
    # Equipment terms
    'flight-case-road-case': 'flight-case',
    'changer-record-changer-stack-loader': 'record-changer',
    'drop-spindle-changer-spindle': 'drop-spindle',
    'electric-pick-up-early-term-for-cartridge': 'electric-pickup',
    
    # Record types
    'guitar-shaped-picture-disc-novelty-vinyl': 'guitar-shaped-picture-disc',
    'zoo-label-novelty-45': 'zoo-label',
    'quirky-cut-sleeve-novelty-die-cut-jacket': 'quirky-cut-sleeve',
    'kiss-style-picture-disc': 'kiss-style-picture-disc',  # Keep as is
    
    # Groove terms
    'spiral-track-locked-groove': 'spiral-track',
    'closed-groove-loop-locked-groove': 'closed-groove',
    'blank-groove-locked-groove': 'blank-groove',
    'perpetual-motion-loop-locked-groove-loop': 'perpetual-motion-loop',
    
    # Other terms
    'back-splice-aka-back-tape': 'back-splice',
    'blank-label-white-label': 'blank-label',
    'demo-copy-promotional-demo': 'demo-copy',
    'dead-wax-run-out-area': 'dead-wax',
    'dj-pool-record-pool': 'dj-pool',
    'reference-lacquer-reference-disc': 'reference-lacquer',
}

def clean_slug_in_file(file_path):
    """Clean up slug in a single markdown file."""
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
    
    if not frontmatter or 'slug' not in frontmatter:
        return False
    
    old_slug = frontmatter['slug']
    
    # Check if this slug needs cleaning
    if old_slug in SLUG_CLEANUP_MAP:
        new_slug = SLUG_CLEANUP_MAP[old_slug]
        
        # Update the slug in frontmatter
        frontmatter['slug'] = new_slug
        
        # Reconstruct the file
        new_frontmatter = yaml.dump(frontmatter, default_flow_style=False, sort_keys=False)
        new_content = f"---\n{new_frontmatter}---{body_content}"
        
        # Write back to file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"Updated {file_path}: {old_slug} → {new_slug}")
        return True
    
    return False

def move_file_if_needed(file_path, old_slug, new_slug):
    """Move file to new location if slug changed."""
    if old_slug == new_slug:
        return file_path
    
    # Determine new file path
    old_path = Path(file_path)
    new_filename = f"{new_slug}.md"
    new_path = old_path.parent / new_filename
    
    # Move the file
    old_path.rename(new_path)
    print(f"Moved {file_path} → {new_path}")
    
    return str(new_path)

def main():
    """Clean up all term slugs."""
    terms_dir = Path("docs/terms")
    
    if not terms_dir.exists():
        print("docs/terms directory not found")
        return
    
    updated_files = []
    
    # Process all markdown files
    for md_file in terms_dir.rglob("*.md"):
        if clean_slug_in_file(md_file):
            updated_files.append(md_file)
    
    # Move files if slugs changed
    for file_path in updated_files:
        old_slug = file_path.stem
        if old_slug in SLUG_CLEANUP_MAP:
            new_slug = SLUG_CLEANUP_MAP[old_slug]
            move_file_if_needed(file_path, old_slug, new_slug)
    
    print(f"\nCleaned up {len(updated_files)} files")

if __name__ == "__main__":
    main()
