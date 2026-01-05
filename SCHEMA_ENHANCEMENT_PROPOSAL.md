# Schema Enhancement Proposal - Waxly 2.1

## Current Schema (v2.0)

**Required fields (7):**
- `slug`, `term`, `summary`, `definition`, `tags`, `created`, `updated`

**Optional fields (4):**
- `aliases`, `see_also`, `regions`

**Total:** 11 fields

---

## Proposed Enhancements

### 1. Alternative Terms/Spellings

**Current state:** We have `aliases` field for alternative names

**User request:** Add distinct field for alternative terms/spellings

**Analysis:**
- `aliases` currently serves this purpose well
- Question: Do we need semantic distinction between:
  - **Aliases**: Different names for same thing (e.g., "acetate" → "lacquer", "reference disc")
  - **Variants**: Spelling variations (e.g., "DJ" → "deejay", "disc jockey")

**Recommendation:**
- **Keep `aliases`** and expand its scope to include both semantic aliases and orthographic variants
- **OR** add new `variants` field specifically for spelling variations
- **Lean toward:** Keep `aliases` only (simpler, already serves the purpose)

**Rationale:** Minimal complexity. The distinction between "alias" and "variant" is often blurry in practice.

---

### 2. Two-Tier Definition Structure

**Current state:**
- `summary` - max 200 chars, one-sentence overview
- `definition` - unlimited length, full explanation

**User request:**
- Short definition: ≤ 25 words
- Long definition: 50–300 words

**Options:**

#### Option A: Repurpose Existing Fields (Backward Compatible)
```json
{
  "summary": "One-sentence overview for metadata/SEO (max 200 chars)",
  "short_definition": "Brief dictionary-style definition (≤25 words)",
  "definition": "Detailed explanation with context (50-300 words)"
}
```
- ✅ Keeps existing `summary` field for its current purpose
- ✅ Adds semantic clarity with `short_definition`
- ✅ Backward compatible (new field is optional initially)
- ❌ Three definition-like fields (might be confusing)

#### Option B: Two-Tier System (Simpler)
```json
{
  "summary": "Brief definition (≤25 words)",
  "definition": "Detailed explanation (50-300 words)"
}
```
- ✅ Clean two-tier system
- ✅ Reuses existing field names
- ✅ Minimal schema change
- ❌ Breaks existing data (summary currently max 200 chars, not word-limited)
- ❌ Requires migration of all 567 terms

#### Option C: Explicit Naming (Most Clear)
```json
{
  "summary": "Meta description for SEO/cards (max 200 chars)",
  "definition_short": "Concise definition (≤25 words)",
  "definition_long": "Extended explanation (50-300 words)"
}
```
- ✅ Extremely clear purpose for each field
- ✅ Allows keeping summary for its current SEO purpose
- ❌ More complex schema
- ❌ Deviates from minimal design principle

**Recommendation: Option A**
- Add `short_definition` as new optional field
- Keep `summary` for current purpose (SEO, social cards, quick context)
- Keep `definition` but add validation for 50-300 word range
- Migrate gradually (make `short_definition` required in v3.0)

---

## Proposed Schema Changes (v2.1)

### New Fields

```json
{
  "short_definition": {
    "type": "string",
    "description": "Brief dictionary-style definition (≤25 words)",
    "maxLength": 175
  }
}
```

### Updated Fields

```json
{
  "definition": {
    "type": "string",
    "description": "Detailed explanation with context (recommended 50-300 words)",
    "minLength": 50
  }
}
```

### Keep Unchanged

- `summary` - Still useful for meta descriptions, social cards, browse pages
- `aliases` - Serves both alternate names and spelling variants

---

## Word Count Validation

**Challenge:** JSON Schema doesn't natively support word count validation

**Solutions:**

1. **Use character limits as proxy:**
   - 25 words ≈ 150-175 characters (avg 6 chars/word)
   - 50 words ≈ 300-350 characters
   - 300 words ≈ 1800-2100 characters

2. **Add custom validation in `tools/validate.js`:**
```javascript
function countWords(text) {
  return text.trim().split(/\s+/).length;
}

function validateDefinitions(term) {
  if (term.short_definition) {
    const words = countWords(term.short_definition);
    if (words > 25) {
      errors.push(`short_definition exceeds 25 words (${words} words)`);
    }
  }

  const defWords = countWords(term.definition);
  if (defWords < 50 || defWords > 300) {
    errors.push(`definition should be 50-300 words (${defWords} words)`);
  }
}
```

**Recommendation:** Use both character limits in schema + word count in validation script

---

## Migration Strategy

### Phase 1: Schema Update (v2.1)
- [ ] Add `short_definition` as optional field
- [ ] Add character limits to definition
- [ ] Update `tools/validate.js` with word count checks
- [ ] Update CONTRIBUTING.md with new guidelines

### Phase 2: Content Migration (Gradual)
- [ ] Start with high-priority terms
- [ ] Add `short_definition` to all terms
- [ ] Ensure `definition` meets 50-300 word target
- [ ] Can be done incrementally over time

### Phase 3: Enforcement (v3.0 - Future)
- [ ] Make `short_definition` required
- [ ] Enforce word count limits strictly
- [ ] Breaking change with migration guide

---

## Final Recommendation

### Schema v2.1 Structure

**Required (7):** slug, term, summary, definition, tags, created, updated

**Optional (5):**
- aliases (expanded scope: alt names + alt spellings)
- see_also
- regions
- **short_definition** ← NEW
- ~~variants~~ (not needed, use aliases)

**Validation:**
- `summary`: max 200 chars (for SEO/social)
- `short_definition`: max 175 chars / ≤25 words (concise definition)
- `definition`: min 300 chars / 50-300 words (detailed explanation)

**Total fields:** 12 (7 required + 5 optional)

**Benefits:**
- ✅ Backward compatible (optional field)
- ✅ Clear semantic purpose for each field
- ✅ Gradual migration possible
- ✅ Maintains minimal design philosophy
- ✅ Supports both quick reference and deep learning use cases

---

## Next Steps

1. Update `dataset/schema/term.schema.json` with v2.1 changes
2. Update `tools/validate.js` with word count validation
3. Update CONTRIBUTING.md with new field guidelines
4. Update API documentation
5. Update site templates to display short_definition
6. Begin migrating existing terms (starting with most-viewed)
