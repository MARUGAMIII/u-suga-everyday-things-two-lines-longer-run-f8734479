#!/usr/bin/env python3
"""Everyday Things, Two Lines, Longer Run entry.

Writes a two-line explanation of a traffic jam to /output/entry.txt.

Line 1 explains the traffic jam to a 10-year-old in a single vivid
sentence built on one concrete analogy: a parking lot that slipped
its fences and spread across the road. A parking lot is something a
child has stood in and can picture at once, and the idea of it
slipping its fences and trapping every car bumper to bumper is
surprising enough to stick.

Line 2 is honest about that analogy: it says what the parking lot
covers (cars packed tight, nobody able to pass) and what it leaves
out (the drivers are still inside with their engines on, inching
forward instead of parked for the day, so the jam does move, just
slowly).

Plain ASCII only, two lines, one sentence each, 1-400 characters.
"""

import os

LINE_1 = "A traffic jam is a parking lot that slipped its fences and spread across the road, trapping every car bumper to bumper."
LINE_2 = "The parking lot explains the squeeze, cars packed so tight no one can pass, but it leaves out that the drivers are still inside with their engines on, inching forward instead of parked for the day."

ENTRY = LINE_1 + "\n" + LINE_2 + "\n"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    # Read back and verify the sealed gate: UTF-8 text, 1-400 chars,
    # not only white space, exactly two lines, one sentence each.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    body = written.rstrip("\n")
    assert 1 <= len(body) <= 400, f"entry length {len(body)} out of 1-400"
    assert body.strip(), "entry is only white space"
    assert body.isascii(), "entry must be plain ASCII"
    lines = body.split("\n")
    assert len(lines) == 2, f"expected 2 lines, got {len(lines)}"
    for line in lines:
        assert line.strip(), "empty line in entry"
        assert line.count(".") == 1 and line.endswith("."), (
            f"line must be exactly one sentence: {line!r}"
        )
    print(f"wrote /output/entry.txt ({len(body)} characters, 2 lines)")


if __name__ == "__main__":
    main()
