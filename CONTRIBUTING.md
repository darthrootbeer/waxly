# Contributing to Waxly

Thank you for your interest in contributing to Waxly! This guide will help you add or edit vinyl terminology.

---

## Quick Start

1. **Fork** this repository
2. **Edit** or add term files in `dataset/terms/`
3. **Validate** your changes
4. **Submit** a pull request

---

## Adding a New Term

### 1. Create the Term File

Create a new JSON file in `dataset/terms/` with the term's slug as the filename:

```bash
# Example: dataset/terms/acetate.json
```

### 2. Use the Term Template

```json
{
  "slug": "your-term-slug",
  "term": "Your Term Name",
  "pos": "noun",
  "pronunciation": "/tɜːrm neɪm/",
  "summary": "A complete sentence short definition (max 25 words).",
  "definition": "Full definition explaining what this term means in vinyl culture, with context, history, and usage examples (recommended 50-300 words).",
  "tags": ["equipment", "pressing"],
  "created": "2026-01-05",
  "updated": "2026-01-05",
  "aliases": ["alternative-term", "another-name"],
  "alt_spellings": ["variant-spelling", "common-misspelling"],
  "etymology": "Origin from Latin terminus (1850s)",
  "first_use": 1857,
  "see_also": ["related-term"],
  "regions": ["US", "UK"]
}
```

### 3. Required Fields

- `slug` - Shortest unique URL-friendly identifier (lowercase, hyphens only, max 50 chars, NEVER includes alt terms)
- `term` - Canonical display name
- `summary` - **Complete sentence** short definition (≤25 words, max 200 chars, must end with . ! or ?)
- `definition` - Detailed explanation (recommended 50-300 words)
- `tags` - At least one category tag (see valid tags below)
- `created` - Date created (YYYY-MM-DD)
- `updated` - Last update date (YYYY-MM-DD)

### 4. Optional Fields

```json
{
  "pos": "noun",
  "pronunciation": "/pronunciation/",
  "aliases": ["alternative-spelling", "variant-name"],
  "etymology": "Historical origin and development",
  "first_use": 1950,
  "see_also": ["related-term-slug"],
  "regions": ["US", "UK", "JA"]
}
```

**Field descriptions:**
- `pos` - Part of speech: noun, verb, adjective, adverb, phrase
- `pronunciation` - IPA notation or simplified phonetic spelling
- `aliases` - Alternative names for the same thing (e.g., "acetate" → "lacquer", "reference disc")
- `alt_spellings` - Spelling variations, regional variants, common misspellings (e.g., "DJ" → "deejay", "disc jockey")
- `etymology` - Origin and historical development of the term
- `first_use` - Year of first known usage (1800-2100)
- `see_also` - Related term slugs (must exist in dataset)
- `regions` - Geographic regions where term is commonly used

---

## Valid Tags

Choose from these categories:

- `equipment` - Turntables, cartridges, tools
- `pressing` - Manufacturing, vinyl production
- `mastering` - Recording, cutting, lacquers
- `dj-related` - DJ techniques, culture
- `collecting` - Collector terms, grading
- `quality-control` - Defects, testing
- `slang` - Informal terminology
- `technical` - Technical specifications
- `historical` - Historical context
- `cultural` - Cultural significance
- `genre-specific` - Genre-related terms
- `regional` - Region-specific terms

---

## Editing an Existing Term

1. Find the term file in `dataset/terms/`
2. Edit the JSON file
3. Update the `updated` date to today
4. Validate and submit PR

---

## Validation

Before submitting, validate your changes:

```bash
# Validate dataset
node tools/validate.js

# Should output:
# ✓ XXX terms validated
# ✓ 0 errors
```

### Common Validation Errors

**"Invalid slug format"**
- Use only lowercase letters, numbers, and hyphens
- No spaces, underscores, or special characters
- Keep it short (max 50 chars)
- Never include alt terms in slug
- Example: `acetate` not `acetate-lacquer-reference-disc`

**"Summary must be a complete sentence"**
- Summary must end with . ! or ?
- Example: ✅ "A soft lacquer disc used for test cuts."
- Example: ❌ "A soft lacquer disc used for test cuts"

**"Summary exceeds 25 words"**
- Keep summaries concise (≤25 words)
- Focus on core definition only

**"Definition is short"**
- Aim for 50-300 words in detailed definition
- Add context, history, usage examples
- Explain cultural significance

**"Invalid tag"**
- Use only tags from the valid list above
- Check spelling and capitalization

**"Invalid part of speech"**
- Must be one of: noun, verb, adjective, adverb, phrase

**"first_use out of range"**
- Must be between 1800-2100
- Use integer year only

**"Missing required field"**
- Ensure all required fields are present
- Double-check field names (case-sensitive)

---

## Writing Guidelines

### Style

- **Clear and accessible** - Write for enthusiasts and newcomers
- **Encyclopedia-like** - Factual, neutral tone
- **Concise** - Get to the point quickly
- **Culturally sensitive** - Respect all communities

### Definition Structure

```json
{
  "definition": "Start with a clear, direct explanation. Add context and details. Include historical or cultural significance if relevant."
}
```

### Good Example (Complete)

```json
{
  "slug": "acetate",
  "term": "Acetate",
  "pos": "noun",
  "pronunciation": "/ˈæsɪteɪt/",
  "summary": "A soft lacquer-coated aluminum disc used to cut the first playable copy of a recording.",
  "definition": "A soft lacquer-coated aluminum (or occasionally glass) disc used to cut the very first playable copy of a recording straight from the mastering lathe. Acetates wear out fast — maybe 10–20 plays — but capture the freshest, most dynamic version of a track. In the '50s and '60s, DJs prized acetates for breaking brand-new singles in clubs before commercial pressings existed. The lacquer coating is fragile and degrades with each play, making acetates unsuitable for mass production but invaluable for test cuts and exclusive DJ use.",
  "tags": ["pressing", "mastering", "dj-related"],
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

### Minimal Example (Required Fields Only)

```json
{
  "slug": "gatefold",
  "term": "Gatefold",
  "summary": "An album cover that opens like a book with panels on both sides.",
  "definition": "A gatefold sleeve is a type of album packaging that folds open from the center, creating a four-panel display when fully opened. First introduced in the late 1950s, gatefolds became popular for deluxe editions and double albums, offering extra space for artwork, liner notes, and credits. The format reached its peak during the progressive rock era of the 1970s when elaborate album art was a key part of the listening experience.",
  "tags": ["collecting"],
  "created": "2026-01-05",
  "updated": "2026-01-05"
}
```

### Avoid

- ❌ Personal opinions or preferences
- ❌ Marketing language or hype
- ❌ Excessive technical jargon without explanation
- ❌ Assumptions about reader knowledge

---

## Cross-References

Link to related terms using `see_also`:

```json
{
  "see_also": ["dubplate", "lacquer-cut", "test-pressing"]
}
```

**Rules:**
- Use the exact slug of the related term
- Only reference terms that exist in the dataset
- Choose 3-5 most relevant related terms

---

## Pull Request Process

### 1. Submit PR

- **Title:** Short description (e.g., "Add term: acetate")
- **Description:** Explain what you added/changed and why

### 2. Automated Checks

Your PR will automatically:
- Validate all JSON syntax
- Check schema compliance
- Verify cross-references

### 3. Review

Maintainers will review for:
- Accuracy and clarity
- Appropriate categorization
- Proper formatting
- Cultural sensitivity

### 4. Merge

Once approved, your contribution will be merged and deployed automatically!

---

## Dataset License

By contributing, you agree that your contributions will be licensed under **CC BY-SA 4.0** (Creative Commons Attribution-ShareAlike 4.0 International).

This means:
- ✓ Your work will be attributed to you
- ✓ Others can freely use and adapt it
- ✓ Derivatives must use the same license

---

## Questions?

- **Issues:** Open an issue on GitHub
- **Discussions:** Use GitHub Discussions
- **Documentation:** Check the README

---

## Recognition

All contributors are valued! Significant contributions may be recognized in release notes.

Thank you for helping preserve vinyl culture knowledge! 🎵
