# Waxly 2.0 Architecture Proposal

**Date:** 2026-01-05
**Status:** Planning Phase
**Purpose:** Transform Waxly from a documentation site into durable vinyl knowledge infrastructure

---

## Executive Summary

This document proposes a **clean-slate rebuild** of Waxly into a canonical, machine-readable vinyl lexicon optimized for AI agents, APIs, and 10-20 year durability.

**Approach:** Extract term content from current system → Build Waxly 2.0 fresh → Replace old site

**What We Keep:**
- 568 term definitions (content only)

**What We Discard:**
- All legacy infrastructure (MkDocs, Python scripts, bloated schema)
- All generated artifacts (7.3MB of JSON-LD, exports, redirects)
- All documentation (rewrite fresh for 2.0)

**Timeline:** 11 working days (2 weeks with buffer)

**Core Principle:** One canonical dataset → All other outputs derive from it

**Result:** 90% smaller codebase, 100% of functionality, infinite% more durable

---

## Phase 1: Current State Analysis

### Repository Structure (As-Is)

```
vinyl-lexicon/
├── docs/
│   ├── terms/{a-z}/{slug}.md      # 568 term files (2.2MB) - THE CONTENT
│   ├── letters/*.md               # Auto-generated A-Z navigation (120KB)
│   ├── tags/*.md                  # Auto-generated tag pages (48KB)
│   ├── jsonld/                    # 475 files, 2.5MB - BLOAT (unused)
│   ├── markdown-export/           # 476 files, 2.8MB - BLOAT (duplicate)
│   ├── redirects/                 # 348 files, 2.0MB - BLOAT (redundant)
│   └── [index, about, contribute] # Static pages
├── scripts/                       # 27 Python scripts - EXCESSIVE
├── schema/term.schema.json        # 952 lines - BLOATED (should be ~50)
├── api/terms.json                 # API export (INCOMPLETE - only 1 term)
├── site/                          # 47MB MkDocs build output
├── mkdocs.yml                     # MkDocs configuration
├── .pre-commit-config.yaml        # Pre-commit hooks
├── .github/workflows/deploy.yml   # GitHub Pages deployment
└── [README, TODO, docs]           # 10+ documentation files
```

### Content Format

**Term File Example:** `docs/terms/a/acetate.md`

```yaml
---
complexity: intermediate
context: technical
domains: [pressing_technique, mastering, dj_technique]
popularity: 5
pos: noun
regions: [US]
see_also: [dubplate, lacquer-cut, reference-disc]
slug: acetate
status: active
summary: "A soft lacquer-coated aluminum disc..."
tags: [dj-related, pressing, cultural]
term: Acetate
updated: '2025-10-06'
verification: unverified
genres: [Hip Hop]
---

# Acetate

**Definition:** A soft lacquer-coated aluminum (or occasionally glass) disc...

**Etymology:** Named for the nitrocellulose acetate lacquer layer...

**Example:** "I scored an acetate of a lost 1972 soul demo..."

**Cultural Note:** In the '50s and '60s, DJs prized acetates...
```

### Technology Stack

- **Generator:** MkDocs + Material theme
- **Validation:** JSON Schema (term.schema.json)
- **Automation:** Pre-commit hooks (fix, validate, regenerate, autolink)
- **Deployment:** GitHub Actions → GitHub Pages
- **Search:** MkDocs Material search + Pagefind
- **API:** JSON export (incomplete)

### Critical Issues Identified

#### 1. Schema Bloat (952 lines → should be ~50)

**Unused/Speculative Fields:**
- `ai_metadata` - ML learning objectives (zero usage)
- `market_data` - Price premiums, investment potential (not a pricing guide)
- `quality_indicators` - Grading factors (not a grading system)
- `translation` - 8 languages defined (zero translations)
- `media` - Images/audio/video support (no media system)
- `bibliography` - Academic citations (not academic)
- `cultural_sensitivity` - Age restrictions, blur/censor system (zero sensitive content)
- `discussion` - Forum features (not a forum)
- `user_rating` - Rating system (doesn't exist)
- `contributor` - Authorship tracking (not used)
- `relationships` - Parent/child/requires/enables graph (over-engineered)

**Redundant/Overlapping Fields:**
- `aliases` vs `aka` - Same concept, two fields
- `tags` vs `domains` - Redundant taxonomies
- `eras` array vs `decade` string vs `first_attested` - Three time representations
- `status`, `context`, `verification` - Three categorical fields, one sufficient

**Result:** 85% complexity, 0% user-facing value

#### 2. Script Redundancy (27 files → should be ~4)

**Overlapping Scripts:**
- 5 "fix" scripts: `fix_terms.py`, `fix_validation_issues.py`, `fix_alternate_terms.py`, `fix_cross_reference_links.py`, `fix_remaining_issues.py`
- 3 redirect scripts: `generate_redirects.py`, `generate_aliases_redirects.py`, `update_redirects.py`
- 3 discogs scripts: `discogs_sync.py`, `generate_discogs_entries.py`, `generate_discogs_references.py` (incomplete integration)

**Dead Code:**
- `generate_json_ld.py` - Creates 475 JSON-LD files (2.5MB) for semantic web (zero consumers)
- `copy_as_markdown.py` - Creates 476 markdown exports (2.8MB) duplicating source
- `check_cultural_sensitivity.py` - Checks unused schema fields
- `check_todos.py` - Wrapper for grep
- `cleanup_slugs.py`, `migrate_chapters.py` - One-time migrations
- `contributor_setup.py` - Duplicates README instructions
- `version.py` - Script for simple file edit

#### 3. Generated Artifact Bloat (7.3MB)

- `docs/jsonld/` - 2.5MB semantic web files (no consumers)
- `docs/markdown-export/` - 2.8MB duplicate exports (unclear purpose)
- `docs/redirects/` - 2.0MB hand-generated redirects (MkDocs plugin handles this)

#### 4. Fantasy Roadmap

`TODO.md` contains 100+ items including:
- "Phase 5 - AI & Machine Learning Integration"
- Vector databases, embeddings, semantic search
- 8-language translation support
- Multimedia attachments (images, audio, video)
- User ratings and discussion forums
- Market pricing data

**None of this aligns with "infrastructure, not product"**

#### 5. Architectural Misalignment

**Current:** Website-first architecture
- Content embedded in MkDocs structure
- Site generation is the primary output
- No true API (incomplete JSON export)
- Content duplicated across formats

**Needed:** Dataset-first architecture
- Canonical dataset as single source of truth
- All outputs derived from dataset
- API as first-class citizen
- Website as one view of many

---

## Phase 2: Waxly 2.0 Vision (Restated)

### What Waxly 2.0 Is

**Waxly is infrastructure, not a product.**

- A **single source of truth** vinyl terminology dataset
- **Canonical, open, machine-readable** knowledge corpus
- Designed for **LLM ingestion, agent querying, API consumption**
- **Durable over decades** (plain text, versioned, auditable)
- **Publicly readable, copyable, forkable** (explicit open license)
- **Low operational complexity** (no databases, no custom backends, serverless/static)

### What Waxly 2.0 Is Not

- Not a CMS or content management system
- Not a forum or community platform
- Not a market pricing guide
- Not a multimedia encyclopedia
- Not a semantic web knowledge graph
- Not an AI training startup

### Primary Goals (Priority Order)

1. **Single Source of Truth**
   - One canonical dataset, all outputs derived
   - Stored in plain text, versioned via Git
   - No duplication of "truth" across layers

2. **Machine-First Compatibility**
   - Optimized for LLM ingestion
   - Agent queryable via API
   - Clear structure, predictable fields, explicit semantics

3. **Open & Free**
   - Publicly readable, no authentication
   - Explicit open license suitable for AI training
   - Designed to be mirrored, forked, archived

4. **Low Operational Complexity**
   - No databases for core functionality
   - No custom backend services
   - Serverless/static wherever possible
   - Minimal long-term maintenance

5. **Human Readability (Secondary)**
   - Simple static site generated from dataset
   - Clean, fast, readable term pages
   - Uses dataset/API as input layer

### Success Metrics

- **Dataset integrity:** 100% valid, versioned, auditable
- **API reliability:** 99.9% uptime, <100ms response
- **Longevity:** Still usable in 10-20 years without changes
- **Reusability:** Other projects can fork/integrate easily
- **Maintenance:** <1 hour/week operational burden

---

## Phase 3: Proposed Waxly 2.0 Structure

### Directory Architecture

```
waxly/
├── dataset/                        # THE CANONICAL SOURCE OF TRUTH
│   ├── terms/
│   │   ├── {slug}.json            # One JSON file per term (568 files)
│   │   └── index.json             # Index of all terms (metadata only)
│   ├── schema/
│   │   ├── term.schema.json       # Minimal term schema (~50 lines)
│   │   └── SCHEMA.md              # Schema documentation
│   ├── LICENSE.md                 # Explicit open license (CC0 or CC-BY-SA)
│   └── CHANGELOG.md               # Versioned dataset changelog
│
├── api/                            # STATELESS READ-ONLY API
│   ├── functions/
│   │   ├── get-term.js            # Serverless function: GET /api/term/{slug}
│   │   ├── list-terms.js          # Serverless function: GET /api/terms
│   │   └── search.js              # Serverless function: GET /api/search?q=
│   ├── package.json               # API dependencies
│   └── README.md                  # API documentation
│
├── site/                           # STATIC HUMAN-READABLE SITE (DERIVED)
│   ├── src/
│   │   ├── templates/             # HTML templates
│   │   ├── styles/                # CSS
│   │   └── scripts/               # Minimal client-side JS
│   ├── build/                     # Generated static site output
│   ├── generator.js               # Static site generator script
│   └── package.json               # Site dependencies
│
├── tools/                          # TOOLING & SCRIPTS
│   ├── validate.js                # Validate dataset against schema
│   ├── migrate.js                 # Migration script (current → dataset/)
│   └── export.js                  # Export utilities (CSV, etc.)
│
├── docs/                           # PROJECT DOCUMENTATION
│   ├── ARCHITECTURE.md            # This document
│   ├── CONTRIBUTING.md            # Contribution guidelines
│   ├── API.md                     # API reference documentation
│   └── SCHEMA.md                  # Dataset schema specification
│
├── .github/
│   ├── workflows/
│   │   ├── validate.yml           # CI: Validate on PR
│   │   ├── deploy-api.yml         # CD: Deploy API to serverless
│   │   └── deploy-site.yml        # CD: Deploy site to static host
│   └── ISSUE_TEMPLATE/            # Issue templates
│
├── README.md                       # Project overview
└── package.json                    # Root project config

```

### Key Architectural Decisions

#### Decision 1: JSON over Markdown+YAML

**Why:**
- JSON is universally parseable (every language, every tool)
- No front-matter parsing complexity
- Native support in databases, APIs, LLMs
- Easier validation and transformation
- Still human-readable with proper formatting

**Migration Path:**
- Convert `docs/terms/{letter}/{slug}.md` → `dataset/terms/{slug}.json`
- Extract YAML front-matter → JSON metadata
- Convert Markdown body → structured `content` object

**Example Term JSON:**

```json
{
  "slug": "acetate",
  "term": "Acetate",
  "aliases": ["lacquer", "reference disc", "cutting disc"],
  "summary": "A soft lacquer-coated aluminum disc used to cut the first playable copy of a recording.",
  "definition": "A soft lacquer-coated aluminum (or occasionally glass) disc used to cut the very first playable copy of a recording straight from the mastering lathe. Acetates wear out fast — maybe 10–20 plays — but capture the freshest, most dynamic version of a track.",
  "content": {
    "etymology": "Named for the nitrocellulose acetate lacquer layer applied over the disc's base.",
    "example": "I scored an acetate of a lost 1972 soul demo — the paper label is handwritten in ballpoint.",
    "cultural_note": "In the '50s and '60s, DJs prized acetates for breaking brand-new singles in clubs before commercial pressings existed. Jamaican sound-system culture still calls them dubplates."
  },
  "tags": ["dj-related", "pressing", "cultural"],
  "regions": ["US", "UK", "JA"],
  "see_also": ["dubplate", "lacquer-cut", "reference-disc"],
  "created": "2024-10-01",
  "updated": "2025-10-06"
}
```

#### Decision 2: Serverless API over Static JSON Files

**Why:**
- Enables query capabilities (search, filter)
- Can add caching, rate limiting, analytics
- Still stateless (reads from dataset/, no database)
- Free-tier friendly (Vercel, Netlify, Cloudflare Workers)
- Scales automatically

**API Endpoints:**

```
GET /api/term/{slug}         # Get single term by slug
GET /api/terms               # List all terms (index only)
GET /api/search?q={query}    # Search terms
GET /api/tags                # List all tags
GET /api/tags/{tag}          # Get terms by tag
GET /api/random              # Get random term
```

**Technology Options:**
- **Vercel Serverless Functions** (recommended: free tier, zero config)
- **Netlify Functions** (alternative: similar capabilities)
- **Cloudflare Workers** (alternative: edge computing)

#### Decision 3: Custom Static Site Generator over MkDocs

**Why:**
- MkDocs is documentation-focused, not dataset-focused
- Custom generator reads directly from `dataset/`
- Full control over HTML structure (semantic, SEO-optimized)
- Smaller build size (no MkDocs overhead)
- Can optimize for speed, accessibility

**Site Generator Approach:**
- Read `dataset/terms/` (the canonical source)
- Generate one HTML page per term
- Generate index pages (A-Z, tags)
- Generate search index (lunr.js or similar)
- Output to `site/build/` (static HTML/CSS/JS)
- Deploy to GitHub Pages, Netlify, Vercel, etc.

**Technology Stack:**
- Node.js for generator script
- Handlebars or Mustache for templates
- Basic CSS (no framework bloat)
- Optional: Lunr.js for client-side search

#### Decision 4: Git as Version Control & Distribution

**Why:**
- Already using Git for version control
- Git history = dataset changelog
- Forkable, auditable, transparent
- Can tag releases (v1.0.0, v2.0.0)
- GitHub releases for periodic exports

**Versioning Strategy:**
- Semantic versioning for dataset releases
- Tag major versions (v2.0.0, v2.1.0)
- Include exports with releases (JSON, CSV, SQLite)
- Automated changelog generation

---

## Phase 4: Canonical Dataset Schema

### Minimal Durable Schema

**Design Principles:**
- **Minimal:** Only include fields that serve current needs
- **Extensible:** Can add fields later without breaking consumers
- **Explicit:** Clear semantics, no ambiguity
- **Durable:** Fields unlikely to change in 10+ years

### Core Fields (Required)

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Waxly Term",
  "description": "Canonical vinyl terminology term schema",
  "type": "object",
  "required": ["slug", "term", "summary", "definition", "tags", "created", "updated"],
  "properties": {
    "slug": {
      "type": "string",
      "description": "Unique URL-friendly identifier",
      "pattern": "^[a-z0-9-]+$"
    },
    "term": {
      "type": "string",
      "description": "Canonical term name (as displayed)"
    },
    "summary": {
      "type": "string",
      "description": "One-sentence summary (max 200 chars)",
      "maxLength": 200
    },
    "definition": {
      "type": "string",
      "description": "Full definition (plain text or markdown)"
    },
    "tags": {
      "type": "array",
      "description": "Category tags",
      "items": {
        "type": "string",
        "enum": [
          "equipment", "pressing", "mastering", "dj-related",
          "collecting", "quality-control", "slang", "technical",
          "historical", "cultural", "genre-specific", "regional"
        ]
      },
      "minItems": 1
    },
    "created": {
      "type": "string",
      "format": "date",
      "description": "Creation date (YYYY-MM-DD)"
    },
    "updated": {
      "type": "string",
      "format": "date",
      "description": "Last update date (YYYY-MM-DD)"
    }
  }
}
```

### Optional Fields

```json
{
  "aliases": {
    "type": "array",
    "description": "Alternative names/spellings",
    "items": {"type": "string"}
  },
  "see_also": {
    "type": "array",
    "description": "Related term slugs (for cross-referencing)",
    "items": {"type": "string"}
  },
  "regions": {
    "type": "array",
    "description": "Geographic regions where term is used",
    "items": {
      "type": "string",
      "enum": ["US", "UK", "CA", "AU", "JA", "DE", "FR", "IT", "NL", "global"]
    }
  },
  "content": {
    "type": "object",
    "description": "Structured content sections",
    "properties": {
      "etymology": {"type": "string"},
      "example": {"type": "string"},
      "cultural_note": {"type": "string"},
      "technical_note": {"type": "string"}
    }
  }
}
```

### Field Justification

| Field | Why Included | Why Required |
|-------|-------------|--------------|
| `slug` | Unique identifier, URL path | Essential for referencing |
| `term` | Human-readable name | Core content |
| `summary` | Quick reference, SEO, previews | User value |
| `definition` | Core explanatory content | Primary purpose |
| `tags` | Categorization, filtering | Navigation |
| `created` | Dataset integrity, audit trail | Provenance |
| `updated` | Freshness indicator | Maintenance |
| `aliases` | Searchability, alternate names | Common need (optional) |
| `see_also` | Cross-referencing, exploration | User value (optional) |
| `regions` | Geographic context | Some terms are regional (optional) |
| `content` | Rich structured content | Editorial flexibility (optional) |

### Removed Fields (From Current Schema)

**Why removed:**
- `pos` (part of speech) - Linguistic detail, low value for vinyl terminology
- `domains` - Redundant with `tags`
- `complexity`, `popularity` - Subjective, hard to maintain
- `status`, `context`, `verification` - Over-categorization
- `genres`, `eras`, `decade`, `first_attested` - Can be in `content.technical_note` if needed
- All speculative fields (AI metadata, market data, translations, media, etc.)

**Result:** ~50 lines vs 952 lines (95% reduction), 100% functional coverage

---

## Phase 5: Clean-Slate Rebuild Strategy

### Rebuild Principles

- **Clean slate:** Build 2.0 from scratch, discard all legacy infrastructure
- **Content extraction only:** Preserve term content, discard everything else
- **No backward compatibility:** No parallel systems, no rollback plan
- **Decisive:** Old site goes offline when 2.0 launches

### What We Keep

**Only the term content:**
- 568 term definitions (text only)
- Term names, summaries, descriptions
- Cross-references between terms
- That's it.

### What We Discard

**Everything else:**
- MkDocs infrastructure
- All 27 Python scripts
- 952-line bloated schema
- 7.3MB generated artifacts (jsonld, markdown-export, redirects)
- Pre-commit hooks
- Old deployment workflows
- Fantasy TODO roadmap
- All documentation files (rewrite fresh)
- Current site design/templates

**Approach:** Extract term content → Build 2.0 fresh → Replace old site

---

### Phase 5.1: Content Extraction (Day 1)

**Goal:** Extract pure term content from legacy files

**Tasks:**
1. Write simple extraction script (`extract-content.js`)
   - Read all `docs/terms/{letter}/{slug}.md`
   - Parse YAML front-matter
   - Extract markdown body
   - Output to temporary JSON file
2. Manual review of extracted data
3. Save as `legacy-content-export.json` (backup only)

**Deliverable:** Single JSON file with all 568 terms' raw content

**Output:**
```json
{
  "extracted_date": "2026-01-05",
  "total_terms": 568,
  "terms": [
    {
      "slug": "acetate",
      "term": "Acetate",
      "summary": "...",
      "definition": "...",
      "aliases": ["..."],
      "see_also": ["..."]
    }
  ]
}
```

---

### Phase 5.2: Build Canonical Dataset (Day 2-3)

**Goal:** Create clean 2.0 dataset structure

**Tasks:**
1. Create new directory structure:
```
dataset/
├── terms/
│   ├── acetate.json
│   ├── dubplate.json
│   └── ...
├── schema/
│   └── term.schema.json
└── LICENSE.md
```

2. Design minimal schema (7 required + 4 optional fields)
3. Write transformation script (`transform-to-v2.js`)
   - Read `legacy-content-export.json`
   - Map to minimal schema
   - Clean/normalize data
   - Write `dataset/terms/{slug}.json`
4. Validate 100% against schema
5. Generate `dataset/terms/index.json` (metadata index)

**Deliverable:** Complete canonical dataset (568 JSON files)

**Validation:**
```bash
node tools/validate.js
# ✓ 568 terms validated
# ✓ 0 errors
# ✓ All cross-references valid
```

---

### Phase 5.3: Build API Layer (Day 4-5)

**Goal:** Deploy production-ready serverless API

**Tasks:**
1. Create `api/` directory with serverless functions
2. Implement all endpoints:
   - `GET /v1/term/{slug}` - Single term
   - `GET /v1/terms` - List all (metadata only)
   - `GET /v1/search?q=` - Search
   - `GET /v1/tags` - List tags
   - `GET /v1/tags/{tag}` - Terms by tag
   - `GET /v1/random` - Random term
3. Add caching headers (1 hour CDN cache)
4. Deploy to Vercel
5. Custom domain: `api.waxly.com` (or subdomain)
6. Load test (verify <100ms response)

**Deliverable:** Live, production API

**Test:**
```bash
curl https://api.waxly.com/v1/term/acetate
curl https://api.waxly.com/v1/search?q=vinyl
curl https://api.waxly.com/v1/random
```

---

### Phase 5.4: Build Static Site (Day 6-8)

**Goal:** Generate fast, semantic static site

**Tasks:**
1. Create `site/` directory structure
2. Design HTML templates (base, term, index, browse, tags)
3. Design CSS (minimal, fast, responsive, accessible)
4. Implement static generator (`site/generator.js`)
   - Read from `dataset/terms/`
   - Generate all pages
   - Build search index (lunr.js)
   - Output to `site/build/`
5. Test locally (all pages, search, mobile, accessibility)
6. Optimize (minify CSS, inline critical CSS, etc.)

**Deliverable:** Production-ready static site

**Test:**
```bash
node site/generator.js
cd site/build && python -m http.server 8000
# Manual testing: navigation, search, mobile, links
```

**Performance targets:**
- Lighthouse score >95
- First Contentful Paint <1s
- Page size <50KB (HTML+CSS)

---

### Phase 5.5: Deployment & Go-Live (Day 9-10)

**Goal:** Deploy everything, replace old site

**Tasks:**
1. Set up GitHub Actions workflows:
   - `validate.yml` - Validate PRs
   - `deploy.yml` - Deploy API + site on merge
2. Configure deployments:
   - API → Vercel serverless
   - Site → GitHub Pages (or Netlify/Vercel)
3. Set up domain:
   - `waxly.com` → static site
   - `api.waxly.com` → API
4. Write fresh documentation:
   - `README.md` - Project overview
   - `docs/API.md` - API reference
   - `docs/SCHEMA.md` - Dataset schema
   - `docs/CONTRIBUTING.md` - How to contribute
5. Final testing (full smoke test)
6. Deploy to production
7. Update DNS (if domain change)
8. Announce launch

**Deliverable:** Waxly 2.0 live in production

---

### Phase 5.6: Legacy Cleanup (Day 11)

**Goal:** Delete all legacy code and infrastructure

**Tasks:**
1. Create archive branch: `git branch archive/waxly-1.0`
2. Delete from main branch:
   - `docs/` (entire directory except keep as reference)
   - `scripts/` (all 27 Python files)
   - `schema/term.schema.json` (old 952-line schema)
   - `mkdocs.yml`
   - `requirements.txt` (Python dependencies)
   - `.pre-commit-config.yaml`
   - Old `.github/workflows/deploy.yml`
   - `TODO.md`, `STATUS.md`, `WAXLY_SUMMARY.md`, etc.
   - `site/` (old MkDocs build)
   - `venv/` (Python virtual environment)
3. Keep only:
   - `dataset/` (canonical source)
   - `api/` (serverless functions)
   - `site/` (static generator + build)
   - `tools/` (validate, export utilities)
   - `docs/` (fresh documentation)
   - `.github/workflows/` (new CI/CD)
   - `README.md`, `LICENSE`, `CHANGELOG.md`

**Result:**
- Repository size: ~50MB → ~5MB (90% reduction)
- Files: ~1,500 → ~150 (90% reduction)
- Scripts: 27 → 3 (89% reduction)
- Complexity: Minimal

**Deliverable:** Clean Waxly 2.0 repository

---

### Migration Timeline

**Total: 11 days (2 weeks with buffer)**

| Day | Phase | Deliverable |
|-----|-------|-------------|
| 1 | Content Extraction | `legacy-content-export.json` |
| 2-3 | Canonical Dataset | `dataset/` with 568 validated terms |
| 4-5 | API Layer | Live API at `api.waxly.com` |
| 6-8 | Static Site | Generated site ready to deploy |
| 9-10 | Deployment | Waxly 2.0 live in production |
| 11 | Cleanup | Legacy code deleted, repo clean |

**Buffer:** +3 days for unexpected issues = **2 weeks total**

---

### No Rollback Plan

This is a **one-way migration**:

- Old site goes offline when 2.0 launches
- No parallel systems maintained
- Legacy code deleted permanently (archived in Git branch)

**Why no rollback:**
- Clean break enables better architecture
- Maintaining parallel systems wastes effort
- 2.0 is simpler, more durable - no reason to go back
- Git history preserves everything if needed

**Mitigation:**
- Archive branch `archive/waxly-1.0` preserves old code
- Comprehensive testing before go-live
- Soft launch period (1-2 weeks) to catch issues

---

### Success Criteria for Go-Live

Before replacing old site, verify:

- [ ] All 568 terms migrated successfully
- [ ] 100% dataset validation passes
- [ ] API returns correct data for all endpoints
- [ ] API response time <100ms (p95)
- [ ] Site generates without errors
- [ ] All internal links work
- [ ] Search returns relevant results
- [ ] Mobile responsive (tested on real devices)
- [ ] Lighthouse score >95
- [ ] Documentation complete and accurate
- [ ] No console errors or warnings
- [ ] Cross-browser tested (Chrome, Firefox, Safari)

**If all criteria met:** Deploy to production, retire old site

**If criteria not met:** Fix issues, re-test, delay launch

---

## Phase 6: API Concept Plan

### API Design Philosophy

- **Stateless:** No sessions, no state, no database
- **Read-only:** No mutations (edits happen via Git PR)
- **Fast:** <100ms response time
- **Free-tier friendly:** Minimal compute, caching-friendly
- **Versioned:** `/v1/` prefix for future compatibility

### Endpoint Specifications

#### GET /api/v1/term/{slug}

**Purpose:** Retrieve single term by slug

**Request:**
```
GET https://api.waxly.com/api/v1/term/acetate
```

**Response:**
```json
{
  "slug": "acetate",
  "term": "Acetate",
  "summary": "A soft lacquer-coated aluminum disc...",
  "definition": "A soft lacquer-coated aluminum...",
  "tags": ["dj-related", "pressing", "cultural"],
  "aliases": ["lacquer", "reference disc"],
  "see_also": ["dubplate", "lacquer-cut", "reference-disc"],
  "regions": ["US", "UK", "JA"],
  "content": {
    "etymology": "Named for the nitrocellulose...",
    "example": "I scored an acetate...",
    "cultural_note": "In the '50s and '60s..."
  },
  "created": "2024-10-01",
  "updated": "2025-10-06"
}
```

**Errors:**
- `404` if slug not found
- `400` if slug invalid format

#### GET /api/v1/terms

**Purpose:** List all terms (metadata only, no full definitions)

**Request:**
```
GET https://api.waxly.com/api/v1/terms
```

**Response:**
```json
{
  "total": 568,
  "terms": [
    {
      "slug": "acetate",
      "term": "Acetate",
      "summary": "A soft lacquer-coated aluminum disc...",
      "tags": ["dj-related", "pressing", "cultural"],
      "updated": "2025-10-06"
    },
    ...
  ]
}
```

**Query Parameters:**
- `?tag=pressing` - Filter by tag
- `?region=US` - Filter by region
- `?limit=50` - Limit results (default: all)
- `?offset=0` - Pagination offset

#### GET /api/v1/search

**Purpose:** Full-text search across terms

**Request:**
```
GET https://api.waxly.com/api/v1/search?q=lathe+cutting
```

**Response:**
```json
{
  "query": "lathe cutting",
  "total": 12,
  "results": [
    {
      "slug": "acetate",
      "term": "Acetate",
      "summary": "A soft lacquer-coated aluminum disc...",
      "relevance": 0.92
    },
    ...
  ]
}
```

**Search Fields:**
- `term`, `summary`, `definition`, `aliases`

**Algorithm:**
- Simple string matching (v1)
- Future: Fuzzy matching, relevance scoring

#### GET /api/v1/tags

**Purpose:** List all available tags

**Request:**
```
GET https://api.waxly.com/api/v1/tags
```

**Response:**
```json
{
  "tags": [
    {"tag": "equipment", "count": 142},
    {"tag": "pressing", "count": 89},
    {"tag": "dj-related", "count": 67},
    ...
  ]
}
```

#### GET /api/v1/random

**Purpose:** Get random term (for discovery)

**Request:**
```
GET https://api.waxly.com/api/v1/random
```

**Response:**
```json
{
  "slug": "platter-mat",
  "term": "Platter Mat",
  ...
}
```

### Implementation Approach

**Technology:** Vercel Serverless Functions (Node.js)

**Why Vercel:**
- Free tier: 100GB bandwidth, 100 hours compute/month
- Zero configuration deployment
- Edge caching built-in
- Custom domains supported
- Automatic HTTPS

**Function Structure:**

```javascript
// api/functions/get-term.js
import fs from 'fs/promises'
import path from 'path'

export default async function handler(req, res) {
  const { slug } = req.query

  // Input validation
  if (!/^[a-z0-9-]+$/.test(slug)) {
    return res.status(400).json({ error: 'Invalid slug format' })
  }

  // Read from dataset
  const termPath = path.join(process.cwd(), 'dataset', 'terms', `${slug}.json`)

  try {
    const data = await fs.readFile(termPath, 'utf-8')
    const term = JSON.parse(data)

    // Set cache headers (1 hour)
    res.setHeader('Cache-Control', 's-maxage=3600, stale-while-revalidate')
    res.setHeader('Access-Control-Allow-Origin', '*')

    return res.status(200).json(term)
  } catch (err) {
    if (err.code === 'ENOENT') {
      return res.status(404).json({ error: 'Term not found' })
    }
    return res.status(500).json({ error: 'Internal server error' })
  }
}
```

**Caching Strategy:**
- CDN edge caching (Vercel automatic)
- `Cache-Control` headers (1 hour)
- `stale-while-revalidate` for resilience

**Rate Limiting:**
- Not needed initially (read-only, cacheable)
- If abuse occurs, add Vercel rate limiting

**Monitoring:**
- Vercel analytics (built-in)
- Simple logging to console
- No complex observability needed initially

---

## Phase 7: Static Site Generation Strategy

### Site Design Philosophy

- **Zero duplication:** Read directly from `dataset/`
- **Semantic HTML:** Crawlable, accessible, SEO-optimized
- **Fast:** <1s page load, minimal JS
- **Responsive:** Mobile-first design
- **No framework bloat:** Vanilla HTML/CSS/JS

### Site Architecture

```
site/
├── src/
│   ├── templates/
│   │   ├── base.hbs           # Base HTML template
│   │   ├── term.hbs           # Term page template
│   │   ├── index.hbs          # Homepage template
│   │   ├── browse.hbs         # A-Z browse template
│   │   └── tag.hbs            # Tag page template
│   ├── styles/
│   │   ├── reset.css          # CSS reset
│   │   ├── layout.css         # Layout styles
│   │   └── theme.css          # Visual theme
│   └── scripts/
│       └── search.js          # Client-side search (lunr.js)
├── build/                     # Generated output
│   ├── index.html
│   ├── terms/
│   │   └── acetate.html
│   ├── browse/
│   │   └── a.html
│   └── tags/
│       └── pressing.html
├── generator.js               # Static site generator
└── package.json
```

### Generator Logic

**Input:** `dataset/terms/*.json`
**Output:** `site/build/*.html`

**Process:**
1. Read all terms from `dataset/terms/`
2. For each term:
   - Load term JSON
   - Apply `term.hbs` template
   - Write to `build/terms/{slug}.html`
3. Generate index pages:
   - Homepage: List all terms (alphabetical)
   - Browse pages: Group by first letter (A-Z)
   - Tag pages: Group by tag
4. Generate search index (lunr.js)
5. Copy static assets (CSS, JS)

**Technology:**
- **Handlebars** for templating
- **Node.js** for generator script
- **Lunr.js** for client-side search
- **No build tools** (no webpack/vite, just Node)

### Page Templates

#### Term Page (`term.hbs`)

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{{term}} - Waxly</title>
  <meta name="description" content="{{summary}}">
  <link rel="stylesheet" href="/styles/theme.css">
</head>
<body>
  <header>
    <nav>
      <a href="/">Waxly</a>
      <a href="/browse">Browse</a>
      <a href="/tags">Tags</a>
    </nav>
  </header>

  <main>
    <article>
      <h1>{{term}}</h1>

      {{#if aliases}}
      <p class="aliases">Also known as: {{#each aliases}}{{this}}{{#unless @last}}, {{/unless}}{{/each}}</p>
      {{/if}}

      <p class="summary">{{summary}}</p>

      <div class="definition">
        <h2>Definition</h2>
        <p>{{definition}}</p>
      </div>

      {{#if content.etymology}}
      <div class="etymology">
        <h3>Etymology</h3>
        <p>{{content.etymology}}</p>
      </div>
      {{/if}}

      {{#if content.example}}
      <div class="example">
        <h3>Example</h3>
        <p>{{content.example}}</p>
      </div>
      {{/if}}

      {{#if content.cultural_note}}
      <div class="cultural-note">
        <h3>Cultural Note</h3>
        <p>{{content.cultural_note}}</p>
      </div>
      {{/if}}

      <div class="metadata">
        <p>Tags: {{#each tags}}<a href="/tags/{{this}}">{{this}}</a>{{#unless @last}}, {{/unless}}{{/each}}</p>
        {{#if regions}}
        <p>Regions: {{#each regions}}{{this}}{{#unless @last}}, {{/unless}}{{/each}}</p>
        {{/if}}
      </div>

      {{#if see_also}}
      <div class="related">
        <h3>See Also</h3>
        <ul>
        {{#each see_also}}
          <li><a href="/terms/{{this}}">{{this}}</a></li>
        {{/each}}
        </ul>
      </div>
      {{/if}}
    </article>
  </main>

  <footer>
    <p>Waxly - The Language of Vinyl, Defined</p>
    <p><a href="/api">API</a> | <a href="https://github.com/waxly/waxly">GitHub</a></p>
  </footer>
</body>
</html>
```

### Search Implementation

**Client-side search using Lunr.js:**

1. **Index Generation** (`generator.js`):
```javascript
const lunr = require('lunr')

// Build search index
const idx = lunr(function() {
  this.ref('slug')
  this.field('term')
  this.field('summary')
  this.field('definition')
  this.field('aliases')

  terms.forEach(term => {
    this.add({
      slug: term.slug,
      term: term.term,
      summary: term.summary,
      definition: term.definition,
      aliases: term.aliases ? term.aliases.join(' ') : ''
    })
  })
})

// Write to build/search-index.json
fs.writeFileSync('build/search-index.json', JSON.stringify(idx))
```

2. **Client-side Search** (`scripts/search.js`):
```javascript
// Load index on page load
let idx
fetch('/search-index.json')
  .then(res => res.json())
  .then(data => {
    idx = lunr.Index.load(data)
  })

// Search function
function search(query) {
  const results = idx.search(query)
  // Display results
}
```

### Deployment

**Target:** GitHub Pages, Netlify, or Vercel

**Build command:**
```bash
node site/generator.js
```

**Output directory:** `site/build/`

**GitHub Actions workflow:**
```yaml
name: Deploy Site

on:
  push:
    branches: [main]

jobs:
  build-deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
      - run: npm install
      - run: node site/generator.js
      - uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./site/build
```

---

## Phase 8: Implementation Checklist

### Pre-Implementation (Day 0)

- [ ] Review and approve this architecture proposal
- [ ] Answer open questions (license, domain, API versioning, design, search)
- [ ] Archive current production site (if needed)
- [ ] Create archive branch: `git branch archive/waxly-1.0 main`
- [ ] Create working branch: `git checkout -b waxly-2.0`

### Day 1: Content Extraction

- [ ] Install Node.js dependencies (`gray-matter`, `js-yaml`)
- [ ] Write `extract-content.js` script
- [ ] Run extraction on all 568 term files
- [ ] Manual spot-check of extracted data (10-20 random terms)
- [ ] Save `legacy-content-export.json`
- [ ] Commit extraction script and output

### Day 2-3: Canonical Dataset

- [ ] Create `dataset/` directory structure
- [ ] Write minimal schema (`dataset/schema/term.schema.json`)
- [ ] Write `transform-to-v2.js` script
- [ ] Transform all 568 terms to v2 format
- [ ] Write `tools/validate.js` script
- [ ] Run validation, fix all errors
- [ ] Generate `dataset/terms/index.json`
- [ ] Validate all cross-references resolve
- [ ] Add `dataset/LICENSE.md` (CC-BY-SA 4.0)
- [ ] Commit dataset

### Day 4-5: API Layer

- [ ] Create `api/` directory structure
- [ ] Set up Vercel project
- [ ] Implement `api/functions/get-term.js`
- [ ] Implement `api/functions/list-terms.js`
- [ ] Implement `api/functions/search.js`
- [ ] Implement `api/functions/get-tags.js`
- [ ] Implement `api/functions/get-tag.js`
- [ ] Implement `api/functions/get-random.js`
- [ ] Test all endpoints locally
- [ ] Deploy to Vercel staging
- [ ] Load test (verify <100ms p95)
- [ ] Configure custom domain `api.waxly.com`
- [ ] Deploy to production
- [ ] Test production endpoints

### Day 6-8: Static Site

- [ ] Create `site/` directory structure
- [ ] Design HTML templates (Handlebars)
  - [ ] `base.hbs` - Base layout
  - [ ] `term.hbs` - Term page
  - [ ] `index.hbs` - Homepage
  - [ ] `browse.hbs` - A-Z browse
  - [ ] `tag.hbs` - Tag page
- [ ] Write CSS
  - [ ] Reset/normalize
  - [ ] Layout (mobile-first)
  - [ ] Typography
  - [ ] Components
- [ ] Implement `site/generator.js`
  - [ ] Read dataset
  - [ ] Generate term pages
  - [ ] Generate index/browse/tag pages
  - [ ] Build search index (lunr.js)
  - [ ] Copy assets
- [ ] Test locally (all pages render)
- [ ] Test search functionality
- [ ] Test mobile responsive
- [ ] Run Lighthouse audit (target >95)
- [ ] Optimize (minify, inline critical CSS)

### Day 9-10: Deployment & Go-Live

- [ ] Create `.github/workflows/validate.yml`
- [ ] Create `.github/workflows/deploy.yml`
- [ ] Configure Vercel integration (API)
- [ ] Configure GitHub Pages/Netlify (site)
- [ ] Write `README.md`
- [ ] Write `docs/API.md`
- [ ] Write `docs/SCHEMA.md`
- [ ] Write `docs/CONTRIBUTING.md`
- [ ] Test full CI/CD workflow (PR → merge → deploy)
- [ ] Final smoke test (all features)
- [ ] Deploy to production
- [ ] Configure DNS (if needed)
- [ ] Monitor for errors (24 hours)

### Day 11: Legacy Cleanup

- [ ] Verify 2.0 is stable in production
- [ ] Delete legacy files:
  - [ ] `docs/terms/`, `docs/letters/`, `docs/tags/`
  - [ ] `docs/jsonld/`, `docs/markdown-export/`, `docs/redirects/`
  - [ ] `scripts/` (all Python scripts)
  - [ ] `schema/term.schema.json` (old schema)
  - [ ] `mkdocs.yml`
  - [ ] `requirements.txt`
  - [ ] `.pre-commit-config.yaml`
  - [ ] Old workflows
  - [ ] `TODO.md`, `STATUS.md`, `WAXLY_SUMMARY.md`
  - [ ] Old `site/` directory
  - [ ] `venv/`
- [ ] Update `.gitignore` for new structure
- [ ] Commit cleanup
- [ ] Merge `waxly-2.0` → `main`
- [ ] Create tag `v2.0.0`
- [ ] Push to GitHub
- [ ] Announce Waxly 2.0 launch

---

## Appendix A: Technology Choices

### Primary Stack (Recommended)

| Layer | Technology | Why |
|-------|-----------|-----|
| Dataset Format | JSON | Universal parsability, validation, LLM-friendly |
| Schema Validation | JSON Schema | Standard, tooling support |
| API Runtime | Vercel Serverless | Free tier, zero config, edge caching |
| API Language | Node.js | Ecosystem, simplicity |
| Site Generator | Custom (Node.js + Handlebars) | Full control, minimal bloat |
| Templating | Handlebars | Simple, logic-less |
| Styling | Vanilla CSS | No framework dependencies |
| Search | Lunr.js | Client-side, fast, no backend |
| Site Hosting | GitHub Pages | Free, reliable, Git-integrated |
| CI/CD | GitHub Actions | Integrated, free for public repos |
| Version Control | Git + GitHub | Standard, community-friendly |

### Alternative Options (Considered)

| Decision | Alternative | Why Not Chosen |
|----------|------------|----------------|
| Dataset Format | YAML | Less universal than JSON, parsing complexity |
| Dataset Format | SQLite | Binary format, harder to diff/version |
| API Runtime | AWS Lambda | More complex setup than Vercel |
| API Runtime | Static JSON files | No query/search capabilities |
| Site Generator | MkDocs | Documentation-focused, not dataset-first |
| Site Generator | 11ty | Additional abstraction, learning curve |
| Site Generator | Astro | Overkill for simple static site |
| Search | Algolia | Third-party service, cost, complexity |
| Search | Pagefind | Good option, but lunr.js simpler |
| Hosting | Netlify | Similar to Vercel, slight preference for Vercel |
| Hosting | Cloudflare Pages | Good option, GitHub Pages integrates better |

---

## Appendix B: Migration Risk Assessment

### Low Risk

- **Dataset conversion:** Automated script, reversible, testable
- **API deployment:** Serverless, stateless, no database to migrate
- **Site generation:** New system runs parallel to old initially

### Medium Risk

- **Schema simplification:** Need to ensure no data loss in field mapping
- **Search functionality:** Lunr.js may not match MkDocs Material search quality
- **Cross-reference links:** Need to validate all `see_also` links resolve

### Mitigation Strategies

1. **Parallel systems:** Keep old site running until new site validated
2. **Validation scripts:** 100% automated validation of dataset integrity
3. **Rollback plan:** Each phase is reversible
4. **Testing:** Comprehensive manual testing of all features
5. **Community review:** Soft launch to gather feedback before full switch

### Rollback Triggers

- Dataset validation fails (missing/corrupted data)
- API unavailable or unacceptably slow (>500ms)
- Site generation broken or missing pages
- Search functionality severely degraded
- Community reports major usability issues

---

## Appendix C: Success Criteria

### Technical Metrics

- [ ] 568 terms migrated successfully (100%)
- [ ] All terms validate against schema (100%)
- [ ] API response time <100ms (95th percentile)
- [ ] API uptime >99.9%
- [ ] Site page load <1s (95th percentile)
- [ ] Site mobile-friendly (Google PageSpeed >90)
- [ ] Repository size reduced >70%
- [ ] Zero broken cross-reference links
- [ ] Search returns relevant results for common queries

### Operational Metrics

- [ ] Deployment fully automated (zero manual steps)
- [ ] CI/CD workflow completes in <5 minutes
- [ ] Contributing workflow documented and tested
- [ ] Maintenance time <1 hour/week

### Community Metrics

- [ ] Documentation complete and clear
- [ ] No blocking issues reported in first 2 weeks
- [ ] Community feedback positive or neutral
- [ ] External projects able to fork/integrate dataset

---

## Appendix D: Open Questions

### Questions for User/Stakeholder

1. **License:** CC0 (public domain) or CC-BY-SA 4.0 (attribution + share-alike)?
   - CC0: Maximum freedom, no attribution required
   - CC-BY-SA: Ensures attribution and derivatives stay open

2. **Domain:** Keep `hellowaxly.com` or switch to `waxly.com`?
   - Current: `hellowaxly.com` (redirects to GitHub Pages)
   - Ideal: `waxly.com` (cleaner, more memorable)

3. **API Versioning:** Start at `/v1/` or `/api/` only?
   - `/v1/`: Explicit versioning from start
   - `/api/`: Simpler, add versioning when needed

4. **Site Design:** Minimal (text-focused) or polished (branded)?
   - Minimal: Faster to build, lower maintenance
   - Polished: Better first impression, more design work

5. **Search:** Client-side (lunr.js) or server-side (API endpoint)?
   - Client-side: Faster, no backend, works offline
   - Server-side: More powerful, relevance tuning, slower

### Recommended Answers

1. **License:** CC-BY-SA 4.0 (ensures attribution and open derivatives)
2. **Domain:** `waxly.com` (if available and affordable)
3. **API Versioning:** `/v1/` (future-proof from start)
4. **Site Design:** Start minimal, polish incrementally
5. **Search:** Client-side lunr.js (simpler, faster)

---

## Next Steps

**Decision Required:**

Answer these 5 questions to proceed:

1. **License:** CC0 (public domain) or CC-BY-SA 4.0 (attribution + share-alike)?
   - *Recommendation: CC-BY-SA 4.0*

2. **Domain:** Keep `hellowaxly.com` or use `waxly.com`?
   - *Recommendation: `waxly.com` if available*

3. **API Versioning:** Start at `/v1/` or `/api/` without version?
   - *Recommendation: `/v1/` for future-proofing*

4. **Site Design:** Minimal text-focused or polished branded design?
   - *Recommendation: Start minimal, polish later*

5. **Search:** Client-side (lunr.js) or server-side (API endpoint)?
   - *Recommendation: Client-side for simplicity*

**Upon Approval:**

1. Archive current state: `git branch archive/waxly-1.0 main`
2. Create working branch: `git checkout -b waxly-2.0`
3. Begin Day 1: Content Extraction
4. Build through Days 2-11 following checklist
5. Launch Waxly 2.0 to production
6. Delete legacy code
7. Merge to main, tag v2.0.0

**Timeline:**

- **Working days:** 11 days
- **With buffer:** 14 days (2 weeks)
- **Calendar time:** 2-3 weeks depending on availability

**What You'll Get:**

- Clean, minimal codebase (90% size reduction)
- Fast, semantic static site (Lighthouse >95)
- Production API (<100ms response time)
- Machine-readable canonical dataset
- Complete documentation
- Fully automated deployment
- Durable architecture designed for 10-20 year lifespan

---

**Ready to begin? Confirm the 5 decisions above and we'll start building.**

---

**End of Proposal**
