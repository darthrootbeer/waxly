#!/usr/bin/env node
/**
 * Intelligent slug shortening script
 * Removes verbose explanations, redundant words, and keeps shortest common form
 */

const fs = require('fs');
const path = require('path');

const termsDir = path.join(__dirname, '..', 'dataset', 'terms');
const files = fs.readdirSync(termsDir).filter(f => f.endsWith('.json') && f !== 'index.json');

// Load all terms
const terms = {};
for (const file of files) {
  const filepath = path.join(termsDir, file);
  terms[file] = JSON.parse(fs.readFileSync(filepath, 'utf-8'));
}

/**
 * Shorten a slug intelligently
 * Rules:
 * 1. Remove explanatory phrases after dash (e.g., "acetate-lacquer-disc" → "acetate")
 * 2. Remove "aka", "also", "or" connectors
 * 3. Remove redundant words
 * 4. Keep shortest recognizable part
 * 5. Prefer first part (usually the most common term)
 */
function shortenSlug(slug, term) {
  let short = slug;

  // Remove parenthetical explanations (anything after aka/also/or)
  short = short.replace(/-aka-.*$/, '');
  short = short.replace(/-also-.*$/, '');
  short = short.replace(/-or-.*$/, '');

  // Remove descriptive suffixes that are too specific
  short = short.replace(/-\d+-gram-\d+-gram.*$/, ''); // -180-gram-200-gram
  short = short.replace(/-\d+-inch.*$/, ''); // -16-inch-transcription
  short = short.replace(/-transcription.*$/, '');
  short = short.replace(/-pressing$/, '');
  short = short.replace(/-copy$/, '');
  short = short.replace(/-edition$/, '');
  short = short.replace(/-record$/, '');
  short = short.replace(/-disc$/, '');
  short = short.replace(/-sleeve$/, '');
  short = short.replace(/-label$/, '');

  // Remove redundant words (e.g., "damping-tonearm-damping" → "tonearm-damping")
  const parts = short.split('-');
  const seen = new Set();
  const unique = [];
  for (const part of parts) {
    if (!seen.has(part)) {
      seen.add(part);
      unique.push(part);
    }
  }
  short = unique.join('-');

  // If still too long, take first 2-3 meaningful parts
  const shortParts = short.split('-');
  if (shortParts.length > 3 && short.length > 20) {
    short = shortParts.slice(0, 2).join('-');
  }

  return short;
}

// Generate shortening plan
const plan = [];
const newSlugs = new Set();
const conflicts = [];

for (const [filename, term] of Object.entries(terms)) {
  const oldSlug = term.slug;
  const newSlug = shortenSlug(oldSlug, term.term);

  if (newSlug !== oldSlug) {
    // Check for conflicts
    if (newSlugs.has(newSlug)) {
      conflicts.push({ oldSlug, newSlug, term: term.term });
    } else {
      newSlugs.add(newSlug);
      plan.push({
        oldSlug,
        newSlug,
        oldFile: filename,
        newFile: `${newSlug}.json`,
        term: term.term,
        savings: oldSlug.length - newSlug.length
      });
    }
  }
}

// Sort by savings (most to least)
plan.sort((a, b) => b.savings - a.savings);

console.log('=== SLUG SHORTENING PLAN ===\n');
console.log(`Total terms: ${files.length}`);
console.log(`Terms to shorten: ${plan.length}`);
console.log(`Conflicts detected: ${conflicts.length}\n`);

if (conflicts.length > 0) {
  console.log('⚠️  CONFLICTS (need manual resolution):');
  conflicts.slice(0, 10).forEach(({ oldSlug, newSlug, term }) => {
    console.log(`  ${oldSlug} → ${newSlug} (CONFLICT!)`);
    console.log(`     Term: "${term}"`);
  });
  console.log('');
}

console.log('Top 30 proposed shortenings:\n');
plan.slice(0, 30).forEach(({ oldSlug, newSlug, term, savings }) => {
  console.log(`  ${oldSlug}`);
  console.log(`  → ${newSlug} (saves ${savings} chars)`);
  console.log(`     Term: "${term}"`);
  console.log('');
});

console.log(`\n💾 Total character savings: ${plan.reduce((sum, p) => sum + p.savings, 0)} chars`);
console.log(`📊 Average slug length: ${oldSlug => plan.reduce((sum, p) => sum + p.oldSlug.length, 0) / plan.length} → ${newSlug => plan.reduce((sum, p) => sum + p.newSlug.length, 0) / plan.length} chars\n`);

// Save plan to file for review
const planFile = path.join(__dirname, '..', 'slug-shortening-plan.json');
fs.writeFileSync(planFile, JSON.stringify({ plan, conflicts }, null, 2));
console.log(`📄 Full plan saved to: slug-shortening-plan.json`);
console.log(`\n⚠️  REVIEW THIS PLAN BEFORE EXECUTING!\n`);
