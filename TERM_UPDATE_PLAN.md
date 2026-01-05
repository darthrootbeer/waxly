# Term Update Execution Plan

## Overview

Update all 567 terms to meet v2.1 schema quality standards.

## Phases

### Phase 1: Core Concepts Enhancement (Priority: HIGH)
**Target: 6 terms**

Enhance core foundational terms with complete v2.1 metadata:
- [x] dead-wax (COMPLETED - example)
- [ ] cartridge
- [ ] fidelity
- [ ] inner-sleeve
- [ ] gatefold
- [ ] jacket

**For each term:**
- Add `pos` (part of speech)
- Add `pronunciation` (IPA)
- Expand definition to 150-300 words with history/context
- Add `aliases` (alternative names)
- Add `alt_spellings` (spelling variants)
- Add `etymology` (origin/history)
- Add `first_use` (year)
- Update `see_also` with relevant cross-references
- Add/update `regions`

### Phase 2: Fix Broken Summaries (Priority: HIGH)
**Target: ~50 terms with incomplete summaries**

Terms with truncated or malformed summaries:
- Summaries ending mid-sentence
- Summaries with embedded formatting (`**noun**`)
- Summaries that are actually definitions

**Actions:**
- Extract clean summary from definition
- Move part-of-speech to `pos` field
- Ensure summary is ≤25 words, complete sentence

### Phase 3: Critical Equipment Terms (Priority: MEDIUM-HIGH)
**Target: ~30 terms**

Essential vinyl equipment terms:
- turntable, tonearm, platter, stylus, needle
- preamp, amplifier, speaker, headphone
- pressing, mastering, cutting, lacquer

**Actions:**
- Expand to 100-200 words
- Add technical metadata
- Include usage context

### Phase 4: Format & Media Terms (Priority: MEDIUM)
**Target: ~40 terms**

Record formats and media types:
- LP, EP, single, 45, 78, 33rpm
- vinyl types, pressing weights
- disc formats, sizes

**Actions:**
- Expand to 75-150 words
- Add historical context
- Include regional variations

### Phase 5: Collecting & Grading Terms (Priority: MEDIUM)
**Target: ~60 terms**

Collector terminology:
- Grading terms (mint, VG, etc.)
- Condition descriptors
- Packaging terms

**Actions:**
- Expand to 50-100 words
- Add usage examples
- Include regional differences

### Phase 6: Genre Terms (Priority: LOW)
**Target: ~200 terms**

Music genre definitions:
- Simple genre terms (jazz, rock, blues, etc.)
- Can remain concise (30-75 words)

**Actions:**
- Add `pos`: "noun"
- Basic expansion with origin/characteristics
- Minimal metadata

### Phase 7: Bulk Automated Enhancements (Priority: ONGOING)
**Target: All terms**

Automated improvements that can be applied to all terms:

1. **Add `pos` field where obvious:**
   - Default most terms to "noun"
   - Set phrases to "phrase"
   - Set actions to "verb"

2. **Add `alt_spellings` from aliases where appropriate:**
   - Identify spelling variants vs semantic aliases
   - Split into correct fields

3. **Add `regions` based on content:**
   - US/UK/JA based on definition mentions
   - International for universal terms

## Execution Strategy

### Batch 1: Manual Enhancement (Today)
- Complete 6 core concepts
- Fix 20 broken summaries
- Validate results

### Batch 2: Semi-Automated (Next)
- Create enhancement script for pos field
- Create script to detect and fix broken summaries
- Bulk add regions based on heuristics

### Batch 3: Systematic Categories
- Work through equipment → formats → collecting → genres
- 20-30 terms per batch
- Commit and validate each batch

## Success Metrics

- [ ] All terms have `pos` field
- [ ] All summaries are complete sentences
- [ ] Core concepts: 150-300 words
- [ ] Equipment terms: 100-200 words
- [ ] Other terms: 50-150 words
- [ ] High-value terms have etymology and first_use
- [ ] All terms validated successfully

## Tools to Create

1. `tools/add-pos-field.js` - Bulk add part-of-speech
2. `tools/fix-broken-summaries.js` - Detect and fix truncated summaries
3. `tools/add-regions.js` - Add region tags based on content
4. `tools/validate-enhanced.js` - Comprehensive validation for enhanced terms

## Estimated Completion

- Phase 1-2: Today (6 + 20 terms)
- Phase 3-5: Ongoing (130 terms)
- Phase 6-7: Bulk operations (441 terms)
