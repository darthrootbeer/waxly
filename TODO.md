# Waxly 2.1 TODO

Tasks organized by priority for v2.1 release and beyond.

---

## 🔴 High Priority (Required for v2.1)

### Content Quality - Fix Existing Terms
- [ ] **Fix all 567 summaries to be complete sentences**
  - Current: Most summaries missing punctuation
  - Required: All summaries must end with . ! or ?
  - Script: Batch update or manual review

- [ ] **Expand short definitions to 50+ words**
  - Current: Many definitions are 2-20 words
  - Target: 50-300 words with context and history
  - Priority: Start with most-viewed/core terms

### Schema Migration
- [x] Update schema to v2.1 with new fields
- [x] Update validation script with word count checks
- [x] Update CONTRIBUTING.md with new guidelines
- [ ] Decide backwards compatibility strategy
  - Make new fields optional (v2.1 - backward compatible)
  - OR require all fields (v3.0 - breaking change)

### Documentation
- [ ] Update CHANGELOG.md with v2.1 changes
- [ ] Update README.md examples with new schema
- [ ] Update docs/API.md with new response fields

---

## 🟡 Medium Priority (Important for v2.1+)

### Content Expansion - Add Missing Terms
- [ ] **Scrape Discogs listings** for missing terminology
  - Target: 100+ most common descriptive terms
  - Focus: notch, jacket, gatefold, groove wear, ringwear, label, spindle marks, matrix, runout, deadwax, shrink wrap, obi, insert, pressing plant codes
  - Parse: Condition grading, format descriptions, pressing details

- [ ] **Scrape eBay vinyl listings** for same purpose
  - Cross-reference with Discogs findings
  - Identify seller/collector vernacular
  - Extract packaging and condition terminology

- [ ] **Compile and prioritize discovered terms**
  - Remove duplicates
  - Sort by frequency
  - Create term files for top 100+ missing terms

### Metadata Enhancement
- [ ] Add `pos` (part of speech) to all terms
  - Identify: noun, verb, adjective, adverb, phrase
  - Priority: Core terms first

- [ ] Add `pronunciation` for ambiguous terms
  - IPA notation preferred
  - Focus on terms with unclear pronunciation

- [ ] Add `etymology` for historical terms
  - Research origins
  - Focus on pre-1960s terminology

- [ ] Add `first_use` dates where known
  - Research historical usage
  - Document sources

### Site Generator Updates
- [ ] Update templates to display new metadata
  - Show part of speech
  - Display pronunciation
  - Include etymology
  - Show first use date

- [ ] Enhance term page layout for dictionary style

---

## 🟢 Low Priority (Future / Nice-to-Have)

### Deployment
- [ ] Merge waxly-2.0 branch to main/master
- [ ] Deploy API to Vercel
- [ ] Configure waxly.music domain DNS
- [ ] Deploy static site to GitHub Pages or Netlify
- [ ] Test all API endpoints in production
- [ ] Verify CORS headers
- [ ] Monitor edge cache performance

### Advanced Features (Post-v2.1)
- [ ] Fuzzy search implementation
- [ ] Bulk export formats (CSV, SQLite, JSON-LD)
- [ ] GraphQL API endpoint
- [ ] Audio pronunciation files (.mp3/.ogg)
- [ ] Historical timeline visualization
- [ ] Interactive term relationship graph
- [ ] Multi-language support (community-driven)

### Community Features
- [ ] GitHub Discussions setup
- [ ] Contribution guidelines refinement
- [ ] Term suggestion template
- [ ] Community recognition system

---

## 📋 Completed

- [x] Schema v2.1 design and implementation
- [x] Add dictionary-style metadata fields (pos, pronunciation, etymology, first_use)
- [x] Expand `aliases` to include variants and spellings
- [x] Update validation script with word count and sentence checks
- [x] Create SCHEMA_ENHANCEMENT_PROPOSAL.md
- [x] Update CONTRIBUTING.md with new field examples
- [x] Add complete sentence validation for summaries
- [x] Add definition word count warnings

---

## 🎯 Current Focus

**Immediate next steps:**
1. Fix all 567 summaries (add punctuation)
2. Expand short definitions (prioritize core 50 terms)
3. Update CHANGELOG for v2.1
4. Begin Discogs vocabulary mining

**Blocked/Waiting:**
- None

**In Progress:**
- Documentation updates
