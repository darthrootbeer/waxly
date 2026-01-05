# Waxly 2.1 TODO

Last updated: 2026-01-05

---

## 🔴 High Priority (Required for v2.1)

### Slug Simplification
- [x] **Audit all slugs for verbosity** (259 identified)
- [x] **Generate shortening plan** (3,811 chars savings)
- [x] **Execute slug shortening** (261 files renamed)
- [x] **Update all cross-references** (64 terms updated)
- [x] **Validate after renaming** (0 errors)

### Content Quality - Fix Existing Terms
- [x] **Fix all 567 summaries to be complete sentences**
  - Status: ✅ COMPLETED - All summaries end with . ! or ?
  - Tool: tools/fix-summaries.js (executed)

- [x] **Add pos field to all terms**
  - Status: ✅ COMPLETED - 567/567 terms have part of speech
  - Tool: tools/bulk-add-pos.js (executed)

- [ ] **Expand short definitions to 50+ words**
  - Current: 561/567 terms need expansion
  - Completed: 6 core terms (dead-wax, cartridge, gatefold, jacket, acetate, inner)
  - Target: 150-300 words for core, 50-150 for others
  - Next: Equipment terms, then formats

### Schema Migration
- [x] Update schema to v2.1 with new fields
- [x] Update validation script with word count checks
- [x] Update CONTRIBUTING.md with new guidelines
- [x] Decide backwards compatibility (v2.1 - optional fields)

### Documentation
- [x] Update CHANGELOG.md with v2.1 changes
- [x] Update README.md examples with new schema
- [x] Update docs/API.md with new response fields
- [x] Create TERM_UPDATE_PLAN.md
- [x] Create SCHEMA_ENHANCEMENT_PROPOSAL.md

---

## 🟡 Medium Priority (v2.1+ Content Enhancement)

### Definition Expansion (561 remaining)
- [x] Identify priority terms (tools/prioritize-definitions.js)
- [x] Core concepts (6/6 complete):
  - [x] dead-wax (184 words)
  - [x] cartridge (235 words)
  - [x] gatefold (236 words)
  - [x] jacket (241 words)
  - [x] acetate (233 words)
  - [x] inner (230 words)

- [ ] **Equipment terms** (~30 terms)
  - turntable, tonearm, platter, stylus, headshell
  - preamp, amplifier, speaker
  - Target: 100-200 words each

- [ ] **Format terms** (~40 terms)
  - LP, EP, single, 45, 78, 33rpm
  - vinyl types, weights, sizes
  - Target: 75-150 words each

- [ ] **Collecting terms** (~60 terms)
  - Grading, condition, packaging
  - Target: 50-100 words each

- [ ] **Genre terms** (~200 terms)
  - Keep concise: 30-75 words
  - Basic origin and characteristics

### Metadata Enhancement
- [x] Add `pos` to all terms (567/567 complete)
- [ ] Add `pronunciation` to ambiguous terms (~50 terms)
- [ ] Add `etymology` to historical terms (~100 terms)
- [ ] Add `first_use` dates where known (~100 terms)
- [ ] Add `aliases` where missing (~200 terms)
- [ ] Add `alt_spellings` where applicable (~150 terms)
- [ ] Add `regions` based on content analysis

### Content Expansion - Add Missing Terms
- [ ] **Scrape Discogs listings** for missing terminology
  - Target: notch, ringwear, spindle marks, matrix codes, etc.
  - Parse condition grading language

- [ ] **Scrape eBay vinyl listings**
  - Cross-reference with Discogs
  - Identify collector vernacular

### Site Generator Updates
- [ ] Update templates to display new metadata fields
- [ ] Enhance term page layout for dictionary style
- [ ] Add pronunciation display
- [ ] Add etymology section
- [ ] Show first use dates

---

## 🟢 Low Priority (Future)

### Deployment
- [ ] Deploy API to Vercel
- [ ] Configure waxly.music domain DNS
- [ ] Deploy static site to GitHub Pages
- [ ] Test all API endpoints in production
- [ ] Monitor performance

### Advanced Features
- [ ] Fuzzy search implementation
- [ ] Bulk export formats (CSV, SQLite)
- [ ] GraphQL API endpoint
- [ ] Audio pronunciation files
- [ ] Historical timeline visualization

---

## ✅ Completed This Session

### Infrastructure
- [x] Schema v2.1 with dictionary-style fields (pos, pronunciation, etymology, first_use, alt_spellings)
- [x] Validation enhancements (word count, complete sentences)
- [x] All documentation updated

### Automation Tools Created
- [x] tools/fix-summaries.js
- [x] tools/audit-slugs.js
- [x] tools/shorten-slugs.js
- [x] tools/execute-slug-shortening.js
- [x] tools/bulk-add-pos.js
- [x] tools/prioritize-definitions.js

### Data Quality
- [x] 567/567 summaries fixed (complete sentences)
- [x] 567/567 terms have pos field
- [x] 261/567 slugs shortened (46%)
- [x] 6/567 terms fully enhanced with v2.1 metadata
- [x] 64 cross-references updated

### Documentation
- [x] README.md, CONTRIBUTING.md, CHANGELOG.md, docs/API.md
- [x] TERM_UPDATE_PLAN.md
- [x] SCHEMA_ENHANCEMENT_PROPOSAL.md

---

## 🎯 Next Actions

**Immediate (High Priority):**
1. Expand equipment terms (30 terms @ 100-200 words)
2. Add pronunciation to top 50 ambiguous terms
3. Add etymology to top 100 historical terms
4. Expand format terms (40 terms @ 75-150 words)

**Short Term:**
5. Expand collecting terms (60 terms @ 50-100 words)
6. Bulk add regions field
7. Add first_use dates to historical terms

**Ongoing:**
8. Systematic genre term expansion (200 terms)
9. Vocabulary mining from Discogs/eBay
10. Site template updates for new fields

---

## 📊 Progress Metrics

- **Summaries:** 567/567 (100%) ✅
- **Pos field:** 567/567 (100%) ✅
- **Slugs shortened:** 261/567 (46%) ✅
- **Definitions expanded:** 6/567 (1%)
- **Full v2.1 metadata:** 6/567 (1%)
- **Documentation:** 100% ✅
