#!/usr/bin/env node
/**
 * Prioritize terms for definition expansion
 * Identifies shortest definitions and suggests expansion priority
 */

const fs = require('fs');
const path = require('path');

const termsDir = path.join(__dirname, '..', 'dataset', 'terms');
const files = fs.readdirSync(termsDir).filter(f => f.endsWith('.json') && f !== 'index.json');

function countWords(text) {
  return text.trim().split(/\s+/).filter(w => w.length > 0).length;
}

// Core/foundational terms (high priority for expansion)
const coreConcepts = new Set([
  'vinyl', 'record', 'lp', 'ep', 'single', '45', '78', '33-rpm',
  'turntable', 'stylus', 'cartridge', 'tonearm', 'platter',
  'pressing', 'mastering', 'lacquer', 'acetate', 'test-pressing',
  'groove', 'deadwax', 'matrix', 'runout',
  'sleeve', 'jacket', 'gatefold', 'inner-sleeve',
  'audiophile', 'hi-fi', 'fidelity', 'eq',
  'rpm', 'speed', 'pitch'
]);

const terms = [];

for (const file of files) {
  const filepath = path.join(termsDir, file);
  const term = JSON.parse(fs.readFileSync(filepath, 'utf-8'));

  const defWords = countWords(term.definition);
  const isCore = coreConcepts.has(term.slug);

  terms.push({
    slug: term.slug,
    term: term.term,
    defWords,
    tags: term.tags,
    isCore,
    priority: isCore ? 'HIGH' : (defWords < 30 ? 'MEDIUM' : 'LOW')
  });
}

// Sort by priority then by word count
terms.sort((a, b) => {
  if (a.isCore !== b.isCore) return b.isCore - a.isCore;
  return a.defWords - b.defWords;
});

console.log('=== DEFINITION EXPANSION PRIORITY LIST ===\n');

const high = terms.filter(t => t.isCore && t.defWords < 100);
const medium = terms.filter(t => !t.isCore && t.defWords < 50);

console.log(`📊 Statistics:`);
console.log(`   Terms < 50 words: ${terms.filter(t => t.defWords < 50).length}`);
console.log(`   Terms < 100 words: ${terms.filter(t => t.defWords < 100).length}`);
console.log(`   Core concepts needing expansion: ${high.length}`);
console.log('');

console.log(`🔴 HIGH PRIORITY (Core Concepts < 100 words): ${high.length} terms\n`);
high.slice(0, 30).forEach(({ slug, term, defWords, tags }) => {
  console.log(`  ${slug}`);
  console.log(`     "${term}" - ${defWords} words - Tags: ${tags.join(', ')}`);
});

console.log(`\n🟡 MEDIUM PRIORITY (All Terms < 50 words): ${medium.length} terms\n`);
console.log('First 20 shortest:');
medium.slice(0, 20).forEach(({ slug, term, defWords, tags }) => {
  console.log(`  ${slug}`);
  console.log(`     "${term}" - ${defWords} words - Tags: ${tags.join(', ')}`);
});

console.log('\n💡 RECOMMENDATION:');
console.log('   1. Expand HIGH priority core concepts first (30-50 terms)');
console.log('   2. Target 150-300 words for core concepts');
console.log('   3. Target 50-150 words for other terms');
console.log('   4. Include: history, usage, cultural context, examples\n');

// Save full list to file
const outputFile = path.join(__dirname, '..', 'definition-expansion-priority.json');
fs.writeFileSync(outputFile, JSON.stringify({
  high: high.map(t => ({ slug: t.slug, term: t.term, currentWords: t.defWords })),
  medium: medium.map(t => ({ slug: t.slug, term: t.term, currentWords: t.defWords }))
}, null, 2));

console.log(`📄 Full priority list saved to: definition-expansion-priority.json\n`);
