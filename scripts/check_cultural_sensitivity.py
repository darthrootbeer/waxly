#!/usr/bin/env python3
"""
Check terms for potential cultural sensitivity issues.
This script helps identify terms that may need content warnings.
"""

import re
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Set

import yaml

# Keywords that might indicate sensitive content
SENSITIVITY_KEYWORDS = {
    "racial": [
        "race",
        "negro",
        "colored",
        "oriental",
        "caucasian",
        "mongoloid",
        "mulatto",
        "half-breed",
        "mixed-race",
        "ethnic",
        "tribal",
    ],
    "gender": [
        "girl",
        "boy",
        "lady",
        "gentleman",
        "feminine",
        "masculine",
        "effeminate",
        "tomboy",
        "sissy",
        "fag",
        "dyke",
        "tranny",
    ],
    "sexual": [
        "gay",
        "queer",
        "fag",
        "dyke",
        "tranny",
        "pervert",
        "deviant",
        "sexual",
        "erotic",
        "pornographic",
    ],
    "religious": [
        "christian",
        "jewish",
        "muslim",
        "buddhist",
        "hindu",
        "atheist",
        "heathen",
        "infidel",
        "blasphemous",
        "sacrilegious",
    ],
    "ableist": [
        "retard",
        "retarded",
        "idiot",
        "moron",
        "imbecile",
        "cripple",
        "handicapped",
        "disabled",
        "deaf",
        "blind",
        "dumb",
        "lame",
    ],
    "classist": [
        "poor",
        "rich",
        "wealthy",
        "poverty",
        "elite",
        "common",
        "vulgar",
        "low-class",
        "high-class",
        "trash",
        "white-trash",
        "ghetto",
    ],
    "ageist": [
        "old",
        "young",
        "elderly",
        "senile",
        "immature",
        "childish",
        "geriatric",
        "juvenile",
        "infantile",
    ],
    "derogatory": [
        "stupid",
        "dumb",
        "idiot",
        "moron",
        "fool",
        "asshole",
        "bitch",
        "bastard",
        "whore",
        "slut",
        "prostitute",
    ],
}

# Historical terms that may be outdated but not necessarily offensive
HISTORICAL_TERMS = [
    "race record",
    "race music",
    "hillbilly",
    "cowboy",
    "indian",
    "oriental",
    "negro",
    "colored",
    "coloured",
]

# Context clues that might indicate sensitive content
SENSITIVE_CONTEXT_CLUES = [
    "historically",
    "outdated",
    "archaic",
    "obsolete",
    "offensive",
    "inappropriate",
    "controversial",
    "problematic",
    "derogatory",
    "racist",
    "sexist",
    "homophobic",
    "ableist",
    "classist",
]


def load_term_frontmatter(file_path: Path) -> Dict[str, Any]:
    """Load YAML frontmatter from a Markdown file."""
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Extract frontmatter
    match = re.match(r"---(.*?)---(.*)", content, re.DOTALL)
    if match:
        try:
            return yaml.safe_load(match.group(1))
        except yaml.YAMLError:
            return {}
    return {}


def check_term_sensitivity(term_data: Dict[str, Any], term_name: str) -> Dict[str, Any]:
    """Check a term for potential sensitivity issues."""
    issues = []
    sensitivity_types = set()

    # Check term name itself
    term_lower = term_name.lower()

    # Check against sensitivity keywords
    for category, keywords in SENSITIVITY_KEYWORDS.items():
        for keyword in keywords:
            if keyword in term_lower:
                issues.append(f"Term contains '{keyword}' (potentially {category})")
                sensitivity_types.add(category)

    # Check historical terms
    for hist_term in HISTORICAL_TERMS:
        if hist_term in term_lower:
            issues.append(f"Term contains historical reference '{hist_term}'")
            sensitivity_types.add("historical_bias")
            sensitivity_types.add("outdated_terminology")

    # Check summary and definition
    summary = term_data.get("summary", "")
    definition = term_data.get("definition", "")
    combined_text = f"{summary} {definition}".lower()

    for category, keywords in SENSITIVITY_KEYWORDS.items():
        for keyword in keywords:
            if keyword in combined_text:
                issues.append(
                    f"Definition contains '{keyword}' (potentially {category})"
                )
                sensitivity_types.add(category)

    # Check for sensitive context clues
    for clue in SENSITIVE_CONTEXT_CLUES:
        if clue in combined_text:
            issues.append(f"Contains sensitivity context clue: '{clue}'")
            sensitivity_types.add("historical_bias")

    # Check tags for sensitivity indicators
    tags = term_data.get("tags", [])
    if "historical" in tags and any(
        sensitive in term_lower for sensitive in ["race", "negro", "colored"]
    ):
        issues.append("Historical term with potentially sensitive racial content")
        sensitivity_types.add("racial")
        sensitivity_types.add("historical_bias")

    if "slang" in tags and len(issues) > 0:
        issues.append("Slang term with potential sensitivity concerns")

    # Determine sensitivity level
    if len(sensitivity_types) >= 3 or "racial" in sensitivity_types:
        level = "high"
    elif len(sensitivity_types) >= 2:
        level = "moderate"
    elif len(sensitivity_types) >= 1:
        level = "mild"
    else:
        level = None

    return {
        "has_issues": len(issues) > 0,
        "issues": issues,
        "sensitivity_types": list(sensitivity_types),
        "sensitivity_level": level,
        "needs_review": len(issues) > 0,
    }


def generate_sensitivity_report(terms_dir: Path) -> Dict[str, Any]:
    """Generate a comprehensive sensitivity report for all terms."""
    report = {
        "generated_at": datetime.now().isoformat(),
        "total_terms_checked": 0,
        "terms_with_issues": 0,
        "sensitivity_summary": {},
        "terms_needing_review": [],
        "recommendations": [],
    }

    sensitivity_counts = {}
    terms_needing_review = []

    # Find all term files
    term_files = list(terms_dir.rglob("*.md"))
    report["total_terms_checked"] = len(term_files)

    for term_file in term_files:
        term_data = load_term_frontmatter(term_file)
        if not term_data:
            continue

        term_name = term_data.get("term", term_file.stem)
        sensitivity_check = check_term_sensitivity(term_data, term_name)

        if sensitivity_check["has_issues"]:
            report["terms_with_issues"] += 1

            # Count sensitivity types
            for sens_type in sensitivity_check["sensitivity_types"]:
                sensitivity_counts[sens_type] = sensitivity_counts.get(sens_type, 0) + 1

            # Add to review list
            terms_needing_review.append(
                {
                    "term": term_name,
                    "file": str(term_file.relative_to(terms_dir.parent)),
                    "issues": sensitivity_check["issues"],
                    "sensitivity_types": sensitivity_check["sensitivity_types"],
                    "sensitivity_level": sensitivity_check["sensitivity_level"],
                }
            )

    report["sensitivity_summary"] = sensitivity_counts
    report["terms_needing_review"] = terms_needing_review

    # Generate recommendations
    if sensitivity_counts:
        report["recommendations"] = [
            "Review terms with sensitivity issues and add appropriate cultural_sensitivity metadata",
            "Consider adding content warnings for terms with 'high' sensitivity levels",
            "Provide historical context for outdated terminology",
            "Suggest modern alternatives where appropriate",
            "Use appropriate obscuration methods (blur, click_reveal, etc.)",
        ]

    return report


def main():
    """Main function to check cultural sensitivity."""
    terms_dir = Path("docs/terms")

    if not terms_dir.exists():
        print(f"Error: Terms directory {terms_dir} not found")
        return

    print("Checking terms for cultural sensitivity issues...")
    print("=" * 60)

    report = generate_sensitivity_report(terms_dir)

    print(f"Total terms checked: {report['total_terms_checked']}")
    print(f"Terms with potential issues: {report['terms_with_issues']}")

    if report["sensitivity_summary"]:
        print("\nSensitivity Summary:")
        for sens_type, count in sorted(report["sensitivity_summary"].items()):
            print(f"  {sens_type}: {count} terms")

    if report["terms_needing_review"]:
        print(f"\nTerms needing review ({len(report['terms_needing_review'])}):")
        for term_info in report["terms_needing_review"][:10]:  # Show first 10
            print(f"\n  📋 {term_info['term']}")
            print(f"     File: {term_info['file']}")
            print(f"     Level: {term_info['sensitivity_level']}")
            print(f"     Types: {', '.join(term_info['sensitivity_types'])}")
            for issue in term_info["issues"][:2]:  # Show first 2 issues
                print(f"     - {issue}")

        if len(report["terms_needing_review"]) > 10:
            print(f"     ... and {len(report['terms_needing_review']) - 10} more")

    if report["recommendations"]:
        print("\nRecommendations:")
        for rec in report["recommendations"]:
            print(f"  • {rec}")

    # Save detailed report
    report_file = Path("docs/data/sensitivity_report.yml")
    report_file.parent.mkdir(parents=True, exist_ok=True)

    with open(report_file, "w", encoding="utf-8") as f:
        yaml.dump(report, f, default_flow_style=False, sort_keys=False)

    print(f"\nDetailed report saved to: {report_file}")


if __name__ == "__main__":
    main()
