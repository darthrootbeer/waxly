# Changelog

All notable changes to the Waxly project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [2.1.0] - 2026-01-05

### 🎯 Dictionary-Style Enhancements

Waxly v2.1 transforms the dataset into a comprehensive vinyl terminology dictionary with linguistic metadata and enhanced validation.

### Added

**New Optional Schema Fields:**
- `pos` - Part of speech (noun, verb, adjective, adverb, phrase)
- `pronunciation` - IPA or phonetic notation for pronunciation guidance
- `alt_spellings` - Spelling variations, regional variants, common misspellings (distinct from aliases)
- `etymology` - Historical origin and development of the term
- `first_use` - Year of first known usage (1800-2100)

**Enhanced Validation:**
- Summary must be complete sentence (ends with . ! or ?)
- Summary word count validation (≤25 words)
- Definition word count recommendations (50-300 words)
- Slug length limit (max 50 characters)
- Part of speech enum validation
- First use year range validation (1800-2100)

**Documentation:**
- SCHEMA_ENHANCEMENT_PROPOSAL.md - Design document for v2.1 enhancements
- TODO.md - Prioritized task list for future development
- Updated CONTRIBUTING.md with new field templates and validation examples

### Changed

**Schema Updates:**
- Clarified `aliases` field: now specifically for alternative names (e.g., "acetate" → "lacquer", "reference disc")
- Added `alt_spellings` field: for spelling variations, regional variants, misspellings (e.g., "DJ" → "deejay", "disc jockey")
- Updated `slug` description to clarify "shortest possible, never includes alt terms"
- Updated `summary` description to emphasize "complete sentence, never truncated"
- Added `short_definition` field (deprecated in favor of `summary`)

**Important Distinction:**
- **Aliases** = Different names for the same thing (semantic alternatives)
- **Alt Spellings** = Variations in how the term is written (orthographic alternatives)

**Validation Updates:**
- Enhanced `tools/validate.js` with word count helpers
- Added complete sentence check for summaries
- Added warnings for short definitions (<20 words) and long definitions (>500 words)

**Documentation Updates:**
- Updated README.md to v2.1 with new schema structure
- Enhanced CONTRIBUTING.md with comprehensive examples
- Updated API documentation examples

### Quality Issues Identified

**Current Dataset Status (567 terms):**
- ❌ ~567 summaries missing sentence-ending punctuation
- ⚠️ ~400+ definitions under 50 words (recommend expansion)
- ⚠️ No terms currently have pos, pronunciation, etymology, or first_use metadata

**Note:** These are identified for gradual improvement. v2.1 fields are optional to maintain backward compatibility.

### Roadmap

**High Priority (v2.1):**
- Fix all summaries to be complete sentences
- Expand definitions to 50-300 words (prioritize core terms)
- Add metadata to high-traffic terms

**Medium Priority (v2.2):**
- Scrape Discogs/eBay for missing collector terminology
- Add 100+ missing terms (notch, jacket, ringwear, etc.)
- Complete metadata for all terms

### Migration Notes

**Backward Compatibility:**
- ✅ All new fields are optional
- ✅ Existing term files remain valid
- ✅ No breaking changes to API responses
- ✅ Gradual migration recommended

**Recommended Actions:**
1. Update validation script: `node tools/validate.js`
2. Review validation warnings for your terms
3. Add punctuation to summaries
4. Expand definitions with context and history
5. Add metadata fields when known

---

## [2.0.0] - 2026-01-05

### 🎉 Complete Rebuild - Waxly 2.0

Waxly has been completely re-architected from a documentation site into a canonical, machine-readable vinyl terminology dataset optimized for AI, APIs, and long-term durability.

### Added

**Infrastructure:**
- Canonical JSON dataset format (567 terms)
- Minimal, durable schema (7 required + 4 optional fields)
- Serverless REST API (4 endpoints)
- Custom static site generator (Node.js + Handlebars)
- GitHub Actions CI/CD workflow
- Dataset validation tooling

**API Endpoints:**
- `GET /v1/term/{slug}` - Retrieve single term
- `GET /v1/terms` - List all terms with filtering
- `GET /v1/search?q=` - Full-text search
- `GET /v1/random` - Random term discovery

**Documentation:**
- Fresh README with complete API reference
- CONTRIBUTING.md guide for community contributions
- docs/API.md comprehensive API documentation
- dataset/LICENSE.md (CC BY-SA 4.0)

**Features:**
- Edge-cached API (<100ms response times)
- CORS-enabled for browser access
- Mobile-first responsive design
- A-Z browse functionality
- Tag-based categorization
- Cross-reference linking between terms

### Changed

**Architecture:**
- Switched from Python/MkDocs to Node.js
- Moved from Markdown+YAML to pure JSON
- Changed from site-first to dataset-first design
- Simplified schema from 952 lines to 65 lines
- Reduced from 40+ optional fields to 4

**Technology Stack:**
- **From:** Python + MkDocs + Material theme
- **To:** Node.js + Handlebars + Vercel

**Repository Structure:**
- **From:** `docs/`, `scripts/`, `schema/`, `site/`, `venv/`
- **To:** `dataset/`, `api/`, `site/`, `tools/`

### Removed

**Legacy Infrastructure:**
- Entire MkDocs documentation system
- 27 Python scripts (replaced with 3 Node.js scripts)
- 952-line bloated schema
- Python virtual environment
- Pre-commit hooks (Python-based)

**Generated Bloat (7.3MB):**
- JSON-LD semantic web files (475 files, 2.5MB)
- Markdown export duplicates (476 files, 2.8MB)
- Manual redirect files (348 files, 2.0MB)

**Configuration Files:**
- mkdocs.yml
- requirements.txt
- .pre-commit-config.yaml
- .markdownlint.json

**Speculative Features:**
- AI metadata fields
- Market pricing data
- Translation support (8 languages)
- Media attachments
- Cultural sensitivity system
- User ratings
- Discussion forums
- Knowledge graph relationships

**Documentation:**
- 14 legacy documentation files
- Fantasy roadmap (TODO.md with AI/ML plans)

### Performance

**Repository Size:**
- Before: ~120MB
- After: ~69MB
- Reduction: 43%

**File Count:**
- Before: ~5,700 files
- After: ~1,420 files
- Reduction: 75%

**Complexity:**
- Schema: 93% reduction (952 → 65 lines)
- Scripts: 89% reduction (27 → 3 files)
- Directories: 70% reduction (30+ → 9)

### Migration Notes

**Breaking Changes:**
- Complete API redesign (no backward compatibility with v1.x)
- New URL structure for terms
- Different data format (JSON instead of Markdown)

**Data Preservation:**
- All 567 term definitions preserved
- Content quality maintained
- Cross-references intact

**Archive:**
- Legacy v1.x code preserved in `archive/waxly-1.0` Git branch

---

## [1.x] - 2024-2025

### Legacy Version (Archived)

- MkDocs-based documentation site
- Python build system
- 568 terms in Markdown+YAML format
- Material for MkDocs theme
- Pagefind search integration
- GitHub Pages deployment

**Status:** Archived (see `archive/waxly-1.0` branch)

---

## Future Roadmap

### Planned for 2.1.0
- Enhanced search (fuzzy matching, relevance scoring)
- Bulk export formats (CSV, SQLite)
- API rate limiting (if needed)
- Performance optimizations

### Under Consideration
- GraphQL API endpoint
- Multilingual support (community-driven)
- Audio pronunciation files (optional)
- Historical timeline visualization

### Not Planned
- User accounts or authentication
- Social features (likes, comments)
- Monetization or paid tiers
- Content management UI (Git-based workflow only)

---

## Versioning Strategy

**Major versions (X.0.0):**
- Breaking API changes
- Major architectural changes
- Schema breaking changes

**Minor versions (2.X.0):**
- New API endpoints
- New features
- Schema additions (backward compatible)

**Patch versions (2.0.X):**
- Bug fixes
- Performance improvements
- Documentation updates

---

## Links

- **Repository:** https://github.com/waxly/waxly
- **API Docs:** https://github.com/waxly/waxly/blob/main/docs/API.md
- **License:** CC BY-SA 4.0 (dataset) / MIT (code)

---

**Waxly - The Language of Vinyl, Defined**
