#!/usr/bin/env python3
"""Validate Adaptive Neology lexicon entries."""

from __future__ import annotations

import re
import sys
from pathlib import Path


REQUIRED_HEADINGS = [
    "One-line Definition",
    "Missing Operation",
    "Why Existing Language Is Insufficient",
    "Analogue Check",
    "Cognitive Function",
    "Examples",
    "Non-Examples",
    "Misuse Risks",
    "Retirement Condition",
    "Rubric Score",
    "Recommendation",
]


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: validate_entry.py <entry.md>")
        return 2

    path = Path(sys.argv[1])
    if not path.exists():
        print(f"Missing file: {path}")
        return 2

    text = path.read_text(encoding="utf-8")
    missing = [heading for heading in REQUIRED_HEADINGS if f"## {heading}" not in text]

    score_match = re.search(r"\|\s*Total\s*\|\s*(\d+)\s*\|", text)
    score = int(score_match.group(1)) if score_match else None

    if missing:
        print("Missing required headings:")
        for heading in missing:
            print(f"- {heading}")
        return 1

    if score is None:
        print("Missing total rubric score row: | Total | <number> |")
        return 1

    if not 0 <= score <= 25:
        print("Total score must be between 0 and 25.")
        return 1

    print(f"OK: {path} passes structural validation with score {score}/25.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
