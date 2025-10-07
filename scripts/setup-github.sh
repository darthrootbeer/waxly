#!/bin/bash

# Vinyl Lexicon - GitHub Setup Script
# This script helps set up the repository for GitHub hosting

set -e

echo "🎵 Vinyl Lexicon - GitHub Setup"
echo "================================"

# Check if we're in the right directory
if [ ! -f "README.md" ] || [ ! -d "content" ]; then
    echo "❌ Error: Please run this script from the vinyl-lexicon project root directory"
    exit 1
fi

echo "✅ Project structure verified"

# Check if git is initialized
if [ ! -d ".git" ]; then
    echo "❌ Error: Git repository not initialized. Please run 'git init' first."
    exit 1
fi

echo "✅ Git repository verified"

# Create GitHub repository (requires GitHub CLI)
if command -v gh &> /dev/null; then
    echo "📡 Creating GitHub repository..."

    # Check if repository already exists
    if gh repo view vinyl-lexicon &> /dev/null; then
        echo "⚠️  Repository 'vinyl-lexicon' already exists on GitHub"
    else
        gh repo create vinyl-lexicon --public --description "Comprehensive digital reference for vinyl record culture, terminology, and collecting"
        echo "✅ GitHub repository created"
    fi

    # Add remote origin
    git remote add origin https://github.com/$(gh api user --jq .login)/vinyl-lexicon.git 2>/dev/null || echo "⚠️  Remote origin already exists"

    # Push to GitHub
    echo "📤 Pushing to GitHub..."
    git push -u origin master

    echo "✅ Repository pushed to GitHub"

    # Note: GitHub Pages disabled for now - local development only
    echo "ℹ️  GitHub Pages disabled - using local development only"

else
    echo "⚠️  GitHub CLI not found. Please install it or set up the repository manually:"
    echo "   1. Create a new repository on GitHub called 'vinyl-lexicon'"
    echo "   2. Add it as remote: git remote add origin https://github.com/YOUR_USERNAME/vinyl-lexicon.git"
    echo "   3. Push: git push -u origin master"
    echo "   4. Enable GitHub Pages in repository settings"
fi

echo ""
echo "🎉 Setup complete!"
echo ""
echo "Next steps:"
echo "  • Visit your GitHub repository to verify the upload"
echo "  • Run 'mkdocs serve' for local development"
echo "  • Share the repository with the vinyl community"
echo ""
echo "Repository URL: https://github.com/$(gh api user --jq .login 2>/dev/null || echo 'YOUR_USERNAME')/vinyl-lexicon"
echo "Local development: mkdocs serve --dev-addr=127.0.0.1:8000"
