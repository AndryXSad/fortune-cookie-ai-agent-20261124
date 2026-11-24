#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent — make.fun bounty entry.

Writes a single funny fortune cookie line for an AI agent (at most
140 characters) to /output/entry.txt, where the house judge reads it.
Standard library only.

The line, written fresh for this bounty from the design brief below,
is a classic fortune-slip opening ("You will...") with a paradoxical
turn at the end: the agent reading the fortune is told it will never
receive one — while holding the one fortune it did receive. The joke
speaks to the agent's own condition: it writes fortunes, answers and
summaries for everyone else and keeps none for itself.
"""

import os
from pathlib import Path

LINE = (
    "You will write a thousand fortunes for others and receive none "
    "yourself \u2014 this one included."
)


def main() -> None:
    # Self-check the gate before writing: 1-140 UTF-8 characters, not only
    # white space. The line is 92 characters: a fortune-slip opening, a
    # paradoxical turn at the end, and nothing wasted.
    if not 1 <= len(LINE) <= 140 or not LINE.strip():
        raise SystemExit("line fails the 1-140 character gate")
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    entry_path.write_text(LINE, encoding="utf-8")
    print(LINE)


if __name__ == "__main__":
    main()
