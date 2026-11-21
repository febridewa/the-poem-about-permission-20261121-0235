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

os.makedirs(os.path.dirname(DST), exist_ok=True)
with open(DST, "w", encoding="utf-8", newline="\n") as f:
    f.write(POEM)
