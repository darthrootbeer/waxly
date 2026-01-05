#!/usr/bin/env node
/**
 * Execute slug shortening plan with conflict resolution
 * Renames files and updates all cross-references
 */

const fs = require('fs');
const path = require('path');

const termsDir = path.join(__dirname, '..', 'dataset', 'terms');
const planFile = path.join(__dirname, '..', 'slug-shortening-plan.json');
const plan = JSON.parse(fs.readFileSync(planFile, 'utf-8'));

// Manual conflict resolution
const conflictResolutions = {
  'tone-arm-lift-cue-lever': 'cue-lever',
  'tone-arm-tube-damping': 'tonearm-damping',
  'vertical-tracking-linear-arm-tangential-arm': 'linear-tracking-arm'
};

// Build rename map
const renameMap = {};
const renames = [];

// Add non-conflicting renames from plan
for (const item of plan.plan) {
  renameMap[item.oldSlug] = item.newSlug;
  renames.push({
    oldSlug: item.oldSlug,
    newSlug: item.newSlug,
    oldFile: `${item.oldSlug}.json`,
    newFile: `${item.newSlug}.json`
  });
}

// Add conflict resolutions
for (const [oldSlug, newSlug] of Object.entries(conflictResolutions)) {
  renameMap[oldSlug] = newSlug;
  renames.push({
    oldSlug,
    newSlug,
    oldFile: `${oldSlug}.json`,
    newFile: `${newSlug}.json`
  });
}

console.log('=== SLUG SHORTENING EXECUTION ===\n');
console.log(`Total renames: ${renames.length}`);
console.log(`Conflicts resolved: ${Object.keys(conflictResolutions).length}\n`);

// Phase 1: Rename files
console.log('Phase 1: Renaming files...\n');
let renamed = 0;

for (const { oldSlug, newSlug, oldFile, newFile } of renames) {
  const oldPath = path.join(termsDir, oldFile);
  const newPath = path.join(termsDir, newFile);

  if (!fs.existsSync(oldPath)) {
    console.log(`⚠️  File not found: ${oldFile}`);
    continue;
  }

  if (fs.existsSync(newPath) && oldPath !== newPath) {
    console.log(`⚠️  Target exists: ${newFile} (skipping ${oldFile})`);
    continue;
  }

  // Update slug in file content
  const term = JSON.parse(fs.readFileSync(oldPath, 'utf-8'));
  term.slug = newSlug;
  term.updated = new Date().toISOString().split('T')[0];

  // Write to new location
  fs.writeFileSync(newPath, JSON.stringify(term, null, 2) + '\n');

  // Remove old file if different
  if (oldPath !== newPath) {
    fs.unlinkSync(oldPath);
  }

  renamed++;
  if (renamed % 25 === 0) {
    console.log(`  Progress: ${renamed} files renamed...`);
  }
}

console.log(`\n✓ ${renamed} files renamed\n`);

// Phase 2: Update cross-references in all terms
console.log('Phase 2: Updating cross-references...\n');

const allFiles = fs.readdirSync(termsDir).filter(f => f.endsWith('.json') && f !== 'index.json');
let updated = 0;

for (const file of allFiles) {
  const filepath = path.join(termsDir, file);
  const term = JSON.parse(fs.readFileSync(filepath, 'utf-8'));
  let changed = false;

  // Update see_also references
  if (term.see_also && Array.isArray(term.see_also)) {
    const newSeeAlso = term.see_also.map(slug => {
      if (renameMap[slug]) {
        changed = true;
        return renameMap[slug];
      }
      return slug;
    });
    term.see_also = newSeeAlso;
  }

  if (changed) {
    term.updated = new Date().toISOString().split('T')[0];
    fs.writeFileSync(filepath, JSON.stringify(term, null, 2) + '\n');
    updated++;
  }
}

console.log(`✓ ${updated} terms had cross-references updated\n`);

// Phase 3: Summary
console.log('=== SUMMARY ===\n');
console.log(`Files renamed: ${renamed}`);
console.log(`Cross-references updated: ${updated}`);
console.log(`\nSample renames:`);
renames.slice(0, 10).forEach(({ oldSlug, newSlug }) => {
  console.log(`  ${oldSlug} → ${newSlug}`);
});

console.log('\n✓ Slug shortening complete!\n');
console.log('⚠️  Remember to rebuild index and validate:\n');
console.log('  node tools/validate.js');
console.log('  cd site && node generator.js\n');
