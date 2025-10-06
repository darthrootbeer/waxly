#!/usr/bin/env python3
"""
Migrate chapter-based content to individual term files.

This script converts the existing chapter-based structure to the new
one-term-per-file structure with rich metadata.
"""

import os
import re
import yaml
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Term:
    """Represents a single term with all its metadata."""
    name: str
    slug: str
    pos: str
    definition: str
    etymology: str = ""
    example: str = ""
    cultural_note: str = ""
    see_also: List[str] = None
    aliases: List[str] = None
    tags: List[str] = None
    domains: List[str] = None
    regions: List[str] = None
    eras: List[str] = None
    first_attested: str = ""
    pronunciation: str = ""
    sources: List[Dict] = None
    summary: str = ""
    updated: str = ""
    popularity: int = 5
    complexity: str = "intermediate"
    status: str = "active"
    context: str = "technical"
    verification: str = "unverified"
    equipment_association: List[str] = None
    genre_association: List[str] = None
    decade: str = ""
    
    def __post_init__(self):
        if self.see_also is None:
            self.see_also = []
        if self.aliases is None:
            self.aliases = []
        if self.tags is None:
            self.tags = []
        if self.domains is None:
            self.domains = []
        if self.regions is None:
            self.regions = ["US"]
        if self.eras is None:
            self.eras = []
        if self.sources is None:
            self.sources = []
        if self.equipment_association is None:
            self.equipment_association = []
        if self.genre_association is None:
            self.genre_association = ["all"]
        if not self.updated:
            self.updated = datetime.now().strftime("%Y-%m-%d")
        if not self.summary:
            self.summary = self.definition[:200] + "..." if len(self.definition) > 200 else self.definition


def slugify(text: str) -> str:
    """Convert text to URL-friendly slug."""
    # Remove special characters and convert to lowercase
    slug = re.sub(r'[^\w\s-]', '', text.lower())
    # Replace spaces and multiple hyphens with single hyphens
    slug = re.sub(r'[-\s]+', '-', slug)
    # Remove leading/trailing hyphens
    return slug.strip('-')


def extract_pos(definition: str) -> str:
    """Extract part of speech from definition."""
    pos_patterns = {
        'noun': r'\(\*\*noun\.?\*\*\)',
        'verb': r'\(\*\*verb\.?\*\*\)',
        'adjective': r'\(\*\*adjective\.?\*\*\)',
        'adverb': r'\(\*\*adverb\.?\*\*\)',
        'phrase': r'\(\*\*phrase\.?\*\*\)',
        'abbreviation': r'\(\*\*abbreviation\.?\*\*\)',
        'acronym': r'\(\*\*acronym\.?\*\*\)'
    }
    
    for pos, pattern in pos_patterns.items():
        if re.search(pattern, definition, re.IGNORECASE):
            return pos
    
    return 'noun'  # Default


def parse_term_section(section: str) -> Optional[Term]:
    """Parse a term section from chapter content."""
    lines = section.strip().split('\n')
    if not lines:
        return None
    
    # Extract term name (first line after ##)
    name_line = lines[0]
    if not name_line.startswith('## '):
        return None
    
    name = name_line[3:].strip()
    slug = slugify(name)
    
    # Extract definition (next line)
    definition = ""
    etymology = ""
    example = ""
    cultural_note = ""
    see_also = []
    
    current_section = "definition"
    
    for line in lines[1:]:
        line = line.strip()
        if not line:
            continue
            
        if line.startswith('**Etymology:**'):
            current_section = "etymology"
            etymology = line[14:].strip()
        elif line.startswith('**Example:**'):
            current_section = "example"
            example = line[12:].strip()
        elif line.startswith('**Cultural Note:**'):
            current_section = "cultural_note"
            cultural_note = line[17:].strip()
        elif line.startswith('**See also:**'):
            current_section = "see_also"
            see_also_text = line[13:].strip()
            see_also = [item.strip() for item in see_also_text.split(',')]
        else:
            if current_section == "definition":
                definition += " " + line
            elif current_section == "etymology":
                etymology += " " + line
            elif current_section == "example":
                example += " " + line
            elif current_section == "cultural_note":
                cultural_note += " " + line
    
    # Clean up text
    definition = re.sub(r'\s+', ' ', definition).strip()
    etymology = re.sub(r'\s+', ' ', etymology).strip()
    example = re.sub(r'\s+', ' ', example).strip()
    cultural_note = re.sub(r'\s+', ' ', cultural_note).strip()
    
    # Extract POS from definition
    pos = extract_pos(definition)
    
    # Remove POS from definition
    definition = re.sub(r'\(\*\*[^*]+\*\*\)\s*', '', definition).strip()
    
    # Generate tags based on content
    tags = generate_tags(name, definition, cultural_note)
    
    # Generate domains based on content
    domains = generate_domains(name, definition, cultural_note)
    
    # Generate equipment associations
    equipment_association = generate_equipment_association(name, definition)
    
    # Generate genre associations
    genre_association = generate_genre_association(name, definition, cultural_note)
    
    # Generate decade based on cultural note
    decade = generate_decade(cultural_note)
    
    return Term(
        name=name,
        slug=slug,
        pos=pos,
        definition=definition,
        etymology=etymology,
        example=example,
        cultural_note=cultural_note,
        see_also=see_also,
        tags=tags,
        domains=domains,
        equipment_association=equipment_association,
        genre_association=genre_association,
        decade=decade
    )


def generate_tags(name: str, definition: str, cultural_note: str) -> List[str]:
    """Generate tags based on term content."""
    tags = []
    content = (name + " " + definition + " " + cultural_note).lower()
    
    # Equipment tags
    if any(word in content for word in ['turntable', 'tonearm', 'cartridge', 'stylus', 'mixer', 'amplifier']):
        tags.append('equipment')
    
    # DJ tags
    if any(word in content for word in ['dj', 'scratch', 'mix', 'beat', 'break']):
        tags.append('dj-related')
    
    # Pressing tags
    if any(word in content for word in ['press', 'pressing', 'lacquer', 'master', 'cut']):
        tags.append('pressing')
    
    # Collecting tags
    if any(word in content for word in ['collect', 'grade', 'condition', 'rare', 'value']):
        tags.append('collecting')
    
    # Technical tags
    if any(word in content for word in ['technical', 'specification', 'measurement', 'engineering']):
        tags.append('technical')
    
    # Historical tags
    if any(word in content for word in ['1940s', '1950s', '1960s', '1970s', '1980s', 'historical', 'vintage']):
        tags.append('historical')
    
    # Cultural tags
    if any(word in content for word in ['culture', 'social', 'movement', 'scene']):
        tags.append('cultural')
    
    return tags


def generate_domains(name: str, definition: str, cultural_note: str) -> List[str]:
    """Generate domains based on term content."""
    domains = []
    content = (name + " " + definition + " " + cultural_note).lower()
    
    if any(word in content for word in ['press', 'pressing', 'manufacturing']):
        domains.append('pressing_technique')
    
    if any(word in content for word in ['master', 'cutting', 'lacquer']):
        domains.append('mastering')
    
    if any(word in content for word in ['quality', 'test', 'grade']):
        domains.append('quality_control')
    
    if any(word in content for word in ['turntable', 'cartridge', 'equipment']):
        domains.append('equipment')
    
    if any(word in content for word in ['dj', 'scratch', 'mix']):
        domains.append('dj_technique')
    
    if any(word in content for word in ['collect', 'market', 'value']):
        domains.append('collecting')
    
    return domains


def generate_equipment_association(name: str, definition: str) -> List[str]:
    """Generate equipment associations based on term content."""
    associations = []
    content = (name + " " + definition).lower()
    
    if any(word in content for word in ['turntable', 'platter', 'deck']):
        associations.append('turntable')
    
    if any(word in content for word in ['tonearm', 'arm']):
        associations.append('tonearm')
    
    if any(word in content for word in ['cartridge', 'pickup']):
        associations.append('cartridge')
    
    if any(word in content for word in ['stylus', 'needle']):
        associations.append('stylus')
    
    if any(word in content for word in ['mixer', 'mix']):
        associations.append('mixer')
    
    if any(word in content for word in ['amplifier', 'amp', 'preamp']):
        associations.append('amplifier')
    
    if any(word in content for word in ['speaker', 'monitor']):
        associations.append('speaker')
    
    return associations


def generate_genre_association(name: str, definition: str, cultural_note: str) -> List[str]:
    """Generate genre associations based on term content."""
    associations = []
    content = (name + " " + definition + " " + cultural_note).lower()
    
    if any(word in content for word in ['hip-hop', 'hip hop', 'rap', 'dj', 'scratch']):
        associations.append('hip_hop')
    
    if any(word in content for word in ['electronic', 'techno', 'house', 'dance']):
        associations.append('electronic')
    
    if any(word in content for word in ['jazz', 'bebop', 'swing']):
        associations.append('jazz')
    
    if any(word in content for word in ['rock', 'pop', 'metal']):
        associations.append('rock')
    
    if any(word in content for word in ['classical', 'orchestral']):
        associations.append('classical')
    
    if not associations:
        associations.append('all')
    
    return associations


def generate_decade(cultural_note: str) -> str:
    """Generate decade based on cultural note."""
    if not cultural_note:
        return ""
    
    content = cultural_note.lower()
    
    if '1940s' in content or '1940' in content:
        return '1940s'
    elif '1950s' in content or '1950' in content:
        return '1950s'
    elif '1960s' in content or '1960' in content:
        return '1960s'
    elif '1970s' in content or '1970' in content:
        return '1970s'
    elif '1980s' in content or '1980' in content:
        return '1980s'
    elif '1990s' in content or '1990' in content:
        return '1990s'
    elif '2000s' in content or '2000' in content:
        return '2000s'
    elif '2010s' in content or '2010' in content:
        return '2010s'
    elif '2020s' in content or '2020' in content:
        return '2020s'
    
    return ""


def create_term_file(term: Term, output_dir: Path) -> None:
    """Create a term file with front-matter and content."""
    # Create letter directory
    letter_dir = output_dir / term.slug[0]
    letter_dir.mkdir(exist_ok=True)
    
    # Create term file
    term_file = letter_dir / f"{term.slug}.md"
    
    # Prepare front-matter
    frontmatter = {
        'term': term.name,
        'slug': term.slug,
        'pos': term.pos,
        'aliases': term.aliases,
        'tags': term.tags,
        'domains': term.domains,
        'regions': term.regions,
        'eras': term.eras,
        'first_attested': term.first_attested,
        'pronunciation': term.pronunciation,
        'see_also': term.see_also,
        'sources': term.sources,
        'summary': term.summary,
        'updated': term.updated,
        'popularity': term.popularity,
        'complexity': term.complexity,
        'status': term.status,
        'context': term.context,
        'verification': term.verification,
        'equipment_association': term.equipment_association,
        'genre_association': term.genre_association,
        'decade': term.decade
    }
    
    # Remove empty fields
    frontmatter = {k: v for k, v in frontmatter.items() if v}
    
    # Write file
    with open(term_file, 'w', encoding='utf-8') as f:
        f.write('---\n')
        yaml.dump(frontmatter, f, default_flow_style=False, allow_unicode=True)
        f.write('---\n\n')
        f.write(f'# {term.name}\n\n')
        
        if term.definition:
            f.write(f'**Definition:** {term.definition}\n\n')
        
        if term.etymology:
            f.write(f'**Etymology:** {term.etymology}\n\n')
        
        if term.example:
            f.write(f'**Example:** {term.example}\n\n')
        
        if term.cultural_note:
            f.write(f'**Cultural Note:** {term.cultural_note}\n\n')


def process_chapter_file(chapter_file: Path, output_dir: Path) -> List[Term]:
    """Process a single chapter file and extract terms."""
    print(f"Processing {chapter_file}...")
    
    with open(chapter_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split content into sections
    sections = re.split(r'\n## ', content)
    
    terms = []
    for i, section in enumerate(sections):
        if i == 0:
            # Skip the chapter header
            continue
        
        # Add back the ## prefix
        section = '## ' + section
        
        term = parse_term_section(section)
        if term:
            terms.append(term)
            create_term_file(term, output_dir)
    
    print(f"  Extracted {len(terms)} terms")
    return terms


def main():
    """Main migration function."""
    # Set up paths
    project_root = Path(__file__).parent.parent
    content_dir = project_root / 'content' / 'books' / 'vinyl-lexicon' / 'chapters'
    output_dir = project_root / 'docs' / 'terms'
    
    # Create output directory
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Process all chapter files
    all_terms = []
    chapter_files = sorted(content_dir.glob('chapter-*.md'))
    
    for chapter_file in chapter_files:
        terms = process_chapter_file(chapter_file, output_dir)
        all_terms.extend(terms)
    
    print(f"\nMigration complete!")
    print(f"Total terms processed: {len(all_terms)}")
    print(f"Output directory: {output_dir}")
    
    # Generate summary
    summary = {
        'total_terms': len(all_terms),
        'migration_date': datetime.now().isoformat(),
        'terms_by_letter': {}
    }
    
    for term in all_terms:
        letter = term.slug[0]
        if letter not in summary['terms_by_letter']:
            summary['terms_by_letter'][letter] = 0
        summary['terms_by_letter'][letter] += 1
    
    # Save summary
    summary_file = output_dir / 'migration_summary.yaml'
    with open(summary_file, 'w') as f:
        yaml.dump(summary, f, default_flow_style=False)
    
    print(f"Migration summary saved to: {summary_file}")


if __name__ == '__main__':
    main()
