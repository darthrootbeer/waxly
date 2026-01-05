# Waxly - TODO

## Priority 1: Active Development

### Phase 4 - Advanced Features
- [ ] `000023` - Add pronunciation audio support
- [ ] `000024` - Improve filtering UI (by tags / eras / regions)

### Phase 5 - AI & Machine Learning Integration
- [ ] `000092` - Add API endpoints for AI consumption (/api/terms/search, /api/terms/embeddings, /api/terms/graph)
- [ ] `000093` - Create AI training dataset exports in multiple formats (JSON, CSV, TXT, RDF/Turtle)
- [ ] `000094` - Implement semantic embeddings and vector database preparation
- [ ] `000095` - Add contextual keywords and cross-reference mapping for knowledge graph traversal
- [ ] `000096` - Create structured prompts and context-aware formatting for different AI use cases

## Priority 2: Infrastructure & Setup

- [ ] `000025` - Write schema and validator for term front-matter
- [ ] `000026` - Build importer to split current A-Z markdown into term files
- [ ] `000027` - Set up contribution guidelines & issue templates
- [ ] `000028` - Create autolink + redirect scripts
- [ ] `000029` - Add validations and pre-commit hooks
- [ ] `000030` - Migrate full content and generate letter/tag hubs
- [ ] `000031` - Plan JSON API export and pronunciation audio
- [ ] `000032` - Implement comprehensive tagging system for terms (DJ-related, compact disc, 1960s era, etc.)
- [ ] `000033` - Add term popularity field (1-10 scale) to track current usage vs historical terms
- [ ] `000034` - Implement regional terminology field to track geographic variations (East Coast US, Italy, England, etc.)
- [ ] `000035` - Add term complexity level field (beginner/intermediate/advanced/expert) for user skill-based filtering
- [ ] `000036` - Implement term frequency field (rare/common/ubiquitous) to indicate how often term appears in literature/media
- [ ] `000037` - Add term status field (active/archaic/obsolete/revived) to track term lifecycle
- [ ] `000038` - Create term context field (formal/informal/slang/technical/jargon) for usage style classification
- [ ] `000039` - Add term source field (oral tradition/written documentation/industry standard/internet) for origin tracking
- [ ] `000040` - Implement term verification field (verified/unverified/contested/needs_research) for accuracy tracking
- [ ] `000041` - Add term cross-references field (synonyms/antonyms/related_terms/see_also) for comprehensive linking
- [ ] `000042` - Create term examples field (usage_examples/context_examples/quote_examples) for practical understanding
- [ ] `000043` - Add term etymology field (word_origin/language_root/historical_development) for linguistic context
- [ ] `000044` - Implement term pronunciation field (phonetic_spelling/audio_file/regional_variations) for correct usage
- [ ] `000045` - Add term cultural significance field (importance_level/cultural_impact/historical_relevance) for context
- [ ] `000046` - Create term equipment association field (turntables/mixers/records/accessories) for gear-specific terms
- [ ] `000047` - Add term genre association field (hip_hop/electronic/jazz/rock/etc) for music-specific terminology
- [ ] `000048` - Implement term decade field (1940s/1950s/1960s/etc) for historical period classification
- [ ] `000049` - Add term user rating field (1-5 stars) for community quality assessment
- [ ] `000050` - Create term last_updated field (timestamp) for content freshness tracking
- [ ] `000051` - Add term contributor field (author/editor/reviewer) for attribution and quality control
- [ ] `000052` - Implement term discussion field (comments/notes/controversies) for community input
- [ ] `000053` - Add term media field (images/videos/audio_clips/diagrams) for multimedia content
- [ ] `000054` - Create term bibliography field (sources/references/citations) for academic rigor
- [ ] `000055` - Add term translation field (translations/equivalents) for multilingual support
- [ ] `000056` - Implement term usage notes field (warnings/cautions/important_info) for practical guidance

## Priority 3: Future Enhancements

### UX & Interface Improvements
- [ ] `000057` - Dark/light theme toggle
- [ ] `000058` - Permalinks with stable slugs
- [ ] `000059` - Related-terms card per entry
- [ ] `000060` - Faceted search for tags/domains/eras
- [ ] `000061` - Copy-code buttons for technical terms
- [ ] `000097` - Visual popularity indicator bars: Color-coded bars (red=1-2, golden=5, green=8-10) showing term popularity on 1-10 scale for quick visual reference

### Content Expansions
- [ ] `000062` - Add more detailed technical specifications for equipment terms
- [ ] `000063` - Expand cultural context and historical notes
- [ ] `000064` - Include audio examples where relevant

### Major Spin-off Project: Record Label Universe
- [ ] `000065` - Create comprehensive record label database (Capitol, Columbia, independent labels, etc.)
- [ ] `000066` - Design interactive, zoomable map interface for record label relationships
- [ ] `000067` - Implement parent/subsidiary label relationship mapping
- [ ] `000068` - Add label timeline and historical evolution tracking
- [ ] `000069` - Create contribution system for community label submissions
- [ ] `000070` - Build search and filtering system for label discovery
- [ ] `000071` - Implement label relationship visualization (mergers, acquisitions, splits)
- [ ] `000072` - Add label geographic distribution mapping
- [ ] `000073` - Create label genre and artist association system
- [ ] `000074` - Develop label discography integration
- [ ] `000075` - Plan separate repository and hosting for Record Label Universe project

### Community & Governance
- [ ] `000076` - Set up small council with clear dispute-resolution policy
- [ ] `000077` - Add community discussion forums
- [ ] `000078` - Create contributor onboarding guide
- [ ] `000079` - Document deployment and hosting procedures

### Advanced Features
- [ ] `000080` - Add bookmarking and favorites functionality
- [ ] `000081` - Create mobile app version
- [ ] `000082` - Add social sharing capabilities
- [ ] `000083` - Implement automated testing for content quality

---

## Completed Tasks

### MVP Phase (Completed 2025-10-06)
- [x] `000008` - **RESTRUCTURE PROJECT**: Migrate from book/chapter model to wiki-style database architecture - (2025-10-06_16.45.00)
- [x] `000009` - Create new repo structure: `data/`, `docs/`, `scripts/`, `schema/`, `api/` directories - (2025-10-06_16.45.00)
- [x] `000010` - Implement one-term-per-file structure with rich front-matter metadata - (2025-10-06_16.45.00)
- [x] `000011` - Create term validation schema and data integrity system - (2025-10-06_15.30.00)
- [x] `00002A` - Extend schema with advanced metadata fields - (2025-10-06_15.30.00)
- [x] `00002B` - Create field visibility system with global defaults and per-term overrides - (2025-10-06_15.30.00)
- [x] `00002C` - Implement Discogs genre/style taxonomy - (2025-10-06_15.45.00)
- [x] `00002D` - Clean up slugs and term names (270 terms processed) - (2025-10-06_16.45.00)
- [x] `00002E` - Comprehensive project cleanup (~25MB saved) - (2025-10-06_16.45.00)
- [x] `00002F` - Create media implementation guide and Discogs taxonomy documentation - (2025-10-06_16.45.00)
- [x] `000012` - Set up MkDocs with Material theme and Pagefind search - (2025-10-06_21.30.00)
- [x] `000013` - ~~Deploy to GitHub Pages with CI/CD pipeline~~ (Cancelled - using local development only)

### Content Migration (Completed 2025-10-06)
- [x] `000014` - Split remaining letters into one-term-per-file structure - (2025-10-06_21.30.00)
- [x] `000015` - Run validator to fill missing front-matter - (2025-10-06_21.30.00)
- [x] `000016` - Generate letter and tag hubs automatically - (2025-10-06_21.30.00)
- [x] `000017` - Implement autolinking script for cross-references - (2025-10-06_21.30.00)

### Contributor Experience (Completed 2025-10-06)
- [x] `000018` - Refine contributor documentation - (2025-10-06_21.45.00)
- [x] `000019` - Add pre-commit hooks and validations - (2025-10-06_21.45.00)
- [x] `000020` - Set up aliases → redirects system - (2025-10-06_21.45.00)
- [x] `000021` - Add related-terms sidebar - (2025-10-06_21.45.00)

### Advanced Features (Completed 2025-10-06 - 2025-10-07)
- [x] `000022` - Expose JSON export of all terms (/api/terms.json) - (2025-10-06_21.45.00)
- [x] `000084` - Create Discogs genre/style reference system - (2025-10-06_22.00.00)
- [x] `000085` - Investigate Discogs API integration - (2025-10-06_22.00.00)
- [x] `000086` - Implement genre/style pages linking to Discogs - (2025-10-06_22.00.00)
- [x] `000087` - Add Discogs URL fields to schema - (2025-10-06_22.00.00)
- [x] `000088` - Add AI-friendly metadata fields to schema - (2025-10-06_22.15.00)
- [x] `000089` - Implement JSON-LD structured data - (2025-10-06_22.15.00)
- [x] `000090` - Create copy-as-markdown functionality - (2025-10-06_22.15.00)
- [x] `000091` - Build machine-readable entity relationships - (2025-10-06_22.15.00)
- [x] `000099` - Expand historical coverage to 1857 - (2025-10-07_10.15.00)
- [x] `000098` - Simplify site to Wikipedia-style resource - (2025-10-07_10.00.00)

### Discogs Integration (Completed 2025-10-06)
- [x] `000013` - Create individual lexicon entries for each Discogs genre (16 entries) - (2025-10-06_21.04.00)
- [x] `000014` - Create individual lexicon entries for each Discogs style (80 entries) - (2025-10-06_21.04.00)
- [x] `000015` - Set up Discogs API integration framework - (2025-10-06_21.04.00)
- [x] `000016` - Update schema to reference genre/style entries - (2025-10-06_21.04.00)

### Cultural Sensitivity (Completed 2025-10-06)
- [x] `000017` - Update cultural sensitivity system for inappropriate terms - (2025-10-06_21.09.00)
- [x] `000018` - Add content obscuration/reveal functionality - (2025-10-06_21.09.00)
- [x] `000019` - Update schema for sensitive content handling - (2025-10-06_21.09.00)
- [x] `000020` - Create user preference system for sensitive content - (2025-10-06_21.09.00)
- [x] `000021` - Add age verification checkbox for 18+ content - (2025-10-06_21.09.00)
- [x] `000022` - Implement persistent user preferences with localStorage - (2025-10-06_21.09.00)
- [x] `000023` - Update sensitive content template to respect preferences - (2025-10-06_21.09.00)

### Initial Project Setup (Completed 2025-01-27)
- [x] `000001` - Create project structure with best practices - (2025-01-27_14.30.00)
- [x] `000002` - Set up standard documentation files - (2025-01-27_14.35.00)
- [x] `000003` - Organize content into structured book format - (2025-01-27_14.40.00)
- [x] `000004` - Create assets directory - (2025-01-27_14.45.00)
- [x] `000005` - Set up tools directory - (2025-01-27_14.50.00)
- [x] `000006` - Initialize Git repository - (2025-01-27_14.55.00)
- [x] `000007` - Create web presentation layer - (2025-01-27_15.00.00)

---

**Last Updated**: 2025-12-11
