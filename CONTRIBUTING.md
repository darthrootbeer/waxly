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
  "summary": "One-sentence summary (max 200 characters)",
  "definition": "Full definition explaining what this term means in vinyl culture.",
  "tags": ["equipment", "pressing"],
  "created": "2026-01-05",
  "updated": "2026-01-05"
}
```

### 3. Required Fields

- `slug` - URL-friendly identifier (lowercase, hyphens only)
- `term` - Display name of the term
- `summary` - Brief one-sentence description (max 200 chars)
- `definition` - Complete definition
- `tags` - At least one tag (see valid tags below)
- `created` - Date created (YYYY-MM-DD)
- `updated` - Last update date (YYYY-MM-DD)

### 4. Optional Fields

```json
{
  "aliases": ["alternative-name", "another-name"],
  "see_also": ["related-term-slug", "another-term-slug"],
  "regions": ["US", "UK", "JA"]
}
```

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
- Example: `heavy-vinyl` not `Heavy_Vinyl`

**"Summary too long"**
- Keep summaries under 200 characters
- Be concise and clear

**"Invalid tag"**
- Use only tags from the valid list above
- Check spelling and capitalization

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

### Good Example

```json
{
  "slug": "acetate",
  "term": "Acetate",
  "summary": "A soft lacquer-coated aluminum disc used to cut the first playable copy of a recording.",
  "definition": "A soft lacquer-coated aluminum (or occasionally glass) disc used to cut the very first playable copy of a recording straight from the mastering lathe. Acetates wear out fast — maybe 10–20 plays — but capture the freshest, most dynamic version of a track. In the '50s and '60s, DJs prized acetates for breaking brand-new singles in clubs before commercial pressings existed.",
  "tags": ["pressing", "mastering", "dj-related"],
  "aliases": ["lacquer", "reference disc"],
  "see_also": ["dubplate", "lacquer-cut"],
  "regions": ["US", "UK"],
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
