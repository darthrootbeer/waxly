# Changelog

All notable changes to the Vinyl Lexicon Project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Planned

- Complete migration from book format to wiki-style database
- 500+ individual term files with rich metadata
- Advanced search and filtering capabilities
- Community contribution workflow
- Record label database with parent/subsidiary relationships
- Mobile app version

## [2.1.0] - 2025-10-06

### Added

- **Enhanced Schema**: Added 8 new advanced metadata field groups:
  - `technical_specs` - Physical dimensions, materials, manufacturing details
  - `historical_timeline` - Introduction year, peak/decline eras, notable examples
  - `cultural_impact` - Collector value, rarity, condition sensitivity, preservation
  - `relationships` - Parent/child concepts, requires/enables/conflicts relationships
  - `usage_context` - Use cases, best practices, avoid-when scenarios
  - `quality_indicators` - Grading factors, common defects, restoration info
  - `market_data` - Price premium, demand, investment potential
  - `advanced_search` - Keywords, related artists, related labels
- **Discogs Integration**: Implemented Discogs genre/style taxonomy with 16 official genres
- **Field Visibility System**: Global defaults with per-term overrides for clean UX
- **Media Implementation Guide**: Comprehensive guide for image and media assets
- **`aka` Field**: New field for storing alternate terms (e.g., "Groove Banding" for "Banding")

### Changed

- **Clean URLs**: Removed descriptive suffixes from slugs (e.g., `auxiliary-weight-dj-slang-slug` → `auxiliary-weight`)
- **Term Names**: Cleaned 270 terms with alternate names in titles (e.g., "Banding (Groove Banding)" → "Banding")
- **Schema Structure**: Enhanced with comprehensive metadata fields for rich content
- **File Organization**: Removed duplicate backup files and legacy content (~25MB saved)

### Fixed

- **Slug Consistency**: All slugs now contain only primary term names
- **Alternate Terms**: Moved from titles to dedicated `aka` field
- **File Structure**: Removed cruft and duplicate files from project
- **Cross-References**: Updated redirects for cleaned up slugs

### Removed

- **Legacy Files**: Removed 4 duplicate backup files (vinyl_lexicon*.md)
- **Old Structure**: Removed legacy content/books/ directory
- **Empty Directories**: Cleaned up unused docs/images/, docs/letters/, docs/tags/
- **Legacy HTML**: Removed old index.html (replaced by MkDocs)

## [2.0.0] - 2025-01-27

### Added

- **MAJOR RESTRUCTURING**: Wiki-style database architecture
- Comprehensive restructuring plan with 25+ metadata fields per term
- New directory structure: `docs/`, `data/`, `scripts/`, `schema/`, `api/`
- Rich term schema with popularity, complexity, regional variations
- Advanced metadata fields: equipment association, genre association, cultural significance
- Quality control fields: verification status, contributor attribution, discussion threads
- Multilingual support framework with translation fields
- API-ready JSON export structure

### Changed

- **Architecture**: From book/chapter model to one-term-per-file structure
- **Searchability**: Enhanced with rich metadata and cross-references
- **Scalability**: Designed for thousands of terms with performance optimization
- **Community Features**: Built-in contribution workflow and quality control
- **Documentation**: Updated to reflect new wiki-style architecture

### Planned Migration

- Convert 500+ terms from 24 chapters to individual files
- Generate automated navigation hubs (letters, tags)
- Implement validation schemas and quality control
- Deploy with MkDocs + Pagefind search (local development only)

## [1.0.0] - 2025-01-27 (Initial Release)

### Added

- Initial project structure based on OA-MD best practices
- Complete vinyl lexicon content with A-Z organization (500+ terms)
- Professional documentation structure
- Assets directory for web presentation materials
- Tools directory for content processing utilities
- Chapter-based organization for better navigation

### Changed

- Restructured from simple markdown files to organized book format
- Implemented chapter-based organization for better navigation

---

**Last Updated**: 2025-01-27
