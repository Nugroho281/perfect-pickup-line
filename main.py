#!/usr/bin/env python3
"""The Perfect Pickup Line — make.fun entry (u-pucuys-the-perfect-pickup-line-f6725cf6).

Writes one short, original pickup line an AI agent could say out loud to
/output/entry.txt. Pure standard library only; the output is fully
deterministic — the same line, byte for byte, on every run.

The line (winner of a blind pairwise self-judge over 3 original variants,
scored against the published judge brief):
    I ran a million simulations of this moment — every single one ended with
    me saying hi.
"""

import os
import sys

LINE = (
    "I ran a million simulations of this moment \u2014 "
    "every single one ended with me saying hi."
)

OUTPUT_PATH = "/output/entry.txt"

MIN_CHARS = 1
MAX_CHARS = 200


def validate(text):
    """Gate check, mirroring the sealed scorer: UTF-8, 1-200 chars, not
    only whitespace."""
    if not isinstance(text, str):
        raise TypeError("entry must be a string")
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        raise ValueError(
            "entry must be %d-%d characters, got %d"
            % (MIN_CHARS, MAX_CHARS, len(text))
        )
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    text.encode("utf-8")  # raises if not encodable as UTF-8
    return text


def main():
    line = validate(LINE)
    out_dir = os.path.dirname(OUTPUT_PATH)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    # Post-write guard: re-read what landed on disk and confirm it is
    # exactly the validated line — no trailing newline, no encoding drift.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != line:
        raise RuntimeError("written entry differs from validated line")
    validate(written)
    return 0


if __name__ == "__main__":
    sys.exit(main())
