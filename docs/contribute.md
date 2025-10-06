# Contributing to the Vinyl Lexicon

We welcome contributions from vinyl enthusiasts, collectors, audio engineers, DJs, and anyone passionate about preserving vinyl culture knowledge. This guide will help you get started.

## 🚀 Quick Start

1. **Fork the repository** on GitHub
2. **Set up local development** (see Development Setup below)
3. **Create a branch** for your changes
4. **Make your contributions** following our guidelines
5. **Validate your changes** using our automated tools
6. **Submit a pull request** for review
7. **Collaborate** with the community to refine your contribution

## 📝 Types of Contributions

### Adding New Terms
- Research and document new terminology
- Provide clear definitions with examples
- Include cultural context and historical notes
- Add cross-references to related terms

### Improving Existing Terms
- Enhance definitions with additional detail
- Add missing cultural context or examples
- Correct inaccuracies or outdated information
- Improve cross-references and linking

### Regional Variations
- Document geographic differences in terminology
- Add pronunciation guides for regional variations
- Provide cultural context for local usage
- Contribute translations and equivalents

### Multimedia Content
- Add images of equipment, records, or techniques
- Contribute audio examples or pronunciation guides
- Create diagrams or technical illustrations
- Provide video demonstrations or tutorials

## 📋 Term Format Guidelines

### File Structure
Each term should be a separate Markdown file with rich front-matter. Files are organized by first letter in `docs/terms/{letter}/`:

```yaml
---
term: "Term Name"
slug: "term-name"
pos: "noun"
aliases: ["alias1", "alias2"]
tags: ["equipment", "pressing", "quality-control"]
domains: ["pressing_technique", "quality_control"]
regions: ["US", "UK"]
eras: ["1970s", "1980s", "modern"]
first_attested: "1970s"
pronunciation: "/tɜrm neɪm/"
see_also: ["related-term-1", "related-term-2"]
sources:
  - label: "Source Name"
    url: "https://example.com"
summary: "Brief one-sentence definition"
updated: "2025-01-27"
popularity: 6
complexity: "intermediate"
status: "active"
context: "technical"
verification: "verified"
equipment_association: ["turntable", "cartridge"]
genres: ["Rock", "Jazz", "Electronic"]
decade: "1970s"
---

# Term Name

**Definition:** Clear, concise definition of the term.

**Etymology:** Origin and development of the term (when known).

**Example:** Practical example of the term in use.

**Cultural Note:** Historical context, cultural significance, or interesting facts.
```

### Required Fields
- `term`: The canonical name of the term
- `slug`: URL-friendly version (lowercase, hyphens) - must match filename
- `pos`: Part of speech (noun, verb, adjective, etc.)
- `summary`: One-sentence definition
- `updated`: ISO date (YYYY-MM-DD)

### Recommended Fields
- `aliases`: Alternative names or spellings
- `tags`: Categorization tags (equipment, pressing, dj-related, etc.)
- `regions`: Geographic usage areas (US, UK, etc.)
- `eras`: Time periods when term was/is used
- `see_also`: Related terms for cross-referencing
- `popularity`: Current usage level (1-10 scale)
- `complexity`: User skill level (beginner/intermediate/advanced/expert)
- `genres`: Associated music genres (use Discogs taxonomy)

### Genre Taxonomy
Use these standardized genre values from the Discogs taxonomy:
- "Rock", "Pop", "Jazz", "Classical", "Electronic", "Hip Hop"
- "Funk / Soul", "Blues", "Reggae", "Latin", "Folk, World, & Country"
- "Non-Music", "Children's", "Brass & Military", "Stage & Screen"

## 🎯 Quality Standards

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

## 🔍 Review Process

### Pull Request Review
1. **Automated checks**: Linting, validation, and formatting
2. **Community review**: Feedback from other contributors
3. **Expert validation**: Technical accuracy verification
4. **Final approval**: Maintainer sign-off and merge

### Review Criteria
- **Content quality**: Accuracy, completeness, and clarity
- **Format compliance**: Follows established guidelines
- **Cultural sensitivity**: Appropriate and respectful representation
- **Technical accuracy**: Correct information and terminology
- **Cross-references**: Proper linking to related terms

## 🛠️ Development Setup

### Prerequisites
- Git for version control
- Python 3.8+ for validation scripts
- MkDocs for local development server
- Node.js (optional, for Pagefind search)

### Local Development
```bash
# Clone your fork
git clone https://github.com/your-username/vinyl-lexicon.git
cd vinyl-lexicon

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run validation
python scripts/validate_terms.py

# Start development server
mkdocs serve
```

### Available Scripts
- **`validate_terms.py`**: Check front-matter completeness and schema compliance
- **`fix_validation_issues.py`**: Automatically fix common validation errors
- **`autolink_cross_references.py`**: Add cross-references between terms
- **`generate_letter_hubs.py`**: Generate letter-based navigation pages
- **`generate_tag_hubs.py`**: Generate tag-based navigation pages

### Validation Tools
- **Term validation**: Check front-matter completeness and format
- **Schema validation**: Validate against `schema/term.schema.json`
- **Link checking**: Verify cross-references and internal links
- **Content linting**: Ensure consistent formatting and style
- **Autolinking**: Automatically create cross-references between related terms

## 📚 Resources

### Reference Materials
- [Term Schema Documentation](../schema/term.schema.json) - Complete field definitions and validation rules
- [Tag Taxonomy](../docs/data/taxonomy.yml) - Available tags and categories
- [Field Visibility Guide](../schema/VISIBILITY_GUIDE.md) - Which fields appear in different contexts
- [Media Guide](../schema/MEDIA_GUIDE.md) - Guidelines for multimedia content
- [Discogs Taxonomy](../schema/DISCOGS_TAXONOMY.md) - Genre classification system

### Project Structure
- **`docs/terms/{letter}/`**: Individual term files organized by first letter
- **`docs/letters/`**: Auto-generated letter hub pages
- **`docs/tags/`**: Auto-generated tag hub pages
- **`scripts/`**: Validation and automation tools
- **`schema/`**: JSON schemas and documentation

### Community
- **GitHub Issues**: Bug reports, feature requests, and discussions
- **Pull Requests**: Submit contributions and improvements
- **GitHub Discussions**: Community conversations and Q&A

## 🎉 Recognition

### Contributor Credits
- All contributors are credited in the repository
- Significant contributions are highlighted in release notes
- Community members are recognized for their expertise and dedication

### Contributor Levels
- **Contributor**: Any meaningful contribution
- **Reviewer**: Regular contributor with review privileges
- **Maintainer**: Core team member with merge privileges
- **Expert**: Recognized authority in specific domains

## ❓ Frequently Asked Questions

### Q: How do I know if a term already exists?
A: Use the search functionality or browse by letter. Check for aliases and alternative spellings.

### Q: What if I'm not sure about the accuracy of information?
A: Mark the term as `verification: "needs_research"` and include your sources. The community can help verify.

### Q: Can I contribute terms in languages other than English?
A: Yes! Use the `translation` field and `regions` field to document multilingual terms.

### Q: How do I handle controversial or disputed terms?
A: Present multiple perspectives fairly, cite sources, and use the `discussion` field for community input.

### Q: What if I find an error in an existing term?
A: Submit a pull request with corrections, or open an issue to discuss the changes needed.

### Q: How do I run the validation tools?
A: Use `python scripts/validate_terms.py` to check all terms, or `python scripts/fix_validation_issues.py` to automatically fix common issues.

### Q: What if my term doesn't pass validation?
A: Check the error messages and use the fix script, or refer to the schema documentation for field requirements.

## 🔧 Automated Workflows

### Pre-commit Validation
Before submitting your changes, run these commands:

```bash
# Validate all terms
python scripts/validate_terms.py

# Fix common validation issues
python scripts/fix_validation_issues.py

# Regenerate navigation pages
python scripts/generate_letter_hubs.py
python scripts/generate_tag_hubs.py

# Add cross-references
python scripts/autolink_cross_references.py

# Test MkDocs build
mkdocs build
```

### Common Issues and Fixes
- **Schema validation errors**: Use `fix_validation_issues.py` to automatically fix common problems
- **Missing cross-references**: Run `autolink_cross_references.py` to add links between related terms
- **Broken navigation**: Regenerate hub pages with the generate scripts
- **Link validation errors**: Check that all internal links use proper `.md` extensions

---

*Thank you for contributing to the Vinyl Lexicon! Your efforts help preserve and expand the knowledge that makes vinyl culture so rich and diverse.*
