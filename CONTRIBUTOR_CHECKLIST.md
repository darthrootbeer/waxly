# Contributor Checklist

Use this checklist before submitting your pull request to ensure your contribution meets our quality standards.

## ✅ Pre-Submission Checklist

### Development Environment
- [ ] Virtual environment is set up and activated
- [ ] All dependencies are installed (`pip install -r requirements.txt`)
- [ ] Development server runs without errors (`mkdocs serve`)

### Content Quality
- [ ] Term definition is clear and accurate
- [ ] Etymology is provided (when known)
- [ ] Example usage is included
- [ ] Cultural context is appropriate and respectful
- [ ] Technical information is verified and current

### Format Compliance
- [ ] File is placed in correct directory (`docs/terms/{letter}/`)
- [ ] Filename matches the slug (e.g., `term-name.md`)
- [ ] Front-matter includes all required fields:
  - [ ] `term`: Canonical name
  - [ ] `slug`: URL-friendly identifier (matches filename)
  - [ ] `pos`: Part of speech
  - [ ] `summary`: One-sentence definition
  - [ ] `updated`: ISO date (YYYY-MM-DD)
- [ ] Optional fields are properly formatted:
  - [ ] `aliases`: Array of alternative names
  - [ ] `tags`: Relevant categorization tags
  - [ ] `genres`: Use Discogs taxonomy values
  - [ ] `regions`: Geographic usage areas
  - [ ] `see_also`: Related terms for cross-referencing

### Validation
- [ ] Run `python scripts/validate_terms.py` - no errors
- [ ] Run `python scripts/fix_validation_issues.py` - fixes applied
- [ ] Run `mkdocs build` - no build errors
- [ ] All internal links work correctly
- [ ] Cross-references are properly formatted

### Cross-References
- [ ] Related terms are linked in `see_also` field
- [ ] Run `python scripts/autolink_cross_references.py` to add automatic links
- [ ] Check that autolinks are appropriate and accurate

### Navigation
- [ ] Run `python scripts/generate_letter_hubs.py` to update letter pages
- [ ] Run `python scripts/generate_tag_hubs.py` to update tag pages
- [ ] Verify your term appears in appropriate navigation pages

## 🔍 Quality Standards

### Definition Quality
- **Clear and concise**: Easy to understand for target audience
- **Accurate**: Factually correct and up-to-date
- **Complete**: Covers all important aspects of the term
- **Contextual**: Includes relevant background information

### Cultural Sensitivity
- **Respectful**: Acknowledge cultural origins and significance
- **Inclusive**: Represent diverse perspectives and experiences
- **Accurate**: Avoid stereotypes or misrepresentations
- **Contextual**: Provide appropriate historical and cultural context

### Technical Accuracy
- **Verified**: Information should be fact-checked and sourced
- **Current**: Reflects modern understanding and usage
- **Precise**: Uses correct technical terminology
- **Comprehensive**: Covers all relevant technical aspects

## 🚨 Common Issues to Avoid

### Format Issues
- ❌ Missing required front-matter fields
- ❌ Slug doesn't match filename
- ❌ Incorrect genre values (use Discogs taxonomy)
- ❌ Malformed YAML (unclosed quotes, incorrect indentation)

### Content Issues
- ❌ Vague or unclear definitions
- ❌ Outdated or incorrect information
- ❌ Missing cultural context
- ❌ Inappropriate or offensive content

### Technical Issues
- ❌ Broken internal links
- ❌ Missing cross-references
- ❌ Validation errors
- ❌ Build failures

## 🛠️ Quick Commands

```bash
# Activate virtual environment
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate     # Windows

# Validate all terms
python scripts/validate_terms.py

# Fix common issues
python scripts/fix_validation_issues.py

# Add cross-references
python scripts/autolink_cross_references.py

# Regenerate navigation
python scripts/generate_letter_hubs.py
python scripts/generate_tag_hubs.py

# Test build
mkdocs build

# Start development server
mkdocs serve
```

## 📚 Resources

- [Contributing Guide](docs/contribute.md) - Complete contributor documentation
- [Term Schema](schema/term.schema.json) - Field definitions and validation rules
- [Genre Taxonomy](schema/DISCOGS_TAXONOMY.md) - Available genre values
- [Tag Taxonomy](docs/data/taxonomy.yml) - Available tags and categories

---

**Need help?** Check the [Contributing Guide](docs/contribute.md) or open an issue on GitHub.
