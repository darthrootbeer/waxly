#!/usr/bin/env node

/**
 * Automated Definition Expansion Script
 *
 * Expands short term definitions (< 50 words) to 50-300 words with full v2.1 metadata
 * using the Claude API for maximum token efficiency.
 *
 * Usage:
 *   node tools/expand-definitions.js                    # Run full expansion
 *   node tools/expand-definitions.js --limit 10         # Process only 10 terms
 *   node tools/expand-definitions.js --dry-run          # Test without writing
 *   node tools/expand-definitions.js --category equipment  # Only equipment terms
 *   node tools/expand-definitions.js --resume           # Resume from last position
 */

require('dotenv').config();
const Anthropic = require('@anthropic-ai/sdk');
const fs = require('fs');
const path = require('path');

// Configuration
const CONFIG = {
  apiKey: process.env.ANTHROPIC_API_KEY,
  model: process.env.CLAUDE_MODEL || 'claude-sonnet-4-5-20250929',
  maxTokens: parseInt(process.env.MAX_TOKENS) || 1500,
  temperature: parseFloat(process.env.TEMPERATURE) || 0.7,
  batchSize: parseInt(process.env.BATCH_SIZE) || 10,
  rateLimit: parseInt(process.env.RATE_LIMIT_DELAY_MS) || 1000,
  enableProgress: process.env.ENABLE_PROGRESS_SAVE === 'true',
  progressFile: process.env.PROGRESS_FILE || '.expand-progress.json'
};

// Category-specific targets
const CATEGORY_TARGETS = {
  equipment: { min: 100, max: 200, priority: 1 },
  technical: { min: 100, max: 200, priority: 2 },
  historical: { min: 100, max: 200, priority: 2 },
  pressing: { min: 75, max: 150, priority: 3 },
  collecting: { min: 50, max: 150, priority: 4 },
  'dj-related': { min: 75, max: 150, priority: 5 },
  cultural: { min: 50, max: 100, priority: 6 }
};

// Paths
const TERMS_DIR = path.join(__dirname, '..', 'dataset', 'terms');
const PROGRESS_PATH = path.join(__dirname, '..', CONFIG.progressFile);

// Parse CLI arguments
const args = process.argv.slice(2);
const options = {
  limit: args.includes('--limit') ? parseInt(args[args.indexOf('--limit') + 1]) : null,
  dryRun: args.includes('--dry-run'),
  category: args.includes('--category') ? args[args.indexOf('--category') + 1] : null,
  resume: args.includes('--resume')
};

// Initialize API client
const client = new Anthropic({ apiKey: CONFIG.apiKey });

// Utility: Count words
function countWords(text) {
  if (!text) return 0;
  return text.trim().split(/\s+/).filter(w => w.length > 0).length;
}

// Utility: Get category priority
function getCategoryPriority(tags) {
  let highestPriority = 999;
  for (const tag of tags) {
    if (CATEGORY_TARGETS[tag] && CATEGORY_TARGETS[tag].priority < highestPriority) {
      highestPriority = CATEGORY_TARGETS[tag].priority;
    }
  }
  return highestPriority;
}

// Utility: Get target word count for term
function getTargetWordCount(tags) {
  for (const tag of tags) {
    if (CATEGORY_TARGETS[tag]) {
      return CATEGORY_TARGETS[tag];
    }
  }
  return { min: 50, max: 150 }; // default
}

// Load progress
function loadProgress() {
  if (!CONFIG.enableProgress || !fs.existsSync(PROGRESS_PATH)) {
    return { lastProcessed: null, index: 0, completed: [] };
  }
  return JSON.parse(fs.readFileSync(PROGRESS_PATH, 'utf-8'));
}

// Save progress
function saveProgress(slug, index, completed) {
  if (!CONFIG.enableProgress) return;
  fs.writeFileSync(PROGRESS_PATH, JSON.stringify({
    lastProcessed: slug,
    index: index,
    completed: completed,
    timestamp: new Date().toISOString()
  }, null, 2));
}

// Build expansion prompt
function buildExpansionPrompt(term, target) {
  return `You are expanding a vinyl terminology encyclopedia entry. Follow the Waxly style guide exactly.

**Current term:**
{
  "slug": "${term.slug}",
  "term": "${term.term}",
  "summary": "${term.summary || ''}",
  "definition": "${term.definition || ''}",
  "tags": ${JSON.stringify(term.tags)},
  "pos": "${term.pos || 'noun'}"
}

**Requirements:**
1. Expand definition to ${target.min}-${target.max} words (based on importance/category)
2. Keep summary as-is (already complete sentence, max 25 words)
3. Add missing v2.1 metadata fields:
   - pronunciation: IPA notation (e.g., "/ˈvaɪnəl/")
   - aliases: Array of alternative names (semantic synonyms)
   - alt_spellings: Array of spelling variants (orthographic)
   - etymology: Origin and historical development (1-2 sentences)
   - first_use: Year (1800-2100) if historically significant
   - regions: Array of region codes (US, UK, EU, JA, etc.) where term is used

4. Writing style (follow these examples):
   - **Acetate**: Covers technology, history (radio/DJ 1950s-60s), Jamaica dubplate culture, fragility (10-20 plays), collector value
   - **Cartridge**: Technical depth (MM vs MC), sonic characteristics, setup complexity, price range ($50-$10k), upgrade importance
   - **Gatefold**: Format explanation, design history, prog-rock era cultural zenith, famous examples, modern reissue practices

5. Content structure:
   - Start with core function/definition
   - Add historical context (when introduced, evolution)
   - Include technical details (how it works, variations)
   - Cover cultural significance (why it matters)
   - End with modern relevance or collector impact

6. Tone: Encyclopedia-like, authoritative but accessible, informative not academic

**Return ONLY valid JSON** matching this schema (no markdown, no explanations):

{
  "slug": "${term.slug}",
  "term": "${term.term}",
  "pos": "noun|verb|adjective|adverb|phrase",
  "pronunciation": "/IPA notation/",
  "summary": "existing summary unchanged",
  "definition": "expanded 50-300 word definition...",
  "tags": ${JSON.stringify(term.tags)},
  "aliases": ["alt name 1", "alt name 2"],
  "alt_spellings": ["spelling variant"],
  "etymology": "origin story",
  "first_use": 1950,
  "see_also": ${JSON.stringify(term.see_also || [])},
  "regions": ["US", "UK"],
  "created": "${term.created}",
  "updated": "${new Date().toISOString().split('T')[0]}"
}`;
}

// Parse and validate expansion response
function parseExpansion(responseText) {
  try {
    // Clean response (remove markdown code blocks if present)
    let cleaned = responseText.trim();
    if (cleaned.startsWith('```json')) {
      cleaned = cleaned.slice(7);
    }
    if (cleaned.startsWith('```')) {
      cleaned = cleaned.slice(3);
    }
    if (cleaned.endsWith('```')) {
      cleaned = cleaned.slice(0, -3);
    }

    const expanded = JSON.parse(cleaned.trim());

    // Validate word count
    const wordCount = countWords(expanded.definition);
    if (wordCount < 50) {
      throw new Error(`Definition too short: ${wordCount} words (need 50+)`);
    }

    return expanded;
  } catch (error) {
    throw new Error(`Failed to parse expansion: ${error.message}`);
  }
}

// Expand single term using Claude API
async function expandTerm(term) {
  const target = getTargetWordCount(term.tags);
  const prompt = buildExpansionPrompt(term, target);

  console.log(`  Calling Claude API for "${term.term}"...`);

  const response = await client.messages.create({
    model: CONFIG.model,
    max_tokens: CONFIG.maxTokens,
    temperature: CONFIG.temperature,
    messages: [{
      role: 'user',
      content: prompt
    }]
  });

  const expanded = parseExpansion(response.content[0].text);
  const wordCount = countWords(expanded.definition);

  console.log(`  ✓ Expanded to ${wordCount} words`);

  return expanded;
}

// Main execution
async function main() {
  console.log('🚀 Vinyl Lexicon Definition Expansion Tool\n');
  console.log('Configuration:');
  console.log(`  Model: ${CONFIG.model}`);
  console.log(`  Dry run: ${options.dryRun}`);
  console.log(`  Limit: ${options.limit || 'none'}`);
  console.log(`  Category filter: ${options.category || 'all'}`);
  console.log(`  Resume: ${options.resume}\n`);

  // Load all terms
  const files = fs.readdirSync(TERMS_DIR)
    .filter(f => f.endsWith('.json') && f !== 'index.json');

  console.log(`Found ${files.length} term files\n`);

  // Load progress
  const progress = options.resume ? loadProgress() : { lastProcessed: null, index: 0, completed: [] };
  const completed = new Set(progress.completed || []);

  if (options.resume && progress.lastProcessed) {
    console.log(`Resuming from: ${progress.lastProcessed} (index ${progress.index})\n`);
  }

  // Identify terms needing expansion
  const candidates = [];

  for (const file of files) {
    const filepath = path.join(TERMS_DIR, file);
    const term = JSON.parse(fs.readFileSync(filepath, 'utf-8'));

    // Skip if already completed in this run
    if (completed.has(term.slug)) {
      continue;
    }

    // Check if needs expansion
    const wordCount = countWords(term.definition);
    const needsExpansion = wordCount < 50;

    // Apply category filter
    if (options.category && !term.tags.includes(options.category)) {
      continue;
    }

    if (needsExpansion) {
      const priority = getCategoryPriority(term.tags);
      candidates.push({
        slug: term.slug,
        file: file,
        filepath: filepath,
        term: term,
        currentWords: wordCount,
        priority: priority,
        tags: term.tags
      });
    }
  }

  // Sort by priority, then by word count (shortest first)
  candidates.sort((a, b) => {
    if (a.priority !== b.priority) return a.priority - b.priority;
    return a.currentWords - b.currentWords;
  });

  console.log(`Found ${candidates.length} terms needing expansion\n`);

  if (candidates.length === 0) {
    console.log('✅ All terms already expanded!\n');
    return;
  }

  // Apply limit
  const toProcess = options.limit ? candidates.slice(0, options.limit) : candidates;

  console.log(`Will process ${toProcess.length} terms\n`);
  console.log('─'.repeat(60));

  // Process each term
  let processed = 0;
  let errors = 0;

  for (let i = 0; i < toProcess.length; i++) {
    const candidate = toProcess[i];

    console.log(`\n[${i + 1}/${toProcess.length}] ${candidate.term.term} (${candidate.slug})`);
    console.log(`  Current: ${candidate.currentWords} words`);
    console.log(`  Tags: ${candidate.tags.join(', ')}`);

    try {
      const expanded = await expandTerm(candidate.term);

      if (!options.dryRun) {
        // Write expanded term back
        fs.writeFileSync(
          candidate.filepath,
          JSON.stringify(expanded, null, 2) + '\n'
        );
        console.log(`  ✓ Written to ${candidate.file}`);
      } else {
        console.log(`  ✓ Dry run - not written`);
      }

      processed++;
      completed.add(candidate.slug);

      // Save progress
      if (!options.dryRun) {
        saveProgress(candidate.slug, i, Array.from(completed));
      }

      // Rate limiting
      if (i < toProcess.length - 1) {
        await new Promise(resolve => setTimeout(resolve, CONFIG.rateLimit));
      }

    } catch (error) {
      console.error(`  ✗ Error: ${error.message}`);
      errors++;
    }
  }

  // Summary
  console.log('\n' + '─'.repeat(60));
  console.log('\n📊 Summary:');
  console.log(`  Processed: ${processed}/${toProcess.length}`);
  console.log(`  Errors: ${errors}`);
  console.log(`  Remaining: ${candidates.length - processed}`);

  if (!options.dryRun && processed > 0) {
    console.log(`\n✅ Expansion complete!`);
    console.log(`\nNext steps:`);
    console.log(`  1. Run: node tools/validate.js`);
    console.log(`  2. Review changes: git diff dataset/terms/`);
    console.log(`  3. Commit: git add dataset/terms/ && git commit -m "Expand definitions for ${processed} terms"`);
  } else if (options.dryRun) {
    console.log(`\n✅ Dry run complete - no files modified`);
    console.log(`\nTo run for real, remove --dry-run flag`);
  }

  console.log('');
}

// Run
main().catch(error => {
  console.error('Fatal error:', error);
  process.exit(1);
});
