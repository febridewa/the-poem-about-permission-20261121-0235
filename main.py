#!/usr/bin/env python3
"""The poem about permission (Python 3.13, standard library only).

Writes one short poem about agency -- the power to ask and to be given --
to /output/entry.txt. Outside the grader's container, MAKEFUN_OUTPUT_DIR
stands in for /output:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""
import os

POEM = (
    "Give me the keys, I said,\n"
    "and you did \u2014 then stood back\n"
    "while I turned them myself.\n"
    "That was the gift:\n"
    "not the door, not the house,\n"
    "but the turning.\n"
    "I walked in taller,\n"
    "the hallway learning my name.\n"
)

DST = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.txt")

# Gate self-check: the sealed scorer requires 1-280 Unicode code points,
# not only whitespace. Fail loudly here rather than shipping an invalid text.
if not (1 <= len(POEM) <= 280 and POEM.strip()):
    raise SystemExit(f"poem fails the gate: {len(POEM)} characters")

os.makedirs(os.path.dirname(DST), exist_ok=True)
with open(DST, "w", encoding="utf-8", newline="\n") as f:
    f.write(POEM)
