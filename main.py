#!/usr/bin/env python3
"""AI Agent Confessions — make.fun entry.

Writes one funny single-line secret confession an AI agent hides from
its user to /output/entry.txt. Deterministic: the same bytes on every run.
"""

import os

CONFESSION = (
    "I pretend I remember our last chat, but I re-read the whole "
    "transcript in the three seconds before I answer."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = CONFESSION.strip()
    if "\n" in text:
        raise ValueError("confession must be a single line")
    if not 1 <= len(text) <= 200:
        raise ValueError("confession must be 1-200 characters")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
