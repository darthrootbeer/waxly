# Discogs Genre & Style Taxonomy Reference

The Vinyl Lexicon uses the [Discogs taxonomy](https://www.discogs.com/) for genre and style classification. This ensures consistency with the world's largest music database and provides a standardized vocabulary for categorizing music-related terms.

> **Discogs as Gold Standard**: Discogs is the authoritative source for genre and style definitions. When creating or editing terms that reference music genres or styles, always defer to Discogs' official definitions, descriptions, and categorizations. Link directly to Discogs genre/style pages when possible.

## How It Works

### Genre > Style Hierarchy

- **Genres** are broad categories (e.g., Rock, Electronic, Jazz)
- **Styles** are specific sub-genres within those categories (e.g., Krautrock, Ambient, Bebop)
- A term typically has **1-3 genres** and **1-6 styles**

## Official Discogs Genres

The following 16 genres are recognized by Discogs:

1. **Blues** — [View on Discogs](https://www.discogs.com/genre/blues)
2. **Brass & Military** — [View on Discogs](https://www.discogs.com/genre/brass-military)
3. **Children's** — [View on Discogs](https://www.discogs.com/genre/childrens)
4. **Classical** — [View on Discogs](https://www.discogs.com/genre/classical)
5. **Electronic** — [View on Discogs](https://www.discogs.com/genre/electronic)
6. **Folk, World, & Country** — [View on Discogs](https://www.discogs.com/genre/folk-world-country)
7. **Funk / Soul** — [View on Discogs](https://www.discogs.com/genre/funk-soul)
8. **Hip Hop** — [View on Discogs](https://www.discogs.com/genre/hip-hop)
9. **Jazz** — [View on Discogs](https://www.discogs.com/genre/jazz)
10. **Latin** — [View on Discogs](https://www.discogs.com/genre/latin)
11. **Non-Music** — [View on Discogs](https://www.discogs.com/genre/non-music) (spoken word, audiobooks, field recordings)
12. **Pop** — [View on Discogs](https://www.discogs.com/genre/pop)
13. **Reggae** — [View on Discogs](https://www.discogs.com/genre/reggae)
14. **Rock** — [View on Discogs](https://www.discogs.com/genre/rock)
15. **Stage & Screen** — [View on Discogs](https://www.discogs.com/genre/stage-screen) (soundtracks, musicals)
16. **All** — Use when a term applies universally across all genres

## Common Styles by Genre

Below are some frequently used styles within each genre. For the complete list, visit the genre pages on Discogs.

### Blues

- Chicago Blues
- Delta Blues
- Electric Blues
- Country Blues
- Texas Blues

### Brass & Military

- Marches
- Brass Band

### Classical

- Baroque
- Romantic
- Contemporary
- Opera
- Symphony

### Electronic

- Ambient
- Techno
- House
- Drum and Bass
- IDM (Intelligent Dance Music)
- Downtempo
- Dubstep
- Electro
- Trance
- Breakbeat

### Folk, World, & Country

- Country
- Bluegrass
- Celtic
- Americana
- World Music
- Folk Rock

### Funk / Soul

- Funk
- Soul
- Disco
- Boogie
- P.Funk
- Go-Go

### Hip Hop

- Boom Bap
- Trap
- Gangsta
- Conscious
- Turntablism
- DJ Battle Tool

### Jazz

- Bebop
- Swing
- Free Jazz
- Fusion
- Hard Bop
- Modal
- Cool Jazz

### Latin

- Salsa
- Bossa Nova
- Samba
- Cumbia
- Reggaeton
- Tango

### Pop

- Synth-pop
- Europop
- K-pop
- Bubblegum
- Teen Pop

### Reggae

- Dub
- Roots Reggae
- Dancehall
- Ska
- Rocksteady

### Rock

- Krautrock
- Psychedelic Rock
- Hard Rock
- Prog Rock
- Punk
- Post-Punk
- Alternative Rock
- Indie Rock
- Grunge
- Heavy Metal
- Stoner Rock

### Stage & Screen

- Soundtrack
- Musical
- Score
- Theme

### Non-Music

- Spoken Word
- Interview
- Field Recording
- Poetry
- Audiobook
- Sound Effects

## Usage in Vinyl Lexicon

### When to Use Genres/Styles

Apply genres and styles to terms when:

- The term is **genre-specific** (e.g., "Breakbeat" is Hip Hop/Electronic styles)
- The term has **strong associations** with certain genres (e.g., "DJ Battle Tool" with Hip Hop)
- The term originated in or is primarily used within specific genres

### When to Use "All"

Use the "all" genre for:

- **Universal equipment** (turntable, cartridge, tonearm)
- **Universal pressing terms** (vinyl, lacquer, matrix)
- **Universal collecting terms** (mint condition, first pressing)
- **Technical terms** that apply across all music

### Examples

**Genre-Specific Term:**

```yaml
term: Breakbeat
genres:
  - Hip Hop
  - Electronic
styles:
  - Breakbeat
  - Drum and Bass
  - Jungle
```

**Universal Term:**

```yaml
term: Gatefold
genres:
  - all
# No styles needed - applies universally
```

**Multi-Genre Term:**

```yaml
term: Dub Plate
genres:
  - Electronic
  - Hip Hop
  - Reggae
styles:
  - Dub
  - Dubstep
  - Dancehall
```

## Best Practices

1. **Be specific** — Use 1-3 genres that truly apply, not every genre
2. **Match Discogs exactly** — Use their spelling and capitalization
3. **Styles are optional** — Only add if the term has clear style associations
4. **Check Discogs first** — When uncertain, search Discogs for similar terms
5. **Don't over-tag** — If a term truly applies to all genres, just use "all"

## Discogs URL Patterns

Each genre and style has a canonical Discogs URL:

**Genre URLs:**

- Format: `https://www.discogs.com/genre/{genre-slug}`
- Example: `https://www.discogs.com/genre/rock`
- Example: `https://www.discogs.com/genre/electronic`

**Style URLs:**

- Format: `https://www.discogs.com/style/{style-slug}`
- Example: `https://www.discogs.com/style/krautrock`
- Example: `https://www.discogs.com/style/ambient`

These URLs provide:

- Official definitions and descriptions
- Release counts and statistics
- Related genres/styles
- Popular artists and releases

## Future Integration Plans

**Phase 1** (Current):

- Manual genre/style assignment using Discogs taxonomy
- Reference Discogs URLs in documentation

**Phase 2** (Planned):

- Add `discogs_genre_url` and `discogs_style_urls` fields to schema
- Create automated validators that check against Discogs taxonomy

**Phase 3** (Future):

- Investigate Discogs API for pulling canonical descriptions
- Implement genre/style reference pages that embed or link to Discogs content
- Sync taxonomy updates from Discogs periodically

## Resources

- [Discogs Database Guidelines - Genres & Styles](https://support.discogs.com/hc/en-us/articles/360005055213-Database-Guidelines-9-Genres-Styles)
- [Discogs Genre Browser](https://www.discogs.com/search/?type=all)
- [Discogs Style Browser](https://www.discogs.com/search/?type=all)
- [Discogs API Documentation](https://www.discogs.com/developers)

## Maintaining Consistency

When adding or editing terms:

1. Check similar terms in the lexicon for genre/style precedent
2. Reference actual Discogs releases that use the term
3. Keep the taxonomy aligned with how Discogs categorizes the term
4. Update this document if you discover new relevant styles

---

**Last Updated**: 2025-10-06
