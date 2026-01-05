#!/usr/bin/env node
/**
 * Waxly v2.0 Static Site Generator
 * MVP: Minimal, fast, no bloat
 */

const fs = require('fs');
const path = require('path');
const Handlebars = require('handlebars');

// Load templates
const baseTemplate = Handlebars.compile(
  fs.readFileSync(path.join(__dirname, 'templates', 'base.html'), 'utf-8')
);
const termTemplate = Handlebars.compile(
  fs.readFileSync(path.join(__dirname, 'templates', 'term.html'), 'utf-8')
);
const indexTemplate = Handlebars.compile(
  fs.readFileSync(path.join(__dirname, 'templates', 'index.html'), 'utf-8')
);

// Helper: render page with base template
function renderPage(content, data = {}) {
  return baseTemplate({ ...data, content });
}

// Generate term pages
function generateTermPages() {
  console.log('Generating term pages...');

  const termsDir = path.join(__dirname, '..', 'dataset', 'terms');
  const outputDir = path.join(__dirname, 'build', 'terms');
  fs.mkdirSync(outputDir, { recursive: true });

  const files = fs.readdirSync(termsDir).filter(f => f.endsWith('.json') && f !== 'index.json');

  for (const file of files) {
    const term = JSON.parse(fs.readFileSync(path.join(termsDir, file), 'utf-8'));
    const content = termTemplate(term);
    const html = renderPage(content, {
      pageTitle: term.term,
      description: term.summary
    });

    fs.writeFileSync(path.join(outputDir, `${term.slug}.html`), html);
  }

  console.log(`  ✓ Generated ${files.length} term pages`);
}

// Generate index page
function generateIndex() {
  console.log('Generating index page...');

  const indexData = JSON.parse(
    fs.readFileSync(path.join(__dirname, '..', 'dataset', 'terms', 'index.json'), 'utf-8')
  );

  const content = indexTemplate({ total: indexData.total });
  const html = renderPage(content, {
    description: 'Open vinyl terminology dataset - machine-readable, AI-friendly'
  });

  fs.writeFileSync(path.join(__dirname, 'build', 'index.html'), html);
  console.log('  ✓ Generated index page');
}

// Generate browse page (A-Z)
function generateBrowsePage() {
  console.log('Generating browse page...');

  const indexData = JSON.parse(
    fs.readFileSync(path.join(__dirname, '..', 'dataset', 'terms', 'index.json'), 'utf-8')
  );

  // Group by first letter
  const grouped = {};
  for (const term of indexData.terms) {
    const letter = term.slug[0].toUpperCase();
    if (!grouped[letter]) grouped[letter] = [];
    grouped[letter].push(term);
  }

  let content = '<h1>Browse All Terms</h1>\n';

  for (const letter of Object.keys(grouped).sort()) {
    content += `<h2 id="${letter.toLowerCase()}">${letter}</h2>\n`;
    content += '<ul class="term-list">\n';
    for (const term of grouped[letter].sort((a, b) => a.slug.localeCompare(b.slug))) {
      content += `<li>
        <h3><a href="/terms/${term.slug}.html">${term.term}</a></h3>
        <p class="summary">${term.summary}</p>
      </li>\n`;
    }
    content += '</ul>\n';
  }

  const html = renderPage(content, { pageTitle: 'Browse A-Z' });
  fs.writeFileSync(path.join(__dirname, 'build', 'browse.html'), html);
  console.log('  ✓ Generated browse page');
}

// Generate tags page
function generateTagsPage() {
  console.log('Generating tags page...');

  const indexData = JSON.parse(
    fs.readFileSync(path.join(__dirname, '..', 'dataset', 'terms', 'index.json'), 'utf-8')
  );

  // Count terms per tag
  const tagCounts = {};
  const tagTerms = {};

  for (const term of indexData.terms) {
    for (const tag of term.tags || []) {
      tagCounts[tag] = (tagCounts[tag] || 0) + 1;
      if (!tagTerms[tag]) tagTerms[tag] = [];
      tagTerms[tag].push(term);
    }
  }

  let content = '<h1>Browse by Tag</h1>\n';

  for (const tag of Object.keys(tagCounts).sort()) {
    content += `<h2 id="${tag}">${tag} <span style="color: #666;">(${tagCounts[tag]})</span></h2>\n`;
    content += '<ul class="term-list">\n';
    for (const term of tagTerms[tag].sort((a, b) => a.slug.localeCompare(b.slug))) {
      content += `<li>
        <h3><a href="/terms/${term.slug}.html">${term.term}</a></h3>
        <p class="summary">${term.summary}</p>
      </li>\n`;
    }
    content += '</ul>\n';
  }

  const html = renderPage(content, { pageTitle: 'Tags' });
  fs.writeFileSync(path.join(__dirname, 'build', 'tags.html'), html);
  console.log('  ✓ Generated tags page');
}

// Copy static assets
function copyAssets() {
  console.log('Copying assets...');

  const stylesDir = path.join(__dirname, 'build', 'styles');
  fs.mkdirSync(stylesDir, { recursive: true });

  fs.copyFileSync(
    path.join(__dirname, 'styles', 'main.css'),
    path.join(stylesDir, 'main.css')
  );

  console.log('  ✓ Copied CSS');
}

// Main
console.log('\nWaxly v2.0 Site Generator\n');

generateTermPages();
generateIndex();
generateBrowsePage();
generateTagsPage();
copyAssets();

console.log('\n✓ Site generated successfully');
console.log('  Output: site/build/');
console.log('\nTo preview: cd site && npm run serve\n');
