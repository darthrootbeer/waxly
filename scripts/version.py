#!/usr/bin/env python3
"""
Version management script for Vinyl Lexicon Project.
Handles semantic versioning and changelog updates.
"""

import re
import sys
from pathlib import Path
from datetime import datetime

def get_current_version():
    """Get the current version from VERSION file."""
    version_file = Path(__file__).parent.parent / "VERSION"
    with open(version_file, 'r') as f:
        return f.read().strip()

def bump_version(current_version, bump_type):
    """Bump version according to semantic versioning."""
    major, minor, patch = map(int, current_version.split('.'))
    
    if bump_type == 'major':
        major += 1
        minor = 0
        patch = 0
    elif bump_type == 'minor':
        minor += 1
        patch = 0
    elif bump_type == 'patch':
        patch += 1
    else:
        raise ValueError("bump_type must be 'major', 'minor', or 'patch'")
    
    return f"{major}.{minor}.{patch}"

def update_version_file(new_version):
    """Update the VERSION file with new version."""
    version_file = Path(__file__).parent.parent / "VERSION"
    with open(version_file, 'w') as f:
        f.write(f"{new_version}\n")
    print(f"✅ Updated VERSION file to {new_version}")

def update_changelog(new_version, bump_type):
    """Update CHANGELOG.md with new version entry."""
    changelog_file = Path(__file__).parent.parent / "CHANGELOG.md"
    
    with open(changelog_file, 'r') as f:
        content = f.read()
    
    # Get current date
    date = datetime.now().strftime("%Y-%m-%d")
    
    # Create new version entry
    version_entry = f"""## [{new_version}] - {date}

### {"Major" if bump_type == "major" else "Minor" if bump_type == "minor" else "Patch"} Changes
- [Add your changes here]

"""
    
    # Replace [Unreleased] with new version
    content = content.replace("## [Unreleased]", version_entry + "## [Unreleased]")
    
    with open(changelog_file, 'w') as f:
        f.write(content)
    
    print(f"✅ Updated CHANGELOG.md with version {new_version}")

def update_readme_version(new_version):
    """Update README.md with new version number."""
    readme_file = Path(__file__).parent.parent / "README.md"
    
    with open(readme_file, 'r') as f:
        content = f.read()
    
    # Update version in README
    content = re.sub(r'\*\*Version:\*\* \d+\.\d+\.\d+', f'**Version:** {new_version}', content)
    
    with open(readme_file, 'w') as f:
        f.write(content)
    
    print(f"✅ Updated README.md with version {new_version}")

def main():
    """Main version management function."""
    if len(sys.argv) != 2:
        print("Usage: python3 scripts/version.py <major|minor|patch>")
        print("  major: Breaking changes")
        print("  minor: New features, backward compatible")
        print("  patch: Bug fixes, backward compatible")
        sys.exit(1)
    
    bump_type = sys.argv[1]
    if bump_type not in ['major', 'minor', 'patch']:
        print("Error: bump_type must be 'major', 'minor', or 'patch'")
        sys.exit(1)
    
    # Get current version and bump it
    current_version = get_current_version()
    new_version = bump_version(current_version, bump_type)
    
    print(f"🎵 Vinyl Lexicon Version Management")
    print(f"Current version: {current_version}")
    print(f"New version: {new_version}")
    print()
    
    # Update all files
    update_version_file(new_version)
    update_changelog(new_version, bump_type)
    update_readme_version(new_version)
    
    print()
    print(f"🎉 Version bump complete!")
    print(f"Don't forget to:")
    print(f"  1. Update the changelog with actual changes")
    print(f"  2. Commit the changes: git add . && git commit -m 'Bump version to {new_version}'")
    print(f"  3. Tag the release: git tag -a v{new_version} -m 'Release version {new_version}'")

if __name__ == "__main__":
    main()
