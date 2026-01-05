# Changelog

All notable changes to the Waxly project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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
