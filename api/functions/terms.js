/**
 * GET /v1/terms
 * Returns list of all terms (metadata only)
 */

const fs = require('fs');
const path = require('path');

module.exports = async (req, res) => {
  try {
    // Read index file
    const indexPath = path.join(process.cwd(), 'dataset', 'terms', 'index.json');
    const data = fs.readFileSync(indexPath, 'utf-8');
    const index = JSON.parse(data);

    // Apply filters if provided
    const { tag, limit, offset } = req.query;
    let terms = index.terms;

    if (tag) {
      terms = terms.filter(t => t.tags && t.tags.includes(tag));
    }

    const start = parseInt(offset) || 0;
    const end = limit ? start + parseInt(limit) : terms.length;
    const paged = terms.slice(start, end);

    // Cache for 1 hour
    res.setHeader('Cache-Control', 's-maxage=3600, stale-while-revalidate');
    res.setHeader('Access-Control-Allow-Origin', '*');

    return res.status(200).json({
      total: terms.length,
      offset: start,
      limit: paged.length,
      terms: paged
    });
  } catch (err) {
    console.error(err);
    return res.status(500).json({ error: 'Internal server error' });
  }
};
