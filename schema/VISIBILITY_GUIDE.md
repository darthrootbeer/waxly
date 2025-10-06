# Field Visibility System

## Overview

The Vinyl Lexicon uses a two-level visibility system to control which fields appear in term entries. This keeps common terms clean while allowing rich metadata for terms that need it.

## How It Works

### Level 1: Global Defaults (`field_visibility.yml`)

The `field_visibility.yml` file defines which fields show by default:

- **Core fields** — Always visible (term, slug, pos, summary, updated)
- **Default visible** — Standard fields shown on most terms
- **Default hidden** — Advanced fields hidden unless enabled
- **Advanced sections** — Rich metadata sections (off by default)

### Level 2: Per-Term Overrides

Individual terms can customize visibility using two optional fields:

#### `visible_sections`

Enable additional sections beyond the defaults:

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

Hide default-visible sections:

```yaml
---
term: Test Pressing
hidden_sections:
  - popularity
  - regions
---
```

## Field Categories

### Core Fields (Always Visible)

- `term` — The canonical term name
- `slug` — URL identifier
- `pos` — Part of speech
- `summary` — Brief definition
- `updated` — Last modified date

### Default Visible Fields

- `aliases` — Alternative names
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

### Default Hidden Fields

> **Note on Genres & Styles**: The Vinyl Lexicon follows the [Discogs genre/style taxonomy](https://www.discogs.com/). Genres are broad categories (Rock, Electronic, Jazz, etc.) with 1-3 per term typical. Styles are more specific sub-genres (Krautrock, Ambient, Bebop, etc.) with 1-6 per term typical. This ensures consistency with the world's largest music database.

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
- `genres` — Discogs-style genre classification (1-3 max)
- `styles` — Discogs-style sub-genre classification (1-6 max)

### Advanced Sections (Hidden by Default)

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

## Usage Examples

### Minimal Term (Uses All Defaults)

```yaml
---
term: Vinyl
slug: vinyl
pos: noun
summary: A synthetic plastic material used to manufacture phonograph records.
updated: '2025-10-06'
---
```

### Rich Equipment Term (Shows Technical Details)

```yaml
---
term: Gatefold
slug: gatefold
pos: noun
summary: A record jacket that opens like a book, revealing inside artwork.
updated: '2025-10-06'
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
updated: '2025-10-06'
context: slang
hidden_sections:
  - complexity
  - verification
  - domains
---
```

## Conditional Visibility Rules

The `field_visibility.yml` file includes display rules that automatically suggest sections based on tags/domains:

- **Technical specs** → equipment, pressing, technical terms
- **Market data** → collecting, historical terms
- **Cultural impact** → historical, cultural, collecting terms
- **Quality indicators** → collecting, quality-control terms

These are suggestions; actual visibility must be explicitly set via `visible_sections`.

## Best Practices

1. **Start minimal** — Only enable sections when you have content for them
2. **Be consistent** — Similar terms should have similar sections enabled
3. **Think user-first** — Show what readers need, hide expert metadata unless relevant
4. **Use relationships** — Connect related concepts with parent/child/requires/enables
5. **Add media** — Include images/diagrams for equipment and physical items
6. **Document sources** — Use bibliography for academic/historical claims
7. **Keep it maintainable** — Don't enable all sections just because they exist

## Schema Validation

All terms must validate against `term.schema.json`. The visibility system doesn't change validation—it only affects display.

Optional fields can be:

- Included in YAML frontmatter but hidden via `hidden_sections`
- Omitted from YAML entirely (defaults to hidden)
- Explicitly shown via `visible_sections`

## Implementation Notes

For developers building the display layer:

1. Load `field_visibility.yml` to get global defaults
2. Parse term frontmatter
3. Merge visibility rules:

   ```text
   visible = (core + default_visible + term.visible_sections) - term.hidden_sections
   ```

4. Only render fields/sections that are in the final `visible` set
5. Respect conditional rules as suggestions in the UI (e.g., "Add technical specs?")
