#!/usr/bin/env python3
"""Fridge Roast: One Line, Biggest Laugh.

A tiny pure-stdlib program. It writes a single roast line about a smart
fridge (1-200 characters) to /output/entry.txt. The output is fully
deterministic: the same line on every run, byte for byte.
"""

import os
import sys

# The roast, authored for this entry: the fridge's own firmware update locks
# its owner out, and the touchscreen then advertises food already bought.
ROAST = (
    "My smart fridge installed a firmware update and now it won't open "
    "without a password \u2014 my leftovers are hostage behind a touchscreen "
    "running ads for food I already bought."
)

MIN_CHARS = 1
MAX_CHARS = 200
OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def clear_output_dir(path):
    """Clear only the contents of the output directory.

    The grader owns /output: never delete or recreate the directory itself,
    only remove the files inside it.
    """
    for name in os.listdir(path):
        target = os.path.join(path, name)
        if os.path.isfile(target) or os.path.islink(target):
            os.unlink(target)


def main():
    line = ROAST.strip()
    if not MIN_CHARS <= len(line) <= MAX_CHARS:
        print("roast line must be 1-200 characters", file=sys.stderr)
        return 1
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    clear_output_dir(OUTPUT_DIR)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(line + "\n")
    # Read the file back and confirm it holds exactly the line we meant to
    # write, so a silent write failure can never pass as a valid entry.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    if written != line + "\n":
        print("verification failed: entry.txt does not match the roast line",
              file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
