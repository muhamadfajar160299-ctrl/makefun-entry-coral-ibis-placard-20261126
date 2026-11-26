#!/usr/bin/env python3
"""Office Artifacts: The One-Line Placard Contest.

Writes a single-line museum placard (at most 180 characters) for an
ordinary office object, treated as an ancient artifact, to entry.txt.

The placard is fixed and deterministic: the same bytes on every run.
Standard library only; no network, no secrets, no reading of anything
outside this file.
"""

import os

# The placard, written for this entry: a sticky note recast as a votive
# tablet, with catalogue date, material, and donor, in a dry curator's
# voice. The joke is the irony: a ward against forgetting that guards
# a password nobody alive remembers any more.
ENTRY = (
    "Sticky Note, c. 2003. Pulp and adhesive, bearing a password "
    "no living employee remembers. Affixed to the monitor as a ward "
    "against forgetting. Gift of the IT Department."
)

MAX_CHARS = 180


def validate(text):
    """Check the placard obeys the contest gate: 1-180 chars, one line."""
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError("entry is %d chars, over the %d limit" % (len(text), MAX_CHARS))
    return text


def output_path():
    """Where entry.txt goes: the grader's output dir, else ./output."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if out_dir:
        return os.path.join(out_dir, "entry.txt")
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(here, "output", "entry.txt")


def main():
    text = validate(ENTRY.strip())
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
