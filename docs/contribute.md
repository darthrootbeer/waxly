# Contributing to the Vinyl Lexicon

We welcome contributions from vinyl enthusiasts, collectors, audio engineers, DJs, and anyone passionate about preserving vinyl culture knowledge. This guide will help you get started.

## 🚀 Quick Start

1. **Fork the repository** on GitHub
2. **Create a branch** for your changes
3. **Make your contributions** following our guidelines
4. **Submit a pull request** for review
5. **Collaborate** with the community to refine your contribution

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
Each term should be a separate Markdown file with rich front-matter:

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
genre_association: ["all"]
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
- `slug`: URL-friendly version (lowercase, hyphens)
- `pos`: Part of speech (noun, verb, adjective, etc.)
- `summary`: One-sentence definition
- `updated`: ISO date (YYYY-MM-DD)

### Recommended Fields
- `aliases`: Alternative names or spellings
- `tags`: Categorization tags
- `regions`: Geographic usage areas
- `eras`: Time periods when term was/is used
- `see_also`: Related terms for cross-referencing
- `popularity`: Current usage level (1-10 scale)
- `complexity`: User skill level (beginner/intermediate/advanced/expert)

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

### Local Development
```bash
# Clone your fork
git clone https://github.com/your-username/vinyl-lexicon.git
cd vinyl-lexicon

# Install dependencies
pip install -r requirements.txt

# Run validation
python scripts/validate_terms.py

# Start development server
mkdocs serve
```

### Validation Tools
- **Term validation**: Check front-matter completeness and format
- **Link checking**: Verify cross-references and internal links
- **Content linting**: Ensure consistent formatting and style
- **Schema validation**: Validate against term schema

## 📚 Resources

### Reference Materials
- [Term Schema Documentation](schema/term.schema.json)
- [Tag Taxonomy](docs/data/taxonomy.yml)
- [Style Guide](docs/style-guide.md)
- [API Documentation](api/README.md)

### Community
- **GitHub Discussions**: Community conversations and Q&A
- **Issue Tracker**: Bug reports and feature requests
- **Contributor Chat**: Real-time collaboration and support

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

---

*Thank you for contributing to the Vinyl Lexicon! Your efforts help preserve and expand the knowledge that makes vinyl culture so rich and diverse.*
