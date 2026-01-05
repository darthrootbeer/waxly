#!/usr/bin/env node
/**
 * Fix summaries to be complete sentences
 * Adds period to summaries that don't end with . ! ?
 */

const fs = require('fs');
const path = require('path');

const termsDir = path.join(__dirname, '..', 'dataset', 'terms');
const files = fs.readdirSync(termsDir).filter(f => f.endsWith('.json') && f !== 'index.json');

let fixed = 0;
let alreadyCorrect = 0;

console.log('Fixing summaries...\n');

for (const file of files) {
  const filepath = path.join(termsDir, file);
  const term = JSON.parse(fs.readFileSync(filepath, 'utf-8'));

  if (term.summary) {
    const trimmed = term.summary.trim();
    const endsWithPunctuation = /[.!?]$/.test(trimmed);

    if (!endsWithPunctuation) {
      term.summary = trimmed + '.';
      term.updated = new Date().toISOString().split('T')[0];
      fs.writeFileSync(filepath, JSON.stringify(term, null, 2) + '\n');
      console.log(`✓ Fixed: ${file}`);
      fixed++;
    } else {
      alreadyCorrect++;
    }
  }
}

console.log(`\n${fixed} summaries fixed`);
console.log(`${alreadyCorrect} summaries already correct`);
console.log(`\nDone!`);
