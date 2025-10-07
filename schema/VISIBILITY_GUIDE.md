# Field Visibility System

## Overview

The Vinyl Lexicon uses a two-level visibility system to control which fields appear in term entries. This keeps common terms clean while allowing rich metadata for terms that need it.

## How It Works

### Level 1: Global Defaults (`field_visibility.yml`)

The `field_visibility.yml` file defines which fields show by default:

- **Core fields** — Always visible (term, slug, pos, summary, updated)
- **Default visible** — All standard and advanced fields are visible by default
- **Default hidden** — Currently empty (all fields visible by default)
- **Advanced sections** — All rich metadata sections are visible by default

### Level 2: Per-Term Overrides

Individual terms can customize visibility using two optional fields:

#### `visible_sections`

Since all sections are now visible by default, this field is primarily used for explicit confirmation or special cases:

```yaml
---
term: Gatefold
visible_sections:
  - technical_specs
  - cultural_impact
  - market_data
---
```

#### `hidden_sections`

Hide specific sections for terms where they're not relevant:

```yaml
---
term: Test Pressing
hidden_sections:
  - market_data
  - cultural_impact
---
```

## Field Categories

### Core Fields (Always Visible)

- `term` — The canonical term name
- `slug` — URL identifier
- `pos` — Part of speech
- `summary` — Brief definition
- `created` — Creation date and time (ISO-8601 format with timezone)
- `updated` — Last modified date and time (ISO-8601 format with timezone)

### All Fields Now Visible by Default

All the following fields are now visible by default unless explicitly hidden via `hidden_sections`:

- `aliases` — Alternative names
- `aka` — Also known as (alternate terms)
- `tags` — Category tags
- `domains` — Technical domains
- `regions` — Geographic usage
- `eras` — Time periods
- `see_also` — Related terms
- `sources` — References
- `popularity` — Usage frequency (1-10)
- `complexity` — Skill level
- `status` — Term lifecycle
- `context` — Usage style
- `verification` — Accuracy status
- `first_attested` — First documented use
- `pronunciation` — Phonetic guide
- `decade` — Primary decade
- `user_rating` — Community rating
- `contributor` — Author
- `discussion` — Community notes
- `media` — Images/diagrams
- `bibliography` — Academic sources
- `translation` — Foreign equivalents
- `usage_notes` — Warnings/tips
- `equipment_association` — Related gear
- `genres` — References to genre entries in the lexicon (1-3 max)
- `styles` — References to style entries in the lexicon (1-6 max)
- `cultural_sensitivity` — Content warnings and sensitivity information
- `regional_variations` — Regional names, variations, and slang terms

> **Note on Genres & Styles**: The Vinyl Lexicon follows the [Discogs genre/style taxonomy](https://www.discogs.com/) by creating individual entries for each genre and style. Each genre (Rock, Electronic, Jazz, etc.) and style (Ambient, Bebop, Progressive Rock, etc.) has its own lexicon entry with full definitions and context. Terms reference these entries by their slugs (e.g., `genres: ["electronic", "jazz"]` and `styles: ["ambient", "bebop"]`). This ensures consistency with the world's largest music database while providing rich, detailed definitions for each classification.

### Advanced Sections (Now Visible by Default)

#### `technical_specs`

Physical and manufacturing details:

- `dimensions` — Physical size
- `materials` — Construction materials
- `manufacturing_process` — How it's made
- `cost_impact` — Effect on price

#### `historical_timeline`

Historical context:

- `introduction_year` — When introduced
- `peak_usage_era` — Most popular period
- `decline_era` — When usage dropped
- `revival_era` — When it came back
- `notable_examples` — Famous instances

#### `cultural_impact`

Collector information:

- `collector_value` — Value to collectors (none, low, moderate, high, very_high, varies)
- `rarity_factor` — How rare (very_common → very_rare, varies)
- `condition_sensitivity` — Impact of condition (low → very_high)
- `preservation_notes` — Care instructions

#### `cultural_sensitivity`

Content warnings and sensitivity information for terms that may contain inappropriate, offensive, or culturally sensitive language:

- `has_sensitive_content` — Whether this term contains culturally sensitive content (boolean)
- `sensitivity_level` — Level of concern (mild, moderate, high, very_high)
- `sensitivity_types` — Types of sensitivity (racial, ethnic, gender, sexual, religious, ableist, classist, ageist, historical_bias, outdated_terminology, offensive_slang, derogatory)
- `content_warning` — Specific warning message for users
- `historical_context` — Historical context explaining why this term is problematic
- `modern_alternatives` — Modern, appropriate alternatives to this term
- `obscuration_method` — How to obscure sensitive content (blur, censor, hover_reveal, click_reveal, expandable, none)
- `age_restricted` — Whether this content requires 18+ age verification (boolean)

**Important:** The Vinyl Lexicon includes historically accurate terms even when they contain inappropriate language. This is done for educational and historical purposes, but with clear warnings and modern alternatives provided. Users can control their display preferences including age verification for mature content.

#### `relationships`

Concept connections:

- `parent_concept` — Broader concept
- `child_concepts` — Narrower concepts
- `requires` — Prerequisites
- `enables` — What this enables
- `conflicts_with` — Incompatible concepts

#### `usage_context`

When and how to use:

- `primary_use_cases` — Main scenarios
- `secondary_use_cases` — Alternative uses
- `avoid_when` — When NOT to use
- `best_practices` — Recommendations

#### `quality_indicators`

Grading and authentication:

- `grading_factors` — What to assess
- `common_defects` — Typical problems
- `restoration_possible` — Can it be fixed? (boolean)
- `authenticity_marks` — Genuine indicators

#### `market_data`

Commercial information:

- `price_premium` — Cost difference
- `market_demand` — Current demand (very_low → very_high, varies)
- `investment_potential` — Investment grade (poor, fair, good, excellent, varies)
- `reproduction_quality` — Reissue quality

#### `advanced_search`

Enhanced discoverability:

- `search_keywords` — Extra search terms
- `related_artists` — Associated artists
- `related_labels` — Associated labels

### Regional Variations

Regional names and variations for terms that have different names in different geographic areas:

```yaml
regional_variations:
  - region: UK
    term: "Wax"
    usage_context: slang
    notes: "Common British slang for vinyl records"
  - region: JA
    term: "レコード盤"
    usage_context: formal
    notes: "Japanese term for record disc"
  - region: DE
    term: "Platte"
    usage_context: informal
    notes: "German informal term for records"
```

Each regional variation includes:
- `region` — Geographic area (US, UK, JA, DE, FR, IT, ES, CA, AU, BR, MX, global, other)
- `term` — The regional name or variation
- `notes` — Additional context about usage
- `usage_context` — Formality level (formal, informal, slang, technical, historical)

### Datetime Fields

The `created` and `updated` fields use ISO-8601 format with timezone information for precise timestamp tracking:

```yaml
created: "2025-01-27T14:30:45.123Z"
updated: "2025-01-27T16:45:22.456-05:00"
```

**Format examples:**
- `2025-01-27T14:30:45Z` — UTC timezone
- `2025-01-27T14:30:45.123Z` — UTC with milliseconds
- `2025-01-27T14:30:45-05:00` — EST timezone
- `2025-01-27T14:30:45+09:00` — JST timezone

**Benefits:**
- **Precise tracking** — Exact creation and modification times
- **Timezone awareness** — Handles contributors from different timezones
- **Sortable** — Chronological ordering across all terms
- **Audit trail** — Complete history of term evolution

## Usage Examples

### Minimal Term (Uses All Defaults)

```yaml
---
term: Vinyl
slug: vinyl
pos: noun
summary: A synthetic plastic material used to manufacture phonograph records.
created: "2025-01-27T14:30:45Z"
updated: "2025-01-27T16:45:22Z"
---
```

### Rich Equipment Term (Shows Technical Details)

```yaml
---
term: Gatefold
slug: gatefold
pos: noun
summary: A record jacket that opens like a book, revealing inside artwork.
created: "2025-01-27T14:30:45Z"
updated: "2025-01-27T16:45:22Z"
visible_sections:
  - technical_specs
  - cultural_impact
  - market_data
technical_specs:
  dimensions: "12.375 x 12.375 inches (standard LP gatefold)"
  materials: ["cardboard", "paper", "glue"]
  manufacturing_process: "Die-cut and folded construction"
  cost_impact: "10-25% higher than standard jacket"
cultural_impact:
  collector_value: high
  rarity_factor: varies
  condition_sensitivity: high
  preservation_notes: "Store flat to prevent creasing"
cultural_sensitivity:
  has_sensitive_content: false
market_data:
  price_premium: "10-25% over standard jacket"
  market_demand: high
  investment_potential: good
---
```

### Slang Term (Hide Some Defaults)

```yaml
---
term: Wax
slug: wax
pos: noun
summary: Slang term for a vinyl record.
created: "2025-01-27T14:30:45Z"
updated: "2025-01-27T16:45:22Z"
context: slang
hidden_sections:
  - complexity
  - verification
  - domains
---
```

### Term with Sensitive Content

```yaml
---
term: "Race Record"
slug: "race-record"
pos: "noun"
summary: "**Race Record** — Historical term for records marketed to African American audiences"
created: "2024-01-15T10:30:00Z"
updated: "2024-01-15T10:30:00Z"
tags: [historical, marketing, cultural]
domains: [cultural, historical]
regions: [US]
eras: [1920s-1960s]
popularity: 3
complexity: intermediate
status: historical
context: formal
verification: verified
equipment_association: []
genres: ["blues", "jazz", "soul", "rhythm-and-blues"]
styles: ["chicago-blues", "delta-blues", "motown"]
first_attested: "1920s"
historical_context: "Term used by record companies to categorize and market music to African American consumers"
cultural_sensitivity:
  has_sensitive_content: true
  sensitivity_level: high
  sensitivity_types: ["racial", "historical_bias", "outdated_terminology"]
  content_warning: "This term contains historically racist language used in music industry marketing"
  historical_context: "This term emerged from a time when the music industry segregated marketing by race, using offensive terminology to categorize audiences"
  modern_alternatives: ["urban music", "rhythm and blues", "soul music", "African American music"]
  obscuration_method: "click_reveal"
  age_restricted: false
---
```

## Conditional Visibility Rules

The `field_visibility.yml` file includes display rules that can be used for highlighting or special styling based on content relevance:

- **Technical specs** → equipment, pressing, technical terms
- **Market data** → collecting, historical terms
- **Cultural impact** → historical, cultural, collecting terms
- **Quality indicators** → collecting, quality-control terms

Since all fields are now visible by default, these rules serve as UI hints for highlighting relevant sections rather than controlling visibility.

## Best Practices

1. **Hide irrelevant sections** — Use `hidden_sections` to hide fields that don't apply to specific terms
2. **Be consistent** — Similar terms should have similar visibility settings
3. **Think user-first** — Show what readers need, hide sections that don't add value
4. **Use relationships** — Connect related concepts with parent/child/requires/enables
5. **Add media** — Include images/diagrams for equipment and physical items
6. **Document sources** — Use bibliography for academic/historical claims
7. **Keep it maintainable** — Only hide sections when they truly don't apply

## Schema Validation

All terms must validate against `term.schema.json`. The visibility system doesn't change validation—it only affects display.

Optional fields can be:

- Included in YAML frontmatter and visible by default
- Omitted from YAML entirely (field won't appear)
- Hidden via `hidden_sections` if not relevant to the term

## Implementation Notes

For developers building the display layer:

1. Load `field_visibility.yml` to get global defaults
2. Parse term frontmatter
3. Merge visibility rules:

   ```text
   visible = (core + default_visible + advanced_sections) - term.hidden_sections
   ```

4. Only render fields/sections that are in the final `visible` set
5. Respect conditional rules as suggestions in the UI (e.g., "Add technical specs?")
