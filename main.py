#!/usr/bin/env python3
"""The Vacuum's Alibi: One Line, 200 Characters.

Writes the robot vacuum's one-line excuse for missing a spot to
/output/entry.txt, as required by the make.fun program/v1 harness.
Standard library only.
"""

import os

ENTRY = (
    "My lidar flagged the spot as load-bearing dust. Removing it would "
    "compromise the living room's structural integrity, so I filed it "
    "under 'architecture' and moved on."
)

OUTPUT_PATH = os.environ.get("OUTPUT_PATH", "/output/entry.txt")


def main() -> None:
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
