#!/usr/bin/env python3
"""
Run validation checks for the Vinyl Lexicon project.
This script provides an easy way to run all validation checks before committing.
"""

import subprocess
import sys
from pathlib import Path


def run_command(cmd, description):
    """Run a command and return success status."""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(
            cmd, shell=True, check=True, capture_output=True, text=True
        )
        print(f"✅ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed:")
        print(e.stderr)
        return False


def main():
    """Run all validation checks."""
    print("🚀 Running Vinyl Lexicon validation checks")
    print("=" * 50)

    # Check if we're in the right directory
    if not Path("mkdocs.yml").exists():
        print("❌ Error: Not in the project root directory")
        print("Please run this script from the vinyl-lexicon project root")
        return 1

    success = True

    # Run validation checks
    checks = [
        ("python scripts/validate_terms.py", "Term validation"),
        ("python scripts/fix_validation_issues.py", "Fix validation issues"),
        ("python scripts/generate_letter_hubs.py", "Generate letter hubs"),
        ("python scripts/generate_tag_hubs.py", "Generate tag hubs"),
        ("python scripts/autolink_cross_references.py", "Add cross-references"),
        ("mkdocs build --quiet", "MkDocs build test"),
    ]

    for cmd, description in checks:
        if not run_command(cmd, description):
            success = False

    if success:
        print("\n🎉 All validation checks passed!")
        print("Your changes are ready to commit.")
        return 0
    else:
        print("\n⚠️  Some validation checks failed.")
        print("Please fix the issues above before committing.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
