/**
 * GET /v1/random
 * Returns a random term
 */

const fs = require('fs');
const path = require('path');

module.exports = async (req, res) => {
  try {
    // Read index
    const indexPath = path.join(process.cwd(), 'dataset', 'terms', 'index.json');
    const data = fs.readFileSync(indexPath, 'utf-8');
    const index = JSON.parse(data);

    // Pick random term
    const randomIndex = Math.floor(Math.random() * index.terms.length);
    const randomSlug = index.terms[randomIndex].slug;

    // Read full term data
    const termPath = path.join(process.cwd(), 'dataset', 'terms', `${randomSlug}.json`);
    const termData = fs.readFileSync(termPath, 'utf-8');
    const term = JSON.parse(termData);

    // No cache (always random)
    res.setHeader('Cache-Control', 'no-cache');
    res.setHeader('Access-Control-Allow-Origin', '*');

    return res.status(200).json(term);
  } catch (err) {
    console.error(err);
    return res.status(500).json({ error: 'Internal server error' });
  }
};
