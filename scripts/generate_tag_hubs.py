#!/usr/bin/env python3
"""
Generate tag hub pages for the vinyl lexicon.
Creates index pages for different categories/tags of terms.
"""

import os
import yaml
from pathlib import Path
from collections import defaultdict

def get_terms_by_tags():
    """Get all terms organized by their tags."""
    terms_dir = Path("docs/terms")
    terms_by_tag = defaultdict(list)
    
    if not terms_dir.exists():
        print(f"Terms directory {terms_dir} not found!")
        return terms_by_tag
    
    # Get all markdown files in terms directory
    for term_file in terms_dir.glob("**/*.md"):
        try:
            with open(term_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extract front matter
            if content.startswith('---'):
                parts = content.split('---', 2)
                if len(parts) >= 3:
                    front_matter = yaml.safe_load(parts[1])
                    term_name = term_file.stem
                    
                    # Get tags from front matter
                    tags = front_matter.get('tags', [])
                    if isinstance(tags, str):
                        tags = [tags]
                    
                    for tag in tags:
                        if tag:
                            terms_by_tag[tag].append({
                                'name': term_name,
                                'path': str(term_file.relative_to(Path("docs"))),
                                'slug': term_name,
                                'title': front_matter.get('term', term_name)
                            })
        except Exception as e:
            print(f"Error processing {term_file}: {e}")
            continue
    
    # Sort terms within each tag
    for tag in terms_by_tag:
        terms_by_tag[tag].sort(key=lambda x: x['name'].lower())
    
    return terms_by_tag

def generate_tag_hub(tag, terms):
    """Generate a hub page for a specific tag."""
    tag_title = tag.replace('-', ' ').title()
    
    content = f"""# {tag_title} Terms

Browse all vinyl terminology terms related to **{tag_title.lower()}**.

## Terms ({len(terms)} total)

"""
    
    for term in terms:
        # Create a relative link to the term
        link_path = term['path'].replace('.md', '/')
        display_name = term.get('title', term['name'])
        content += f"- [{display_name}]({link_path})\n"
    
    content += f"""

---

**Browse by letter:** [A](../letters/a.md) • [B](../letters/b.md) • [C](../letters/c.md) • [D](../letters/d.md) • [E](../letters/e.md) • [F](../letters/f.md) • [G](../letters/g.md) • [H](../letters/h.md) • [I](../letters/i.md) • [J](../letters/j.md) • [K](../letters/k.md) • [L](../letters/l.md) • [M](../letters/m.md) • [N](../letters/n.md) • [O](../letters/o.md) • [P](../letters/p.md) • [Q](../letters/q.md) • [R](../letters/r.md) • [S](../letters/s.md) • [T](../letters/t.md) • [U](../letters/u.md) • [V](../letters/v.md) • [W](../letters/w.md) • [X](../letters/x.md) • [Y](../letters/y.md) • [Z](../letters/z.md)

**Browse by category:** [Equipment](equipment.md) • [DJ-related](dj-related.md) • [Pressing](pressing.md) • [Genres](genres.md) • [Historical](historical.md)

**Search:** Use the search function in the top navigation to find specific terms.
"""
    
    return content

def main():
    """Generate all tag hub pages."""
    print("Generating tag hub pages...")
    
    # Get terms organized by tags
    terms_by_tag = get_terms_by_tags()
    
    # Define the main categories we want to create
    main_categories = {
        'equipment': 'Equipment and hardware terms',
        'dj-related': 'DJ and mixing terminology',
        'pressing': 'Pressing and manufacturing terms',
        'genres': 'Music genre and style terms',
        'historical': 'Historical and vintage terms'
    }
    
    # Generate hub page for each main category
    tags_dir = Path("docs/tags")
    tags_dir.mkdir(exist_ok=True)
    
    for category, description in main_categories.items():
        # Get terms for this category (case-insensitive matching)
        category_terms = []
        for tag, terms in terms_by_tag.items():
            if category.lower() in tag.lower() or tag.lower() in category.lower():
                category_terms.extend(terms)
        
        # Remove duplicates
        seen = set()
        unique_terms = []
        for term in category_terms:
            if term['name'] not in seen:
                seen.add(term['name'])
                unique_terms.append(term)
        
        # Sort unique terms
        unique_terms.sort(key=lambda x: x['name'].lower())
        
        content = f"""# {description}

Browse all vinyl terminology terms related to **{description.lower()}**.

## Terms ({len(unique_terms)} total)

"""
        
        for term in unique_terms:
            # Create a relative link to the term
            link_path = term['path'].replace('.md', '/')
            display_name = term.get('title', term['name'])
            content += f"- [{display_name}]({link_path})\n"
        
        content += f"""

---

**Browse by letter:** [A](../letters/a.md) • [B](../letters/b.md) • [C](../letters/c.md) • [D](../letters/d.md) • [E](../letters/e.md) • [F](../letters/f.md) • [G](../letters/g.md) • [H](../letters/h.md) • [I](../letters/i.md) • [J](../letters/j.md) • [K](../letters/k.md) • [L](../letters/l.md) • [M](../letters/m.md) • [N](../letters/n.md) • [O](../letters/o.md) • [P](../letters/p.md) • [Q](../letters/q.md) • [R](../letters/r.md) • [S](../letters/s.md) • [T](../letters/t.md) • [U](../letters/u.md) • [V](../letters/v.md) • [W](../letters/w.md) • [X](../letters/x.md) • [Y](../letters/y.md) • [Z](../letters/z.md)

**Browse by category:** [Equipment](equipment.md) • [DJ-related](dj-related.md) • [Pressing](pressing.md) • [Genres](genres.md) • [Historical](historical.md)

**Search:** Use the search function in the top navigation to find specific terms.
"""
        
        # Write the hub page
        hub_file = tags_dir / f"{category}.md"
        with open(hub_file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"Generated {hub_file} with {len(unique_terms)} terms")
    
    print(f"Generated {len(main_categories)} tag hub pages")

if __name__ == "__main__":
    main()
