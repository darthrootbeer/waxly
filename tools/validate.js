#!/usr/bin/env node
/**
 * Validate dataset against schema
 * MVP: Simple validation, clear errors
 */

const fs = require('fs');
const path = require('path');

// Load schema
const schema = JSON.parse(fs.readFileSync('dataset/schema/term.schema.json', 'utf-8'));
const required = schema.required;
const validTags = schema.properties.tags.items.enum;

// Helper: count words in text
function countWords(text) {
  return text.trim().split(/\s+/).filter(w => w.length > 0).length;
}

// Helper: check if text is complete sentence
function isCompleteSentence(text) {
  return /[.!?]$/.test(text.trim());
}

// Simple validator
function validateTerm(term, slug) {
  const errors = [];

  // Required fields
  for (const field of required) {
    if (!term[field]) {
      errors.push(`Missing required field: ${field}`);
    }
  }

  // Slug format and length
  if (term.slug) {
    if (!/^[a-z0-9-]+$/.test(term.slug)) {
      errors.push(`Invalid slug format: ${term.slug}`);
    }
    if (term.slug.length > 50) {
      errors.push(`Slug too long: ${term.slug.length} chars (max 50)`);
    }
  }

  // Summary validation (primary short definition)
  if (term.summary) {
    if (term.summary.length > 200) {
      errors.push(`Summary too long: ${term.summary.length} chars (max 200)`);
    }
    const summaryWords = countWords(term.summary);
    if (summaryWords > 25) {
      errors.push(`Summary exceeds 25 words (${summaryWords} words)`);
    }
    if (!isCompleteSentence(term.summary)) {
      errors.push(`Summary must be a complete sentence (ends with . ! or ?)`);
    }
  }

  // Definition validation (extended definition)
  if (term.definition) {
    const defWords = countWords(term.definition);
    if (defWords < 20) {
      console.warn(`  ⚠ Definition is short (${defWords} words, recommend 50-300)`);
    }
    if (defWords > 500) {
      console.warn(`  ⚠ Definition is long (${defWords} words, recommend 50-300)`);
    }
  }

  // Part of speech validation
  if (term.pos) {
    const validPos = schema.properties.pos.enum;
    if (!validPos.includes(term.pos)) {
      errors.push(`Invalid part of speech: ${term.pos} (valid: ${validPos.join(', ')})`);
    }
  }

  // First use year validation
  if (term.first_use) {
    if (typeof term.first_use !== 'number') {
      errors.push(`first_use must be a number: ${term.first_use}`);
    } else if (term.first_use < 1800 || term.first_use > 2100) {
      errors.push(`first_use out of range: ${term.first_use} (1800-2100)`);
    }
  }

  // Tags
  if (term.tags) {
    if (!Array.isArray(term.tags) || term.tags.length === 0) {
      errors.push('Tags must be non-empty array');
    } else {
      for (const tag of term.tags) {
        if (!validTags.includes(tag)) {
          errors.push(`Invalid tag: ${tag}`);
        }
      }
    }
  }

  // Dates
  const dateRegex = /^\d{4}-\d{2}-\d{2}$/;
  if (term.created && !dateRegex.test(term.created)) {
    errors.push(`Invalid created date: ${term.created}`);
  }
  if (term.updated && !dateRegex.test(term.updated)) {
    errors.push(`Invalid updated date: ${term.updated}`);
  }

  return errors;
}

// Validate all terms
console.log('Validating dataset...\n');

const termsDir = path.join(__dirname, '..', 'dataset', 'terms');
const files = fs.readdirSync(termsDir).filter(f => f.endsWith('.json') && f !== 'index.json');

let totalErrors = 0;
let validTerms = 0;

for (const file of files) {
  const filepath = path.join(termsDir, file);
  const term = JSON.parse(fs.readFileSync(filepath, 'utf-8'));
  const errors = validateTerm(term, file.replace('.json', ''));

  if (errors.length > 0) {
    console.log(`✗ ${file}:`);
    for (const error of errors) {
      console.log(`  - ${error}`);
    }
    totalErrors += errors.length;
  } else {
    validTerms++;
  }
}

console.log(`\n${validTerms} terms validated`);

if (totalErrors > 0) {
  console.log(`✗ ${totalErrors} errors found\n`);
  process.exit(1);
} else {
  console.log('✓ 0 errors\n');
  console.log('Dataset is valid!');
}
