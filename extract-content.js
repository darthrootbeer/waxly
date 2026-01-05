#!/usr/bin/env node
/**
 * Extract term content from legacy Markdown files
 * MVP: Simple, fast, no dependencies except gray-matter
 */

const fs = require('fs');
const path = require('path');

// Simple YAML front-matter parser (no dependencies)
function parseFrontMatter(content) {
  if (!content.startsWith('---')) return null;

  const parts = content.split('---');
  if (parts.length < 3) return null;

  const frontMatter = parts[1].trim();
  const body = parts.slice(2).join('---').trim();

  // Simple YAML parser (handles our basic structure)
  const data = {};
  const lines = frontMatter.split('\n');
  let currentKey = null;
  let currentArray = null;

  for (let line of lines) {
    line = line.trim();
    if (!line || line.startsWith('#')) continue;

    // Array items
    if (line.startsWith('- ')) {
      if (currentArray) {
        currentArray.push(line.substring(2).trim());
      }
      continue;
    }

    // Key-value pairs
    const colonIndex = line.indexOf(':');
    if (colonIndex > 0) {
      const key = line.substring(0, colonIndex).trim();
      let value = line.substring(colonIndex + 1).trim();

      // Remove quotes
      if ((value.startsWith("'") && value.endsWith("'")) ||
          (value.startsWith('"') && value.endsWith('"'))) {
        value = value.substring(1, value.length - 1);
      }

      // Empty value means array follows
      if (!value) {
        currentKey = key;
        currentArray = [];
        data[key] = currentArray;
      } else {
        data[key] = value;
        currentKey = null;
        currentArray = null;
      }
    }
  }

  return { data, body };
}

// Extract content from all term files
function extractContent() {
  const termsDir = path.join(__dirname, 'docs', 'terms');
  const terms = [];

  console.log('Extracting term content from docs/terms/...\n');

  // Read all letter directories
  const letters = fs.readdirSync(termsDir).filter(f => {
    const stat = fs.statSync(path.join(termsDir, f));
    return stat.isDirectory();
  });

  let count = 0;

  for (const letter of letters.sort()) {
    const letterDir = path.join(termsDir, letter);
    const files = fs.readdirSync(letterDir).filter(f => f.endsWith('.md'));

    for (const file of files) {
      const filePath = path.join(letterDir, file);
      const content = fs.readFileSync(filePath, 'utf-8');
      const parsed = parseFrontMatter(content);

      if (!parsed) {
        console.warn(`⚠ Skipped ${file} (no front matter)`);
        continue;
      }

      const { data, body } = parsed;

      // Extract only what we need for v2
      const term = {
        slug: data.slug || file.replace('.md', ''),
        term: data.term || '',
        summary: data.summary || '',
        tags: Array.isArray(data.tags) ? data.tags : [],
        aliases: Array.isArray(data.aliases) ? data.aliases : [],
        see_also: Array.isArray(data.see_also) ? data.see_also : [],
        regions: Array.isArray(data.regions) ? data.regions : [],
        body: body
      };

      terms.push(term);
      count++;

      if (count % 50 === 0) {
        console.log(`  Extracted ${count} terms...`);
      }
    }
  }

  console.log(`\n✓ Extracted ${count} terms\n`);

  return {
    extracted_date: new Date().toISOString().split('T')[0],
    total_terms: count,
    terms: terms
  };
}

// Main
const output = extractContent();
const outputPath = path.join(__dirname, 'legacy-content-export.json');

fs.writeFileSync(outputPath, JSON.stringify(output, null, 2));

console.log(`✓ Saved to: ${outputPath}`);
console.log(`✓ File size: ${(fs.statSync(outputPath).size / 1024 / 1024).toFixed(2)} MB`);
console.log('\nNext: Review extracted data and build canonical dataset');
