#!/usr/bin/env node
/**
 * Audit term slugs for unnecessary verbosity
 * Identifies slugs that should be shortened to most common term
 */

const fs = require('fs');
const path = require('path');

const termsDir = path.join(__dirname, '..', 'dataset', 'terms');
const files = fs.readdirSync(termsDir).filter(f => f.endsWith('.json') && f !== 'index.json');

const issues = [];
const longSlugs = [];
const redundantSlugs = [];
const verboseSlugs = [];

console.log('Auditing slugs for verbosity...\n');

for (const file of files) {
  const filepath = path.join(termsDir, file);
  const term = JSON.parse(fs.readFileSync(filepath, 'utf-8'));
  const slug = term.slug;

  // Check for overly long slugs (>20 chars)
  if (slug.length > 20) {
    longSlugs.push({ slug, length: slug.length, term: term.term });
  }

  // Check for redundant parts (word appears twice)
  const words = slug.split('-');
  const uniqueWords = [...new Set(words)];
  if (words.length > uniqueWords.length) {
    redundantSlugs.push({ slug, term: term.term, issue: 'redundant words' });
  }

  // Check for verbose patterns
  if (slug.includes('-aka-') || slug.includes('-also-') || slug.includes('-or-')) {
    verboseSlugs.push({ slug, term: term.term, issue: 'verbose connectors (aka/also/or)' });
  }

  // Check for parenthetical explanations in slug
  if (slug.match(/\w+-\w+-\w+-\w+-\w+/)) { // 5+ hyphenated parts
    verboseSlugs.push({ slug, term: term.term, issue: '5+ parts - likely over-explained' });
  }
}

// Report findings
console.log('=== AUDIT RESULTS ===\n');

console.log(`📏 Long Slugs (>20 chars): ${longSlugs.length}`);
if (longSlugs.length > 0) {
  console.log('\nTop 20 longest slugs:');
  longSlugs
    .sort((a, b) => b.length - a.length)
    .slice(0, 20)
    .forEach(({ slug, length, term }) => {
      console.log(`  ${length} chars: ${slug}`);
      console.log(`           Term: "${term}"`);
    });
}

console.log(`\n🔁 Redundant Slugs: ${redundantSlugs.length}`);
if (redundantSlugs.length > 0) {
  console.log('\nSlugs with repeated words:');
  redundantSlugs.slice(0, 15).forEach(({ slug, term, issue }) => {
    console.log(`  ${slug}`);
    console.log(`           Term: "${term}" (${issue})`);
  });
}

console.log(`\n📝 Verbose Slugs: ${verboseSlugs.length}`);
if (verboseSlugs.length > 0) {
  console.log('\nOverly verbose slugs:');
  const uniqueVerbose = verboseSlugs.filter((v, i, arr) =>
    arr.findIndex(x => x.slug === v.slug) === i
  );
  uniqueVerbose.slice(0, 20).forEach(({ slug, term, issue }) => {
    console.log(`  ${slug}`);
    console.log(`           Term: "${term}" (${issue})`);
  });
}

console.log(`\n\n=== SUMMARY ===`);
console.log(`Total terms: ${files.length}`);
console.log(`Long slugs (>20 chars): ${longSlugs.length}`);
console.log(`Redundant slugs: ${redundantSlugs.length}`);
console.log(`Verbose slugs: ${verboseSlugs.length}`);
console.log(`\n💡 Recommendation: Review these ${longSlugs.length + redundantSlugs.length + verboseSlugs.length} slugs for potential shortening\n`);
