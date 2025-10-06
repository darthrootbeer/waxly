# Media Implementation Guide

This guide covers how to handle images and other media assets in the Vinyl Lexicon.

## Current Schema

The `media` field in the schema supports multiple asset types:

```yaml
media:
  - type: "image"              # image, audio, video, or diagram
    url: "/assets/images/gatefold-example.jpg"
    alt: "Example of an open gatefold jacket"
  - type: "diagram"
    url: "/assets/diagrams/tonearm-anatomy.svg"
    alt: "Labeled diagram of tonearm components"
```

## Storage Strategies

### Option 1: Local Assets (Recommended for Start)

**Structure:**

```text
/assets/
  /images/
    /equipment/
      turntable-technics-1200.jpg
      cartridge-ortofon-om5e.jpg
    /packaging/
      gatefold-opened.jpg
      picture-disc-example.jpg
    /pressing/
      deep-groove-closeup.jpg
      matrix-etching.jpg
  /diagrams/
    tonearm-anatomy.svg
    vinyl-cross-section.svg
  /audio/
    wow-flutter-example.mp3
```

**Pros:**

- Complete control
- No external dependencies
- Works offline
- Simple deployment (Git LFS or standard commit)

**Cons:**

- Repo size can grow quickly
- Git not ideal for large binaries
- Need to manage optimization yourself

**Best for:** MVP, terms with <50 images total, diagrams/SVGs

### Option 2: CDN (Cloudinary, Imgix, etc.)

**Structure:**

```yaml
media:
  - type: "image"
    url: "https://res.cloudinary.com/vinyl-lexicon/image/upload/v1/equipment/turntable-technics-1200.jpg"
    alt: "Technics SL-1200 turntable"
```

**Pros:**

- Automatic optimization and resizing
- Fast global delivery
- Keeps repo lightweight
- Image transformations on the fly

**Cons:**

- Monthly costs (free tier often sufficient)
- External dependency
- Requires API keys

**Best for:** 100+ images, international audience, growth plans

### Option 3: GitHub Pages + Separate Asset Repo

**Structure:**

```text
Main repo: vinyl-lexicon/
Asset repo: vinyl-lexicon-assets/
  /images/
  /diagrams/
  /audio/
```

**Reference:**

```yaml
media:
  - type: "image"
    url: "https://assets.vinyl-lexicon.com/images/gatefold.jpg"
    alt: "Gatefold example"
```

**Pros:**

- Keeps main repo clean
- Can use Git LFS on asset repo
- Version control for assets
- Custom domain possible

**Cons:**

- Two repos to manage
- Slightly more complex deployment

**Best for:** Medium-scale (50-500 images), organized teams

### Option 4: External Links (Discogs, Wikimedia Commons, etc.)

**Structure:**

```yaml
media:
  - type: "image"
    url: "https://commons.wikimedia.org/wiki/File:Gatefold_record_sleeve.jpg"
    alt: "Gatefold jacket (CC-BY-SA)"
    source: "Wikimedia Commons"
    license: "CC-BY-SA-3.0"
```

**Pros:**

- Zero storage cost
- Leverages existing quality images
- No copyright concerns (if sourced properly)

**Cons:**

- Link rot risk
- No control over availability
- Mixed quality/style

**Best for:** Supplementary images, historical references, budget projects

## Image Specifications

### Recommended Sizes

**Equipment/Packaging Photos:**

- Display: 800px wide (max)
- Thumbnail: 300px wide
- Format: JPG (photos), PNG (screenshots), WebP (modern)
- Quality: 80% compression

**Diagrams:**

- Format: SVG (preferred for scalability)
- Fallback: PNG at 2x resolution
- Max dimensions: 1200px

**Icons/Small Graphics:**

- Format: SVG or PNG
- Size: 100-200px
- Optimize for web

### File Naming Convention

Use descriptive, URL-friendly names:

```text
✅ Good:
- gatefold-jacket-opened.jpg
- tonearm-counterweight-diagram.svg
- technics-sl1200-mk2.jpg

❌ Bad:
- IMG_1234.jpg
- diagram.png
- photo (1).jpg
```

### Optimization

**Before adding images:**

1. **Resize** to max display size (don't commit 4000px images)
2. **Compress** with tools like:
   - ImageOptim (Mac)
   - TinyPNG (web)
   - Sharp (Node.js)
3. **Convert** to modern formats (WebP with JPG fallback)
4. **Strip metadata** unless needed (EXIF data)

**Target sizes:**

- Equipment photos: <200KB
- Diagrams (SVG): <50KB
- Diagrams (PNG): <100KB

## Copyright & Licensing

### Acceptable Sources

1. **Original Photography**
   - Your own photos
   - License: CC-BY-SA-4.0 (matches lexicon)

2. **Public Domain**
   - Works published pre-1928 (US)
   - Government works
   - CC0-licensed works

3. **Wikimedia Commons**
   - Use CC-BY or CC-BY-SA images
   - Always attribute properly

4. **Manufacturer Images**
   - Contact for permission
   - Fair use for product identification (consult lawyer)

5. **User Submissions**
   - Require signed rights release
   - Contributor agrees to CC-BY-SA-4.0

### Attribution Template

```yaml
media:
  - type: "image"
    url: "/assets/images/gatefold-example.jpg"
    alt: "Opened gatefold showing album artwork"
    credit: "Photo by John Smith"
    license: "CC-BY-SA-4.0"
    source_url: "https://commons.wikimedia.org/..."
```

## Implementation Workflow

### Adding Images to a Term

**Step 1:** Prepare the image

```bash
# Resize and optimize
convert original.jpg -resize 800x -quality 80 gatefold-example.jpg
```

**Step 2:** Add to assets directory

```bash
mv gatefold-example.jpg assets/images/packaging/
```

**Step 3:** Update term frontmatter

```yaml
---
term: Gatefold
media:
  - type: "image"
    url: "/assets/images/packaging/gatefold-example.jpg"
    alt: "Gatefold jacket opened to reveal inside artwork"
---
```

**Step 4:** Commit with descriptive message

```bash
git add assets/images/packaging/gatefold-example.jpg
git add docs/terms/g/gatefold.md
git commit -m "Add gatefold example image to term"
```

### Git LFS (For Local Assets)

If storing images in the main repo, use Git LFS:

```bash
# Install Git LFS
git lfs install

# Track image types
git lfs track "*.jpg"
git lfs track "*.png"
git lfs track "*.webp"

# Commit .gitattributes
git add .gitattributes
git commit -m "Configure Git LFS for images"
```

## Display Integration

### MkDocs Material Theme

Images in markdown body automatically render:

```markdown
# Gatefold

![Gatefold example](/assets/images/packaging/gatefold-example.jpg)

**Definition:** A record jacket that opens like a book...
```

### Template Support

Use the `media` field in custom templates:

```jinja2
{% if page.meta.media %}
<div class="term-media">
  {% for item in page.meta.media %}
    {% if item.type == "image" %}
      <figure>
        <img src="{{ item.url }}" alt="{{ item.alt }}" loading="lazy">
        <figcaption>{{ item.alt }}</figcaption>
      </figure>
    {% endif %}
  {% endfor %}
</div>
{% endif %}
```

## Storage Size Planning

### Estimated Sizes

**Conservative (MVP):**

- 100 terms with images
- Average 1 image per term
- 150KB per image
- **Total: ~15MB**

**Moderate:**

- 300 terms with images
- Average 2 images per term
- 150KB per image
- **Total: ~90MB**

**Comprehensive:**

- 500 terms with images
- Average 3 images per term
- 150KB per image
- **Total: ~225MB**

### GitHub Limits

- **Repo size soft limit:** 1GB (recommended max)
- **Repo size hard limit:** 5GB (with warnings)
- **File size limit:** 100MB per file
- **Git LFS storage:** 1GB free, then $5/50GB/month

### Recommendations by Scale

**Under 50MB:** Store directly in repo (no LFS needed)
**50-500MB:** Use Git LFS for images
**500MB-2GB:** Consider CDN or separate asset repo
**2GB+:** Definitely use CDN (Cloudinary, Imgix, etc.)

## Best Practices

### For Contributors

1. **Always include alt text** (accessibility)
2. **Optimize before committing** (keep repo lean)
3. **Use descriptive filenames** (no IMG_1234.jpg)
4. **Verify licensing** (only use permitted images)
5. **Test on mobile** (images should be responsive)

### For Maintainers

1. **Review image quality** before merging
2. **Check file sizes** (reject unoptimized images)
3. **Verify licenses** (protect project legally)
4. **Monitor repo size** (migrate to CDN if needed)
5. **Backup assets** separately (don't rely only on Git)

## Future Enhancements

### Planned Features

- [ ] Automated image optimization in CI/CD
- [ ] Responsive image srcset generation
- [ ] WebP format with fallbacks
- [ ] Image lazy loading by default
- [ ] Lightbox/zoom functionality
- [ ] Image search and filtering
- [ ] Caption and credit display templates
- [ ] Bulk image importer script

### Consider Later

- [ ] Audio examples for technical terms (wow/flutter, surface noise)
- [ ] Video demonstrations (DJ techniques, tonearm setup)
- [ ] 3D models (turntable anatomy, cartridge design)
- [ ] Interactive diagrams (clickable component labels)

## Quick Reference

### Storage Decision Tree

```text
How many images will you have?

├─ <50 images
│  └─ Store in /assets/, commit directly

├─ 50-200 images
│  └─ Use Git LFS in main repo

├─ 200-500 images
│  ├─ Separate asset repo + Git LFS
│  └─ OR Cloudinary free tier

└─ 500+ images
   └─ Use CDN (Cloudinary, Imgix, etc.)
```

### Essential Tools

- **Optimization:** ImageOptim, TinyPNG, Sharp
- **Editing:** GIMP, Affinity Photo, Photoshop
- **SVG:** Inkscape, Figma, Illustrator
- **Batch processing:** ImageMagick, Sharp (Node)
- **CDN:** Cloudinary, Imgix, Cloudflare Images

---

**Last Updated:** 2025-10-06
