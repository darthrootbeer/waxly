/**
 * GET /v1/term/[slug]
 * Returns single term by slug
 */

const fs = require('fs');
const path = require('path');

module.exports = async (req, res) => {
  const { slug } = req.query;

  // Validate slug
  if (!slug || !/^[a-z0-9-]+$/.test(slug)) {
    return res.status(400).json({ error: 'Invalid slug format' });
  }

  // Read term file
  const termPath = path.join(process.cwd(), 'dataset', 'terms', `${slug}.json`);

  try {
    const data = fs.readFileSync(termPath, 'utf-8');
    const term = JSON.parse(data);

    // Cache for 1 hour
    res.setHeader('Cache-Control', 's-maxage=3600, stale-while-revalidate');
    res.setHeader('Access-Control-Allow-Origin', '*');

    return res.status(200).json(term);
  } catch (err) {
    if (err.code === 'ENOENT') {
      return res.status(404).json({ error: 'Term not found' });
    }
    console.error(err);
    return res.status(500).json({ error: 'Internal server error' });
  }
};
