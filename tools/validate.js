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

// Simple validator
function validateTerm(term, slug) {
  const errors = [];

  // Required fields
  for (const field of required) {
    if (!term[field]) {
      errors.push(`Missing required field: ${field}`);
    }
  }

  // Slug format
  if (term.slug && !/^[a-z0-9-]+$/.test(term.slug)) {
    errors.push(`Invalid slug format: ${term.slug}`);
  }

  // Summary length
  if (term.summary && term.summary.length > 200) {
    errors.push(`Summary too long: ${term.summary.length} chars (max 200)`);
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
