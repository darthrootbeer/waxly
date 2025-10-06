# Vinyl Lexicon - TODO

## Current Tasks

### MVP Phase - Week 1 (Priority 1)

- [ ] `000008` - **RESTRUCTURE PROJECT**: Migrate from book/chapter model to wiki-style database architecture
- [ ] `000009` - Create new repo structure: `data/`, `docs/`, `scripts/`, `schema/`, `api/` directories
- [ ] `000010` - Implement one-term-per-file structure with rich front-matter metadata
- [x] `000011` - Create term validation schema and data integrity system - (2025-10-06_15.30.00)
- [x] `00002A` - Extend schema with advanced metadata fields (technical specs, historical timeline, cultural impact, relationships, usage context, quality indicators, market data, advanced search) - (2025-10-06_15.30.00)
- [x] `00002B` - Create field visibility system with global defaults and per-term overrides - (2025-10-06_15.30.00)
- [x] `00002C` - Implement Discogs genre/style taxonomy (Genre > Style hierarchy, 16 official genres, 1-3 genres per term, 1-6 styles per term) - (2025-10-06_15.45.00)
- [ ] `000012` - Set up MkDocs with Material theme and Pagefind search
- [ ] `000013` - Deploy to GitHub Pages with CI/CD pipeline

### Phase 2 - Content Migration

- [ ] `000014` - Split remaining letters into one-term-per-file structure
- [ ] `000015` - Run validator to fill missing front-matter
- [ ] `000016` - Generate letter and tag hubs automatically
- [ ] `000017` - Implement autolinking script for cross-references

### Phase 3 - Contributor Experience

- [ ] `000018` - Refine contributor documentation
- [ ] `000019` - Add pre-commit hooks and validations
- [ ] `000020` - Set up aliases → redirects system
- [ ] `000021` - Add related-terms sidebar

### Phase 4 - Advanced Features

- [ ] `000022` - Expose JSON export of all terms (/api/terms.json)
- [ ] `000023` - Add pronunciation audio support
- [ ] `000024` - Improve filtering UI (by tags / eras / regions)
- [ ] `000084` - Create Discogs genre/style reference system: Map each genre and style to official Discogs URLs (e.g., /genre/rock, /style/krautrock)
- [ ] `000085` - Investigate Discogs API integration for pulling canonical genre/style descriptions and metadata
- [ ] `000086` - Implement genre/style pages in lexicon that link to and reference Discogs as authoritative source
- [ ] `000087` - Add "discogs_genre_url" and "discogs_style_urls" fields to schema for storing canonical Discogs references

### Infrastructure & Setup

- [ ] `000025` - Write schema and validator for term front-matter
- [ ] `000026` - Build importer to split current A-Z markdown into term files
- [ ] `000027` - Set up contribution guidelines & issue templates
- [ ] `000028` - Create autolink + redirect scripts
- [ ] `000029` - Add validations and pre-commit hooks
- [ ] `000030` - Migrate full content and generate letter/tag hubs
- [ ] `000031` - Plan JSON API export and pronunciation audio
- [ ] `000032` - Implement comprehensive tagging system for terms (DJ-related, compact disc, 1960s era, etc.)
- [ ] `000033` - Add term popularity field (1-10 scale) to track current usage vs historical terms
- [ ] `000034` - Implement regional terminology field to track geographic variations (East Coast US, Italy, England, etc.)
- [ ] `000035` - Add term complexity level field (beginner/intermediate/advanced/expert) for user skill-based filtering
- [ ] `000036` - Implement term frequency field (rare/common/ubiquitous) to indicate how often term appears in literature/media
- [ ] `000037` - Add term status field (active/archaic/obsolete/revived) to track term lifecycle
- [ ] `000038` - Create term context field (formal/informal/slang/technical/jargon) for usage style classification
- [ ] `000039` - Add term source field (oral tradition/written documentation/industry standard/internet) for origin tracking
- [ ] `000040` - Implement term verification field (verified/unverified/contested/needs_research) for accuracy tracking
- [ ] `000041` - Add term cross-references field (synonyms/antonyms/related_terms/see_also) for comprehensive linking
- [ ] `000042` - Create term examples field (usage_examples/context_examples/quote_examples) for practical understanding
- [ ] `000043` - Add term etymology field (word_origin/language_root/historical_development) for linguistic context
- [ ] `000044` - Implement term pronunciation field (phonetic_spelling/audio_file/regional_variations) for correct usage
- [ ] `000045` - Add term cultural significance field (importance_level/cultural_impact/historical_relevance) for context
- [ ] `000046` - Create term equipment association field (turntables/mixers/records/accessories) for gear-specific terms
- [ ] `000047` - Add term genre association field (hip_hop/electronic/jazz/rock/etc) for music-specific terminology
- [ ] `000048` - Implement term decade field (1940s/1950s/1960s/etc) for historical period classification
- [ ] `000049` - Add term user rating field (1-5 stars) for community quality assessment
- [ ] `000050` - Create term last_updated field (timestamp) for content freshness tracking
- [ ] `000051` - Add term contributor field (author/editor/reviewer) for attribution and quality control
- [ ] `000052` - Implement term discussion field (comments/notes/controversies) for community input
- [ ] `000053` - Add term media field (images/videos/audio_clips/diagrams) for multimedia content
- [ ] `000054` - Create term bibliography field (sources/references/citations) for academic rigor
- [ ] `000055` - Add term translation field (translations/equivalents) for multilingual support
- [ ] `000056` - Implement term usage notes field (warnings/cautions/important_info) for practical guidance

## Completed Tasks

- [x] `000001` - Create project structure mirroring OA-MD best practices with content/, assets/, tools/, and documentation directories - (2025-01-27_14.30.00)
- [x] `000002` - Set up standard project documentation files (README.md, CHANGELOG.md, LICENSE, CONTRIBUTING.md, TODO.md) - (2025-01-27_14.35.00)
- [x] `000003` - Organize vinyl lexicon content into structured book format with chapters - (2025-01-27_14.40.00)
- [x] `000004` - Create assets directory with styles, fonts, and images for web presentation - (2025-01-27_14.45.00)
- [x] `000005` - Set up tools directory for content processing and conversion utilities - (2025-01-27_14.50.00)
- [x] `000006` - Initialize Git repository and configure for GitHub hosting - (2025-01-27_14.55.00)
- [x] `000007` - Create web presentation layer for digital book experience - (2025-01-27_15.00.00)

## Future Enhancements

### UX & Interface Improvements

- [ ] `000057` - Dark/light theme toggle
- [ ] `000058` - Permalinks with stable slugs
- [ ] `000059` - Related-terms card per entry
- [ ] `000060` - Faceted search for tags/domains/eras
- [ ] `000061` - Copy-code buttons for technical terms

### Content Expansions

- [ ] `000062` - Add more detailed technical specifications for equipment terms
- [ ] `000063` - Expand cultural context and historical notes
- [ ] `000064` - Include audio examples where relevant

### Major Spin-off Project: Record Label Universe

- [ ] `000065` - Create comprehensive record label database (Capitol, Columbia, independent labels, etc.)
- [ ] `000066` - Design interactive, zoomable map interface for record label relationships
- [ ] `000067` - Implement parent/subsidiary label relationship mapping
- [ ] `000068` - Add label timeline and historical evolution tracking
- [ ] `000069` - Create contribution system for community label submissions
- [ ] `000070` - Build search and filtering system for label discovery
- [ ] `000071` - Implement label relationship visualization (mergers, acquisitions, splits)
- [ ] `000072` - Add label geographic distribution mapping
- [ ] `000073` - Create label genre and artist association system
- [ ] `000074` - Develop label discography integration
- [ ] `000075` - Plan separate repository and hosting for Record Label Universe project

### Community & Governance

- [ ] `000076` - Set up small council with clear dispute-resolution policy
- [ ] `000077` - Add community discussion forums
- [ ] `000078` - Create contributor onboarding guide
- [ ] `000079` - Document deployment and hosting procedures

### Advanced Features

- [ ] `000080` - Add bookmarking and favorites functionality
- [ ] `000081` - Create mobile app version
- [ ] `000082` - Add social sharing capabilities
- [ ] `000083` - Implement automated testing for content quality

## Project Overview

**Goal**: Create a free, mobile-friendly, desktop-friendly, blazing-fast digital A-Z reference for vinyl record culture and terminology, suitable for GitHub Pages now and easily expandable into a wiki-like community resource later.

**Chosen Stack**: Static site built from Markdown with Material-for-MkDocs + Pagefind search hosted on GitHub Pages

**Key Benefits**:

- Free, serverless, very fast to load
- Great responsive UX out of the box
- Search is pre-built and instant
- Good for version control and PR-based contributions
- Scales to thousands of entries without performance loss

## 🏗️ MAJOR RESTRUCTURING: From Book to Wiki Database

**Current Problem**: The project is structured as a traditional book with chapters, which limits extensibility and searchability.

**New Architecture**: Wiki-style database with one-term-per-file structure and rich metadata.

### New Repository Structure

```text
vinyl-lexicon/
├── docs/                          # MkDocs content directory
│   ├── index.md                   # Homepage
│   ├── about.md                   # About page
│   ├── contribute.md              # Contribution guidelines
│   ├── terms/                     # Individual term files
│   │   ├── a/
│   │   │   ├── a-b-test-press.md
│   │   │   ├── acetate.md
│   │   │   └── acoustic-suspension.md
│   │   ├── b/
│   │   └── ...
│   ├── letters/                   # Auto-generated letter hubs
│   │   ├── a.md
│   │   ├── b.md
│   │   └── ...
│   ├── tags/                      # Auto-generated tag hubs
│   │   ├── equipment.md
│   │   ├── dj-related.md
│   │   └── ...
│   ├── images/                    # Media assets
│   └── data/                      # Structured data
│       ├── taxonomy.yml           # Controlled vocabulary
│       ├── aliases.yml            # Term aliases
│       └── redirects.yml          # URL redirects
├── scripts/                       # Processing tools
│   ├── split_from_letter_md.py    # Convert chapters to terms
│   ├── validate_frontmatter.py    # Validate term metadata
│   ├── build_letter_indexes.py    # Generate letter hubs
│   └── check_links.sh             # Link validation
├── schema/                        # Data validation
│   └── term.schema.json           # Term front-matter schema
├── api/                           # JSON API endpoints
│   └── terms.json                 # All terms as JSON
├── mkdocs.yml                     # MkDocs configuration
├── .github/workflows/gh-pages.yml # CI/CD pipeline
└── .pre-commit-config.yaml        # Pre-commit hooks
```

### Term File Structure

Each term file (`docs/terms/a/acetate.md`) contains:

```yaml
---
term: "Acetate"
slug: "acetate"
pos: "noun"
aliases: ["lacquer", "reference disc"]
tags: ["equipment", "pressing", "mastering"]
domains: ["pressing_technique", "mastering"]
regions: ["US", "UK", "JA"]
eras: ["1940s", "1950s", "1960s"]
first_attested: "1940s"
pronunciation: "/ˈæsɪteɪt/"
see_also: ["dubplate", "lacquer cut", "reference disc"]
sources:
  - label: "Audio Engineering Society"
    url: "https://example.com"
summary: "A soft lacquer-coated aluminum disc used to cut the first playable copy"
updated: "2025-01-27"
popularity: 7
complexity: "intermediate"
status: "active"
context: "technical"
verification: "verified"
---

# Acetate

**Definition:** A soft lacquer-coated aluminum (or occasionally glass) disc used to cut the very first playable copy of a recording straight from the mastering lathe.

**Etymology:** Named for the nitrocellulose acetate lacquer layer applied over the disc's base.

**Example:** "I scored an acetate of a lost 1972 soul demo — the paper label is handwritten in ballpoint."

**Cultural Note:** In the '50s and '60s, DJs prized acetates for breaking brand-new singles in clubs before commercial pressings existed.
```

### Key Advantages of New Structure

1. **Maximum Searchability**: Each term is individually indexed and searchable
2. **Rich Metadata**: 25+ fields per term for comprehensive categorization
3. **Scalability**: Easy to add new terms without restructuring
4. **API-Ready**: JSON export for external integrations
5. **Community-Friendly**: Clear contribution workflow with validation
6. **Future-Proof**: Extensible architecture for new features

**Licenses**: Content (CC-BY-SA 4.0), Code (MIT)

---

**Last Updated**: 2025-01-27
