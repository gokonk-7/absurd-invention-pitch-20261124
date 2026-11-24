#!/usr/bin/env python3
"""One-Sentence Absurd Invention Pitch.

Writes a single sentence pitching a ridiculous invention that fixes a tiny
everyday annoyance to /output/entry.txt, as the competition's program/v1
harness requires.

The pitch: a showerhead that listens for you rehearsing an argument you
already lost and cuts the water, so the shower that never ends finally does.
The laugh comes from the invention itself -- a showerhead that referees your
imaginary arguments -- and the fix is silly yet weirdly plausible: it can
hear you, it knows you lost, and it is the only thing in the bathroom with
the power to end the debate.
"""

import os
import sys

PITCH = (
    "A showerhead that cuts the water the moment you start rehearsing "
    "an argument you already lost, so your longest showers finally end "
    "on time."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 220


def main() -> int:
    text = PITCH.strip()
    if not (1 <= len(text) <= MAX_CHARS):
        print(f"pitch is {len(text)} chars, must be 1-{MAX_CHARS}", file=sys.stderr)
        return 1
    if text.count(".") != 1 or not text.endswith("."):
        print("pitch must be exactly one sentence", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
