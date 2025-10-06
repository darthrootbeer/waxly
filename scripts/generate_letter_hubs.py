#!/usr/bin/env python3
"""
Generate letter hub pages for the vinyl lexicon.
Creates index pages for each letter (a-z) that list all terms starting with that letter.
"""

import os
import glob
from pathlib import Path
from collections import defaultdict

def get_terms_by_letter():
    """Get all terms organized by their starting letter."""
    terms_dir = Path("docs/terms")
    terms_by_letter = defaultdict(list)
    
    if not terms_dir.exists():
        print(f"Terms directory {terms_dir} not found!")
        return terms_by_letter
    
    # Get all markdown files in terms directory
    for term_file in terms_dir.glob("**/*.md"):
        # Extract the term name from the filename
        term_name = term_file.stem
        if term_name and term_name[0].isalpha():
            letter = term_name[0].lower()
            terms_by_letter[letter].append({
                'name': term_name,
                'path': str(term_file.relative_to(Path("docs"))),
                'slug': term_name
            })
    
    # Sort terms within each letter
    for letter in terms_by_letter:
        terms_by_letter[letter].sort(key=lambda x: x['name'].lower())
    
    return terms_by_letter

def generate_letter_hub(letter, terms):
    """Generate a hub page for a specific letter."""
    letter_upper = letter.upper()
    letter_title = f"Terms starting with '{letter_upper}'"
    
    content = f"""# {letter_title}

Browse all vinyl terminology terms starting with the letter **{letter_upper}**.

## Terms ({len(terms)} total)

"""
    
    for term in terms:
        # Create a relative link to the term
        link_path = term['path'].replace('.md', '/')
        content += f"- [{term['name']}]({link_path})\n"
    
    content += f"""

---

**Browse by letter:** [A](a.md) • [B](b.md) • [C](c.md) • [D](d.md) • [E](e.md) • [F](f.md) • [G](g.md) • [H](h.md) • [I](i.md) • [J](j.md) • [K](k.md) • [L](l.md) • [M](m.md) • [N](n.md) • [O](o.md) • [P](p.md) • [Q](q.md) • [R](r.md) • [S](s.md) • [T](t.md) • [U](u.md) • [V](v.md) • [W](w.md) • [X](x.md) • [Y](y.md) • [Z](z.md)

**Browse by category:** [Equipment](../tags/equipment.md) • [DJ-related](../tags/dj-related.md) • [Pressing](../tags/pressing.md) • [Genres](../tags/genres.md) • [Historical](../tags/historical.md)

**Search:** Use the search function in the top navigation to find specific terms.
"""
    
    return content

def main():
    """Generate all letter hub pages."""
    print("Generating letter hub pages...")
    
    # Get terms organized by letter
    terms_by_letter = get_terms_by_letter()
    
    # Generate hub page for each letter
    letters_dir = Path("docs/letters")
    letters_dir.mkdir(exist_ok=True)
    
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        terms = terms_by_letter.get(letter, [])
        content = generate_letter_hub(letter, terms)
        
        # Write the hub page
        hub_file = letters_dir / f"{letter}.md"
        with open(hub_file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"Generated {hub_file} with {len(terms)} terms")
    
    print(f"Generated {len(terms_by_letter)} letter hub pages")

if __name__ == "__main__":
    main()
