# Waxly 2.1 TODO

## Schema Enhancements

### Dictionary-Style Metadata Fields
- [x] Expand `aliases` to include alternative names, spellings, and variants
- [ ] Add `pos` (part of speech): noun, verb, adjective, etc.
- [ ] Add `pronunciation`: IPA or phonetic notation
- [ ] Add `etymology`: origin and historical development
- [ ] Add `first_use`: year of first known usage
- [ ] Update `dataset/schema/term.schema.json` with new fields
- [ ] Update documentation in CONTRIBUTING.md
- [ ] Update API responses to include new fields
- [ ] Update site templates to display new metadata

**Rationale**: Transform Waxly into a proper vinyl terminology dictionary with linguistic metadata.

### Definition Structure (Revised)
- [x] Add `short_definition` field (≤25 words, ~175 chars)
- [x] Update `definition` to require 50+ chars (recommended 50-300 words)
- [ ] **Clarify**: `summary` should be a complete sentence (the short definition)
- [ ] **Rule**: Summary must never be cut off mid-sentence
- [ ] Update all 567 terms to ensure complete sentence summaries
- [ ] Expand definitions to 50-300 words where appropriate
- [ ] Update CONTRIBUTING.md with new definition guidelines

**Revised Structure:**
- `summary`: Complete sentence short definition (≤25 words) - PRIMARY definition
- `definition`: Extended explanation with context, history, usage (50-300 words)
- `short_definition`: DEPRECATED in favor of `summary`

**Rationale**: Align with dictionary conventions - summary as primary definition, definition as extended notes.

## Schema Design Questions

**Field naming options:**
- Option A: `short_definition` + `long_definition` (explicit)
- Option B: `summary` + `definition` (current, repurpose summary)
- Option C: `definition` + `extended_definition` (brief is primary)

**Alternative terms naming:**
- Option A: `alternate_spellings` (specific)
- Option B: `variants` (general)
- Option C: `alt_terms` (concise)
- Option D: Keep `aliases` and expand its scope

**Backwards compatibility:**
- [ ] Decide: breaking change (v3.0) or backward-compatible (v2.1)?
- [ ] If breaking: update CHANGELOG with migration guide
- [ ] If compatible: make new fields optional, add validation

## Content Expansion

### Vocabulary Mining
- [ ] **Scrape Discogs listings** to identify 100+ most common terms for describing records
  - Target terms: notch, jacket, gatefold, groove wear, ringwear, label, spindle marks, matrix, runout, deadwax, etc.
  - Parse listing descriptions, condition notes, grading language
  - Extract frequently-used terminology in seller/collector community
  - Identify missing terms in current dataset

- [ ] **Scrape eBay vinyl record listings** for same purpose
  - Parse listing titles and descriptions
  - Identify condition terminology
  - Extract format/packaging terms
  - Cross-reference with Discogs findings

- [ ] Compile unified list of discovered terms
- [ ] Remove duplicates of existing terms
- [ ] Prioritize by frequency of usage
- [ ] Create term files for top 100+ missing terms

### Definition Enhancement
- [ ] Review all 567 terms for definition expansion opportunities
- [ ] Prioritize high-traffic terms first
- [ ] Expand definitions to 50-300 words where appropriate
- [ ] Add historical context where relevant
- [ ] Add cultural significance where relevant
- [ ] Maintain encyclopedia-like tone
- [ ] Keep technical accuracy

## Validation Updates

- [ ] Update `tools/validate.js` for new schema fields
- [ ] Add word count validation for short_definition (≤25 words)
- [ ] Add word count validation for long_definition (50-300 words)
- [ ] Add character count check for summary if retained

## Deployment

- [ ] Merge waxly-2.0 branch to main/master
- [ ] Deploy API to Vercel
- [ ] Configure waxly.music domain
- [ ] Deploy static site to GitHub Pages or Netlify
- [ ] Test all API endpoints in production
- [ ] Verify CORS headers
- [ ] Monitor edge cache performance

## Future Enhancements (Post-2.1)

- [ ] Fuzzy search implementation
- [ ] Bulk export formats (CSV, SQLite)
- [ ] GraphQL API endpoint (if requested)
- [ ] Audio pronunciation files (optional)
- [ ] Historical timeline visualization
