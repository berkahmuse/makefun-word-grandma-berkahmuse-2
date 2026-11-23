#!/usr/bin/env python3
"""One Word From Grandma — entry program.

Writes exactly one word to /output/entry.txt: the single word our
grandma would text about AI.

The word is "Al". Grandma does not know what "AI" is. She has decided
it is a man named Al. Al is very clever, Al does the typing now, and
she would like Al to call her back.

Deterministic: no input, no randomness, no network. The output is
always the two bytes "Al", no trailing newline, so repeated runs are
byte-identical.
"""

import os

WORD = "Al"
OUTPUT_PATH = "/output/entry.txt"

# Mirror of the sealed gate in RULES.txt: /output/entry.txt must be
# UTF-8 text of 1 to 30 characters, not only white space. Refuse to
# write anything that would fail it, so a bad WORD can never ship.
assert 1 <= len(WORD) <= 30 and WORD.strip(), "WORD fails the gate"


def main() -> None:
    parent = os.path.dirname(OUTPUT_PATH)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
