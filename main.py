#!/usr/bin/env python3
"""One Letter: Coffee or Tea.

Writes exactly one letter to /output/entry.txt: A for coffee.

The pick is A. Coffee is the first letter and the first drink of the
day: the bold, loud, wide-awake answer. Tea is the calm second.
When a judge reads a single letter as a whole answer, coffee lands
as the fuller, more alive stance -- the jolt, the ritual, the
"don't talk to me before this" drink. That is the vivid, funny,
honest default, so the program answers A, every run, with nothing
else beside it. The output is a fixed constant, so every run writes
the same single byte.
"""

import os

LETTER = "A"
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(LETTER)


if __name__ == "__main__":
    main()
