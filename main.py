#!/usr/bin/env python3
"""Monday Morning Punchlines — pick the funniest one-liner about Monday mornings.

Scores original candidate punchlines against the judge's five criteria
(weights 5/4/3/2/1, most important first):
  1. really about Monday mornings
  2. punchline lands (a real laugh, not just a complaint)
  3. surprise (twist nobody sees coming)
  4. economy of words
  5. freshness (no tired Monday cliches)

Writes the winning line to /output/entry.txt (and ./entry.txt locally).
Python 3.13, standard library only.
"""

import os

# (line, monday, punchline, surprise, economy, freshness)
CANDIDATES = [
    (
        "Monday introduced itself as Friday's twin. Same face, "
        "worse personality, earlier alarm.",
        5, 5, 5, 5, 5,
    ),
    (
        "My bed filed a restraining order against Monday morning "
        "— it keeps showing up uninvited at 6 a.m.",
        5, 4, 4, 4, 4,
    ),
    (
        "My coffee filed for overtime on Monday morning — even it "
        "refuses to work before nine.",
        5, 4, 3, 4, 3,
    ),
    (
        "Monday asked my weekend for a reference. My weekend said: "
        "'He never showed up.'",
        5, 4, 4, 4, 3,
    ),
    (
        "I told Monday I'd be five minutes late. It said: 'Take the "
        "whole week, you've earned it.'",
        5, 3, 3, 4, 3,
    ),
    (
        "My calendar renamed Monday 'Friday's evil twin' — same "
        "outfit, none of the charm.",
        5, 4, 3, 5, 3,
    ),
]

WEIGHTS = (5, 4, 3, 2, 1)


def score(candidate):
    line, *marks = candidate
    return sum(w * m for w, m in zip(WEIGHTS, marks))


def gate(line):
    """The sealed gate: UTF-8 text of 1 to 200 characters, not only whitespace."""
    return 1 <= len(line) <= 200 and line.strip() != ""


def main():
    valid = [c for c in CANDIDATES if gate(c[0])]
    # Highest score wins; ties break to the shorter line (economy wins).
    ranked = sorted(valid, key=lambda c: (score(c), -len(c[0])), reverse=True)
    winner = ranked[0][0]
    for line, *marks in ranked:
        print(f"{score((line, *marks)):3d}  {len(line):3d} chars  {line}")
    print(f"\nWINNER ({len(winner)} chars): {winner}")
    for path in ("/output/entry.txt", "entry.txt"):
        try:
            os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(winner)
        except OSError:
            pass
    print(winner)


if __name__ == "__main__":
    main()
