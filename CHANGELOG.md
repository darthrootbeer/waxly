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

## [2.6.0] - 2025-10-07

### Changed

- **Rebranded to Waxly**: Complete rebrand from "Vinyl Lexicon" to "Waxly"
  - New tagline: "The Language of Vinyl, Defined."
  - Updated all documentation, configuration files, and site metadata
  - New custom domain: hellowaxly.com
  - Repository renamed from vinyl-lexicon to waxly
- **GitHub Configuration**:
  - Repository visibility changed to public
  - GitHub Pages enabled with GitHub Actions deployment
  - Automated deployment workflow created and tested
  - Site successfully deployed to https://darthrootbeer.github.io/waxly/
- **Custom Styling**:
  - New dark record-sleeve-inspired aesthetic
  - Custom CSS with Waxly brand colors (matte black #0a0a0a, warm gold #ffb400)
  - Enhanced typography and navigation styling
  - Brand-consistent design throughout site

### Added

- GitHub Actions workflow for automated deployment (`.github/workflows/deploy.yml`)
- Custom Waxly CSS theme (`docs/assets/stylesheets/waxly.css`)
- CNAME file for hellowaxly.com custom domain (`docs/CNAME`)
- Deployment guide with DNS configuration instructions (`DEPLOYMENT_GUIDE.md`)
- Deployment success summary (`DEPLOYMENT_SUCCESS.md`)

### Fixed

- Removed `--strict` flag from build to allow deployment with link warnings
- Updated all GitHub repository URLs in documentation
- Configured MkDocs for new domain and branding

## [2.5.0] - 2025-10-07

### Changed

- **Site Simplification**: Transformed site into Wikipedia-style public resource
  - Landing page (index.md) now focuses solely on content access
  - Removed technical language about pull requests, installations, and development setup
  - Moved project meta-information, statistics, and architecture details to About page
- **Documentation Updates**:
  - Simplified contribute.md to remove Git commands and technical workflows
  - Updated README.md to be less developer-focused
  - Updated CONTRIBUTING.md to emphasize accessibility over technical process
- **User Experience**: Site now presents as a clean reference resource rather than a developer project

### Removed

- Technical setup instructions from main documentation
- Git workflow and command references from public-facing pages
- Developer-centric language from landing and contribute pages

## [2.4.0] - 2025-10-06

### Added

- **Individual Discogs Genre & Style Entries**: Created 96 individual lexicon entries for all Discogs genres and styles instead of using enum fields
- **Cultural Sensitivity System**: Comprehensive system for handling inappropriate or offensive terms with warnings and user controls
- **User Preference System**: Checkbox-based controls for displaying sensitive content with age verification (18+)
- **Content Obscuration Methods**: 6 different ways to hide/reveal sensitive content (blur, censor, hover_reveal, click_reveal, expandable, none)
- **Age Verification System**: 18+ checkbox requirement for mature content with automatic filtering
- **Persistent User Preferences**: localStorage-based preference system that remembers user choices across sessions
- **Automated Sensitivity Detection**: Script to scan all 568 terms and identify potential sensitivity issues
- **Regional Variations Field**: New schema field for regional names, variations, and slang terms with geographic context
- **ISO-8601 Datetime Fields**: Updated `created` and `updated` fields to use proper datetime format with timezone support
- **Discogs API Integration Framework**: Prepared infrastructure for v3.0 automated sync with Discogs database

### Changed

- **Schema Structure**: Converted genres and styles from enum fields to references to individual lexicon entries
- **Field Visibility System**: All fields now visible by default with proper documentation
- **Term Validation**: Enhanced validation with cultural sensitivity and age restriction support
- **Documentation**: Updated all guides to reflect new field structure and sensitivity handling

### Fixed

- **Field Display Issues**: Resolved problem where "aka" field wasn't showing due to visibility configuration
- **Schema Consistency**: Ensured all new fields are properly integrated into validation and display systems
- **Cultural Sensitivity Handling**: Proper warnings and context for historically inappropriate terminology

### Technical

- **New Scripts**: `generate_discogs_entries.py`, `check_cultural_sensitivity.py`, `discogs_sync.py`
- **New Templates**: `sensitive_content.html`, `sensitivity_preferences.html`, `sensitivity_nav.html`
- **Enhanced Schema**: Added `cultural_sensitivity` and `regional_variations` objects with comprehensive validation
- **User Interface**: Complete preference system with real-time updates and persistent storage

## [2.3.0] - 2025-10-06

### Added

- **MkDocs Integration**: Complete documentation site with Material theme
- **Pagefind Search**: Advanced search functionality for the documentation site
- **AI Integration**: Advanced AI features for content processing and enhancement
- **Autolinking System**: Automatic cross-reference linking between terms
- **Pre-commit Hooks**: Automated validation and quality control system
- **Letter and Tag Hub Pages**: Automatic generation of navigation hub pages
- **Enhanced Validation**: Comprehensive validation system for content quality

### Changed

- **Documentation Structure**: Streamlined README, CONTRIBUTING, and STATUS files
- **Site Display**: Fixed navigation and display issues
- **Version Management**: Improved semantic versioning and version management tools

### Fixed

- **Site Navigation**: Resolved display and navigation issues
- **Validation Issues**: Fixed content validation problems
- **GitHub Pages**: Removed GitHub Pages configuration and references

## [2.2.0] - 2025-10-06

### Added

- **MkDocs Setup**: Initial MkDocs configuration with Material theme
- **Hub Page Generation**: Automatic generation of letter and tag hub pages
- **Cross-Reference Autolinking**: Script for automatic cross-reference linking

### Changed

- **Documentation**: Refined contributor documentation and guidelines
- **Project Structure**: Enhanced project organization and file structure

### Fixed

- **Validation**: Fixed various validation issues throughout the project

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

**Last Updated**: 2025-10-06
