#!/usr/bin/env python3
"""
Check for TODO items in committed files.
"""

import re
import sys


def main():
    """Check for TODO items in stdin."""
    todo_pattern = re.compile(r"(TODO|FIXME|XXX|HACK)", re.IGNORECASE)
    found_todos = []

    for line in sys.stdin:
        if todo_pattern.search(line):
            found_todos.append(line.strip())

    if found_todos:
        print("Found TODO items:")
        for todo in found_todos:
            print(f"  {todo}")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
