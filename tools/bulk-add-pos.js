#!/usr/bin/env node
/**
 * Bulk add 'pos' (part of speech) field to all terms
 * Uses heuristics to determine part of speech
 */

const fs = require('fs');
const path = require('path');

const termsDir = path.join(__dirname, '..', 'dataset', 'terms');
const files = fs.readdirSync(termsDir).filter(f => f.endsWith('.json') && f !== 'index.json');

// Keywords that indicate different parts of speech
const verbIndicators = ['cut', 'press', 'master', 'play', 'spin', 'scratch', 'mix', 'blend', 'sample'];
const phraseIndicators = ['-and-', '-to-', '-of-', '-for-', '-with-'];

let added = 0;
let skipped = 0;

console.log('Adding pos field to terms...\n');

for (const file of files) {
  const filepath = path.join(termsDir, file);
  const term = JSON.parse(fs.readFileSync(filepath, 'utf-8'));

  // Skip if already has pos field
  if (term.pos) {
    skipped++;
    continue;
  }

  // Determine part of speech
  let pos = 'noun'; // default

  // Check for verb indicators
  const slug = term.slug.toLowerCase();
  const termName = term.term.toLowerCase();

  if (verbIndicators.some(v => slug.includes(v) || termName.includes(v))) {
    // Check if it's gerund (noun form of verb) or actual verb
    if (slug.endsWith('-ing') || termName.endsWith('ing')) {
      pos = 'noun'; // gerunds are nouns
    } else {
      pos = 'verb';
    }
  }

  // Check for phrases (multi-word with connectors)
  if (phraseIndicators.some(p => slug.includes(p))) {
    pos = 'phrase';
  }

  // Add pos field
  term.pos = pos;
  term.updated = new Date().toISOString().split('T')[0];

  fs.writeFileSync(filepath, JSON.stringify(term, null, 2) + '\n');
  added++;

  if (added % 50 === 0) {
    console.log(`Progress: ${added} terms updated...`);
  }
}

console.log(`\n✓ ${added} terms updated with pos field`);
console.log(`⊘ ${skipped} terms already had pos field`);
console.log('\nBreakdown:');
console.log('  - Most terms set to "noun" (default)');
console.log('  - Multi-word phrases set to "phrase"');
console.log('  - Action words set to "verb"\n');
console.log('⚠️  Manual review recommended for accuracy\n');
