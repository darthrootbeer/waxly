#!/usr/bin/env node
/**
 * Transform extracted content to Waxly v2.0 format
 * MVP: Minimal schema, clean data
 */

const fs = require('fs');
const path = require('path');

// Parse markdown body to extract definition
function parseBody(body) {
  if (!body) return { definition: '' };

  // Extract definition (everything after # heading)
  const lines = body.split('\n');
  let definition = '';
  let inDefinition = false;

  for (const line of lines) {
    if (line.startsWith('#')) {
      // Skip heading
      continue;
    }
    if (line.startsWith('**Definition:**')) {
      definition = line.replace('**Definition:**', '').trim();
      inDefinition = true;
      continue;
    }
    if (inDefinition && line.trim() && !line.startsWith('**')) {
      // Continue building definition until next section
      definition += ' ' + line.trim();
    }
    if (line.startsWith('**Etymology:**') ||
        line.startsWith('**Example:**') ||
        line.startsWith('**Cultural')) {
      inDefinition = false;
    }
  }

  // Fallback: use first paragraph if no Definition: marker
  if (!definition) {
    const paragraphs = body.split('\n\n').filter(p =>
      p.trim() &&
      !p.startsWith('#') &&
      !p.startsWith('**')
    );
    if (paragraphs.length > 0) {
      definition = paragraphs[0].trim();
    }
  }

  return { definition: definition || body.substring(0, 500) };
}

// Transform to v2 format
function transformTerm(legacy) {
  const { definition } = parseBody(legacy.body);

  // Clean and validate tags
  const validTags = [
    "equipment", "pressing", "mastering", "dj-related",
    "collecting", "quality-control", "slang", "technical",
    "historical", "cultural", "genre-specific", "regional"
  ];

  const tags = legacy.tags
    .filter(t => validTags.includes(t))
    .slice(0, 3); // Max 3 tags for cleanliness

  // Ensure at least one tag
  if (tags.length === 0) {
    tags.push('cultural'); // default
  }

  const term = {
    slug: legacy.slug,
    term: legacy.term || legacy.slug.replace(/-/g, ' ').replace(/\b\w/g, l => l.toUpperCase()),
    summary: legacy.summary.substring(0, 200), // enforce max length
    definition: definition,
    tags: tags,
    created: new Date().toISOString().split('T')[0],
    updated: new Date().toISOString().split('T')[0]
  };

  // Optional fields (only if present)
  if (legacy.aliases && legacy.aliases.length > 0) {
    term.aliases = legacy.aliases;
  }
  if (legacy.see_also && legacy.see_also.length > 0) {
    term.see_also = legacy.see_also;
  }
  if (legacy.regions && legacy.regions.length > 0) {
    term.regions = legacy.regions;
  }

  return term;
}

// Main
console.log('Transforming legacy content to Waxly v2.0...\n');

const input = JSON.parse(fs.readFileSync('legacy-content-export.json', 'utf-8'));
const termsDir = path.join(__dirname, 'dataset', 'terms');

let count = 0;
const index = [];

for (const legacy of input.terms) {
  const term = transformTerm(legacy);

  // Write individual JSON file
  const filename = `${term.slug}.json`;
  const filepath = path.join(termsDir, filename);
  fs.writeFileSync(filepath, JSON.stringify(term, null, 2));

  // Add to index (metadata only)
  index.push({
    slug: term.slug,
    term: term.term,
    summary: term.summary,
    tags: term.tags,
    updated: term.updated
  });

  count++;
  if (count % 50 === 0) {
    console.log(`  Transformed ${count} terms...`);
  }
}

// Write index file
const indexPath = path.join(termsDir, 'index.json');
fs.writeFileSync(indexPath, JSON.stringify({
  total: count,
  generated: new Date().toISOString().split('T')[0],
  terms: index
}, null, 2));

console.log(`\n✓ Transformed ${count} terms`);
console.log(`✓ Written to dataset/terms/`);
console.log(`✓ Created index.json\n`);
console.log('Next: Validate dataset');
