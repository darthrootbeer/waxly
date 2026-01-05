/**
 * GET /v1/search?q=query
 * Simple full-text search
 */

const fs = require('fs');
const path = require('path');

function searchTerms(query, terms) {
  const q = query.toLowerCase();
  const results = [];

  for (const slug of terms) {
    const termPath = path.join(process.cwd(), 'dataset', 'terms', `${slug}.json`);
    try {
      const data = fs.readFileSync(termPath, 'utf-8');
      const term = JSON.parse(data);

      // Search in term, summary, definition, aliases
      const searchText = [
        term.term,
        term.summary,
        term.definition,
        ...(term.aliases || [])
      ].join(' ').toLowerCase();

      if (searchText.includes(q)) {
        results.push({
          slug: term.slug,
          term: term.term,
          summary: term.summary,
          tags: term.tags
        });
      }
    } catch (err) {
      // Skip invalid terms
    }
  }

  return results;
}

module.exports = async (req, res) => {
  const { q } = req.query;

  if (!q || q.length < 2) {
    return res.status(400).json({ error: 'Query must be at least 2 characters' });
  }

  try {
    // Read index to get all term slugs
    const indexPath = path.join(process.cwd(), 'dataset', 'terms', 'index.json');
    const data = fs.readFileSync(indexPath, 'utf-8');
    const index = JSON.parse(data);

    const termSlugs = index.terms.map(t => t.slug);
    const results = searchTerms(q, termSlugs);

    // Cache for 5 minutes
    res.setHeader('Cache-Control', 's-maxage=300');
    res.setHeader('Access-Control-Allow-Origin', '*');

    return res.status(200).json({
      query: q,
      total: results.length,
      results: results.slice(0, 50) // Max 50 results
    });
  } catch (err) {
    console.error(err);
    return res.status(500).json({ error: 'Internal server error' });
  }
};
