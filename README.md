# Waxly 2.1

> Canonical, open, machine-readable vinyl terminology dictionary

**Domain:** waxly.music (planned)

---

## What is Waxly?

Waxly is **infrastructure, not a product**. It's a comprehensive vinyl terminology dictionary and single source of truth, designed for:

- **AI & LLMs** - Structured, machine-readable data optimized for ingestion
- **Developers** - Free public API for applications and tools
- **Researchers** - Open dataset (CC BY-SA 4.0) for academic and commercial use
- **Linguists** - Dictionary-style metadata (etymology, pronunciation, part of speech)
- **Collectors** - Comprehensive reference with historical context
- **Humans** - Fast, accessible web reference

**Coverage:** 567+ terms from the phonautograph (1857) to modern vinyl culture

**Schema:** Dictionary-style structure with linguistic metadata, definitions, and cross-references

---

## Quick Start

### Browse Terms

Visit the website (coming soon: waxly.music) to browse all terms alphabetically or by tag.

### Use the API

Free, open, read-only API:

```bash
# Get single term
curl https://waxly.music/v1/term/acetate

# List all terms (metadata only)
curl https://waxly.music/v1/terms

# Search
curl https://waxly.music/v1/search?q=vinyl

# Random term
curl https://waxly.music/v1/random
```

### Use the Dataset

The canonical dataset is in `dataset/terms/` - 567 JSON files, one per term.

```bash
# Clone repository
git clone https://github.com/waxly/waxly.git
cd waxly

# Read a term
cat dataset/terms/acetate.json

# Validate dataset
node tools/validate.js
```

---

## Architecture

Waxly 2.0 has three layers, all derived from one canonical dataset:

```
dataset/terms/*.json  →  [Canonical Source of Truth]
                     ↓
             ┌───────┴────────┐
             ↓                ↓
         API Layer       Static Site
      (Serverless)       (Generated)
```

### 1. Canonical Dataset (`dataset/`)

- **Format:** JSON (one file per term)
- **Schema v2.1:** Dictionary-style (7 required + 9 optional fields)
  - Required: slug, term, summary, definition, tags, created, updated
  - Optional: pos, pronunciation, aliases, alt_spellings, etymology, first_use, see_also, regions, short_definition
- **License:** CC BY-SA 4.0
- **Versioned:** Git history is the changelog

### 2. Public API (`api/`)

- **Runtime:** Vercel Serverless Functions
- **Endpoints:** `/v1/term/{slug}`, `/v1/terms`, `/v1/search`, `/v1/random`
- **Performance:** <100ms response time, edge-cached
- **Cost:** Free tier (no authentication required)

### 3. Static Site (`site/`)

- **Generator:** Custom Node.js + Handlebars
- **Output:** Semantic HTML, minimal CSS
- **Performance:** Lighthouse score >95
- **Hosting:** GitHub Pages (or Netlify/Vercel)

---

## Repository Structure

```
waxly/
├── dataset/              # Canonical source of truth
│   ├── terms/*.json      # 567 term files
│   ├── schema/           # JSON schema
│   └── LICENSE.md        # CC BY-SA 4.0 license
├── api/                  # Serverless API
│   └── functions/*.js    # API endpoints
├── site/                 # Static site generator
│   ├── templates/        # HTML templates
│   ├── styles/           # CSS
│   ├── generator.js      # Build script
│   └── build/            # Generated output
├── tools/                # Utilities
│   └── validate.js       # Dataset validator
└── .github/workflows/    # CI/CD automation
```

---

## Development

### Prerequisites

- Node.js 18+
- Git

### Local Setup

```bash
# Clone repository
git clone https://github.com/waxly/waxly.git
cd waxly

# Validate dataset
node tools/validate.js

# Build site locally
cd site
npm install
node generator.js

# Preview site
npm run serve
# Visit http://localhost:8000
```

### Adding/Editing Terms

1. Edit JSON file in `dataset/terms/`
2. Validate: `node tools/validate.js`
3. Rebuild site: `node site/generator.js`
4. Commit and push (auto-deploys via GitHub Actions)

**Schema:** See `dataset/schema/term.schema.json` for required fields

---

## API Reference

### GET /v1/term/{slug}

Returns single term by slug.

**Example:**
```bash
curl https://waxly.music/v1/term/acetate
```

**Response:**
```json
{
  "slug": "acetate",
  "term": "Acetate",
  "pos": "noun",
  "pronunciation": "/ˈæsɪteɪt/",
  "summary": "A soft lacquer-coated aluminum disc used to cut the first playable copy of a recording.",
  "definition": "Full definition text with context, history, and usage examples...",
  "tags": ["dj-related", "pressing", "mastering"],
  "aliases": ["lacquer", "reference disc"],
  "alt_spellings": ["acetate disc", "acetate record"],
  "etymology": "From 'acetate' referring to cellulose acetate...",
  "first_use": 1934,
  "see_also": ["dubplate", "lacquer-cut", "test-pressing"],
  "regions": ["US", "UK", "JA"],
  "created": "2026-01-05",
  "updated": "2026-01-05"
}
```

### GET /v1/terms

Returns list of all terms (metadata only).

**Parameters:**
- `tag` - Filter by tag
- `limit` - Limit results
- `offset` - Pagination offset

**Example:**
```bash
curl https://waxly.music/v1/terms?tag=pressing&limit=10
```

### GET /v1/search?q={query}

Full-text search across all terms.

**Example:**
```bash
curl https://waxly.music/v1/search?q=vinyl
```

### GET /v1/random

Returns a random term (for discovery).

**Example:**
```bash
curl https://waxly.music/v1/random
```

---

## Dataset License

**CC BY-SA 4.0** - Creative Commons Attribution-ShareAlike 4.0 International

- ✓ Free to use, share, and adapt (including commercial use)
- ✓ Must provide attribution
- ✓ Derivatives must use same license

**Attribution:**
> Waxly Vinyl Terminology Dataset, available at https://waxly.music, licensed under CC BY-SA 4.0

See `dataset/LICENSE.md` for full license text.

---

## Code License

**MIT License** - All code (scripts, API, site generator) is MIT licensed.

See `LICENSE` for details.

---

## Contributing

We welcome contributions from the vinyl community!

**How to contribute:**

1. Fork this repository
2. Add/edit term JSON files in `dataset/terms/`
3. Validate: `node tools/validate.js`
4. Submit pull request

**Guidelines:**
- Follow the schema (`dataset/schema/term.schema.json`)
- One term per file
- Use clear, accessible language
- Provide sources when possible

---

## Project Goals

Waxly is designed to be:

1. **Durable** - Still usable in 10-20 years without changes
2. **Open** - Free to use, fork, and integrate
3. **Machine-first** - Optimized for AI/LLM consumption
4. **Low-maintenance** - Minimal operational burden
5. **Canonical** - Single source of truth for vinyl terminology

**Not a goal:** Traffic, monetization, feature bloat, community platform

---

## Version History

- **v2.1.0** (2026-01-05) - Dictionary-style enhancements: added pos, pronunciation, etymology, first_use fields; enhanced validation
- **v2.0.0** (2026-01-05) - Complete rebuild: dataset-first architecture, minimal schema, serverless API, static site generator
- **v1.x** - MkDocs-based documentation site (archived)

---

## Contact

- **GitHub:** https://github.com/waxly/waxly
- **Issues:** https://github.com/waxly/waxly/issues
- **License Questions:** See `dataset/LICENSE.md`

---

**Waxly - The Language of Vinyl, Defined**
