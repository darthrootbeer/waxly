#!/usr/bin/env python3
"""
Update redirects.yml to include redirects for cleaned up slugs.
"""

from pathlib import Path

import yaml

# Mapping of old slugs to new slugs (from cleanup_slugs.py)
SLUG_CLEANUP_MAP = {
    "auxiliary-weight-dj-slang-slug": "auxiliary-weight",
    "groovebox-djproducer-slang": "groovebox",
    "fig-leaf-sleeve-collector-slang": "fig-leaf-sleeve",
    "hard-bop-pressing-collector-slang": "hard-bop-pressing",
    "j-cut-single-collector-slang": "j-cut-single",
    "seam-stress-ring-wear-humorous-slang": "seam-stress-ring-wear",
    "non-fill-pressing-defect": "non-fill",
    "foam-rot-aging-defect": "foam-rot",
    "fish-eye-label-pressing-defect": "fish-eye-label",
    "j-cut-groove-pressing-defect": "j-cut-groove",
    "flanging-tape-vinyl-effect": "flanging",
    "flight-case-road-case": "flight-case",
    "changer-record-changer-stack-loader": "record-changer",
    "drop-spindle-changer-spindle": "drop-spindle",
    "electric-pick-up-early-term-for-cartridge": "electric-pickup",
    "guitar-shaped-picture-disc-novelty-vinyl": "guitar-shaped-picture-disc",
    "zoo-label-novelty-45": "zoo-label",
    "quirky-cut-sleeve-novelty-die-cut-jacket": "quirky-cut-sleeve",
    "spiral-track-locked-groove": "spiral-track",
    "closed-groove-loop-locked-groove": "closed-groove",
    "blank-groove-locked-groove": "blank-groove",
    "perpetual-motion-loop-locked-groove-loop": "perpetual-motion-loop",
    "back-splice-aka-back-tape": "back-splice",
    "blank-label-white-label": "blank-label",
    "demo-copy-promotional-demo": "demo-copy",
    "dead-wax-run-out-area": "dead-wax",
    "dj-pool-record-pool": "dj-pool",
    "reference-lacquer-reference-disc": "reference-lacquer",
}


def get_letter_from_slug(slug):
    """Get the first letter of a slug for directory organization."""
    return slug[0]


def main():
    """Update redirects.yml with old slug redirects."""
    redirects_file = Path("docs/data/redirects.yml")

    if not redirects_file.exists():
        print("redirects.yml not found")
        return

    # Load existing redirects
    with open(redirects_file, "r", encoding="utf-8") as f:
        content = f.read()

    # Parse YAML
    try:
        data = yaml.safe_load(content)
    except yaml.YAMLError as e:
        print(f"Error parsing YAML: {e}")
        return

    if "redirects" not in data:
        data["redirects"] = {}

    # Add new redirects for cleaned up slugs
    new_redirects = []
    for old_slug, new_slug in SLUG_CLEANUP_MAP.items():
        letter = get_letter_from_slug(new_slug)
        new_url = f"terms/{letter}/{new_slug}"

        # Add redirect from old slug to new slug
        data["redirects"][old_slug] = new_url
        new_redirects.append(f'  "{old_slug}": "{new_url}"')

    # Write back to file
    with open(redirects_file, "w", encoding="utf-8") as f:
        f.write(content)

        # Add new redirects at the end
        f.write("\n  # Cleaned up slug redirects\n")
        for redirect in sorted(new_redirects):
            f.write(f"{redirect}\n")

    print(f"Added {len(new_redirects)} redirects for cleaned up slugs")


if __name__ == "__main__":
    main()
