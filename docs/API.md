# Waxly API Documentation

**Base URL:** `https://waxly.music` (or your deployed domain)
**Version:** v1
**Authentication:** None (public read-only access)

---

## Overview

The Waxly API provides programmatic access to the complete vinyl terminology dataset. All endpoints return JSON and are cached at the edge for fast global access.

**Features:**
- 🌐 Public, free, no authentication required
- ⚡ Edge-cached for <100ms response times
- 🔓 CORS-enabled for browser access
- 📝 RESTful design
- 🎯 Simple, predictable structure

---

## Endpoints

### GET /v1/term/{slug}

Retrieve a single term by its slug.

**Parameters:**
- `slug` (path, required) - URL-friendly term identifier

**Example Request:**
```bash
curl https://waxly.music/v1/term/acetate
```

**Example Response:**
```json
{
  "slug": "acetate",
  "term": "Acetate",
  "pos": "noun",
  "pronunciation": "/ˈæsɪteɪt/",
  "summary": "A soft lacquer-coated aluminum disc used to cut the first playable copy of a recording.",
  "definition": "A soft lacquer-coated aluminum (or occasionally glass) disc used to cut the very first playable copy of a recording straight from the mastering lathe. Acetates wear out fast — maybe 10–20 plays — but capture the freshest, most dynamic version of a track. In the '50s and '60s, DJs prized acetates for breaking brand-new singles in clubs before commercial pressings existed.",
  "tags": ["dj-related", "pressing", "mastering"],
  "aliases": ["lacquer", "reference disc"],
  "alt_spellings": ["acetate disc", "acetate record"],
  "etymology": "From 'acetate' referring to cellulose acetate, though modern acetates use nitrocellulose lacquer",
  "first_use": 1934,
  "see_also": ["dubplate", "lacquer-cut", "test-pressing"],
  "regions": ["US", "UK", "JA"],
  "created": "2026-01-05",
  "updated": "2026-01-05"
}
```

**Response Codes:**
- `200` - Success
- `404` - Term not found
- `400` - Invalid slug format

**Cache:** 1 hour

---

### GET /v1/terms

List all terms with metadata (no full definitions).

**Parameters:**
- `tag` (query, optional) - Filter by tag
- `limit` (query, optional) - Max results to return
- `offset` (query, optional) - Pagination offset

**Example Request:**
```bash
# Get all terms
curl https://waxly.music/v1/terms

# Filter by tag
curl https://waxly.music/v1/terms?tag=pressing

# Pagination
curl https://waxly.music/v1/terms?limit=50&offset=100
```

**Example Response:**
```json
{
  "total": 567,
  "offset": 0,
  "limit": 567,
  "terms": [
    {
      "slug": "acetate",
      "term": "Acetate",
      "summary": "A soft lacquer-coated aluminum disc...",
      "tags": ["dj-related", "pressing", "cultural"],
      "updated": "2026-01-05"
    },
    {
      "slug": "dubplate",
      "term": "Dubplate",
      "summary": "An exclusive vinyl disc...",
      "tags": ["dj-related", "cultural"],
      "updated": "2026-01-05"
    }
  ]
}
```

**Response Codes:**
- `200` - Success
- `500` - Server error

**Cache:** 1 hour

---

### GET /v1/search

Full-text search across all terms.

**Parameters:**
- `q` (query, required) - Search query (min 2 characters)

**Example Request:**
```bash
curl "https://waxly.music/v1/search?q=vinyl"
```

**Example Response:**
```json
{
  "query": "vinyl",
  "total": 42,
  "results": [
    {
      "slug": "heavyweight-vinyl",
      "term": "Heavyweight Vinyl",
      "summary": "Vinyl records pressed on 180-gram or 200-gram stock...",
      "tags": ["pressing", "quality-control"]
    },
    {
      "slug": "virgin-vinyl",
      "term": "Virgin Vinyl",
      "summary": "Vinyl pressed from new, unused PVC compound...",
      "tags": ["pressing", "quality-control"]
    }
  ]
}
```

**Search Behavior:**
- Searches across: term name, summary, definition, aliases
- Case-insensitive
- Returns up to 50 results
- Simple substring matching (no fuzzy search in v1)

**Response Codes:**
- `200` - Success
- `400` - Query too short (min 2 chars)
- `500` - Server error

**Cache:** 5 minutes

---

### GET /v1/random

Get a random term (useful for discovery features).

**Parameters:** None

**Example Request:**
```bash
curl https://waxly.music/v1/random
```

**Example Response:**
```json
{
  "slug": "platter-mat",
  "term": "Platter Mat",
  "summary": "A mat placed on the turntable platter...",
  "definition": "A mat placed on the turntable platter to dampen vibrations...",
  "tags": ["equipment"],
  "created": "2026-01-05",
  "updated": "2026-01-05"
}
```

**Response Codes:**
- `200` - Success
- `500` - Server error

**Cache:** None (always fresh)

---

## Response Format

All endpoints return JSON with consistent structure:

### Success Response

```json
{
  // Data specific to endpoint
}
```

### Error Response

```json
{
  "error": "Error message describing what went wrong"
}
```

---

## Rate Limiting

**Current:** No rate limiting
**Future:** May implement fair-use limits if needed

**Recommended:**
- Cache responses on your end
- Use `?limit` parameter for paginated access
- Don't hammer the API unnecessarily

---

## CORS

All endpoints include CORS headers:

```
Access-Control-Allow-Origin: *
```

This means you can call the API directly from browser JavaScript.

**Example (JavaScript):**
```javascript
fetch('https://waxly.music/v1/term/acetate')
  .then(res => res.json())
  .then(data => console.log(data))
```

---

## Caching

Responses include cache headers:

- **GET /v1/term/{slug}** - 1 hour cache
- **GET /v1/terms** - 1 hour cache
- **GET /v1/search** - 5 minute cache
- **GET /v1/random** - No cache

**Headers:**
```
Cache-Control: s-maxage=3600, stale-while-revalidate
```

---

## Data Schema

### Term Object

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `slug` | string | Yes | Unique identifier (shortest common form) |
| `term` | string | Yes | Display name |
| `summary` | string | Yes | Complete sentence definition (≤25 words, max 200 chars) |
| `definition` | string | Yes | Detailed explanation (recommended 50-300 words) |
| `tags` | array | Yes | Category tags (min 1) |
| `created` | string | Yes | Creation date (YYYY-MM-DD) |
| `updated` | string | Yes | Last update date (YYYY-MM-DD) |
| `pos` | string | No | Part of speech (noun, verb, adjective, adverb, phrase) |
| `pronunciation` | string | No | IPA or phonetic notation |
| `aliases` | array | No | Alternative names for the same thing |
| `alt_spellings` | array | No | Spelling variations, regional variants, misspellings |
| `etymology` | string | No | Historical origin and development |
| `first_use` | integer | No | Year of first known usage (1800-2100) |
| `see_also` | array | No | Related term slugs |
| `regions` | array | No | Geographic regions |

---

## Example Use Cases

### Build a Glossary Widget

```javascript
async function loadGlossary() {
  const res = await fetch('https://waxly.music/v1/terms?tag=dj-related')
  const data = await res.json()

  data.terms.forEach(term => {
    // Render term in your UI
  })
}
```

### Search Autocomplete

```javascript
async function searchTerms(query) {
  if (query.length < 2) return []

  const res = await fetch(`https://waxly.music/v1/search?q=${encodeURIComponent(query)}`)
  const data = await res.json()

  return data.results
}
```

### Random Term of the Day

```javascript
async function getRandomTerm() {
  const res = await fetch('https://waxly.music/v1/random')
  return await res.json()
}
```

---

## Dataset Access

Prefer to work with the raw dataset? Download the complete dataset from GitHub:

```bash
git clone https://github.com/waxly/waxly.git
cd waxly/dataset/terms
```

All 567 terms are available as individual JSON files.

---

## Changelog

### v1 (2026-01-05)
- Initial API release
- 4 endpoints: term, terms, search, random
- 567 terms available
- Edge-cached for fast global access

---

## Support

- **Issues:** https://github.com/waxly/waxly/issues
- **Documentation:** https://github.com/waxly/waxly
- **Dataset License:** CC BY-SA 4.0

---

## Attribution

When using the Waxly dataset in your project:

> Powered by the Waxly Vinyl Terminology Dataset (https://waxly.music)
> Licensed under CC BY-SA 4.0

---

**Happy building!** 🎵
