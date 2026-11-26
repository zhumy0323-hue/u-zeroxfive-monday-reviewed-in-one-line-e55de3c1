#!/usr/bin/env python3
"""Monday, Reviewed in One Line.

Writes one funny one-line review of Monday to /output/entry.txt:
a single line, under 200 characters, no title, no explanation.
Standard library only, no network, no randomness, deterministic output.
"""

import os

ENTRY = (
    "Monday: woke up tired, worked tired, went to bed tired, "
    "and somehow still owe Tuesday an apology. "
    "Zero stars, would not relive, back again next week anyway."
)


def main() -> None:
    assert len(ENTRY) < 200, f"entry too long: {len(ENTRY)} chars"
    assert "\n" not in ENTRY, "entry must be a single line"
    assert ENTRY.strip() == ENTRY, "entry must not have leading/trailing space"
    assert ENTRY, "entry must not be empty"

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)

    # Read back and verify the exact bytes on disk.
    with open("/output/entry.txt", "rb") as f:
        written = f.read()
    assert written == ENTRY.encode("utf-8"), "written bytes differ from entry"
    assert not written.endswith(b"\n"), "entry must have no trailing newline"


if __name__ == "__main__":
    main()
