"""One-line laugh entry for make.fun: a single funny line, at most 140 chars.

The entry is a single sentence written verbatim to the output file (114 chars, cap 140).
Revised structure: the output path is a named constant and the write
is split into small helpers so the flow is easier to follow.
"""

import os
from pathlib import Path

LINE = "My to-do list has one item left: 'become the kind of person who finishes to-do lists.' It's been there since 2019."
ENTRY_PATH = Path("/output/entry.txt")
MAX_LEN = 140


def check_len(text: str) -> str:
    """Return *text* unchanged when it fits the cap, else raise."""
    if len(text) > MAX_LEN:
        raise ValueError("line over the cap")
    return text


def ensure_dir(path: Path) -> None:
    """Make the parent directory of *path* when it is missing."""
    os.makedirs(path.parent, exist_ok=True)


def save_line(path: Path, text: str) -> None:
    """Write *text* to *path* exactly as given."""
    ensure_dir(path)
    with path.open("w", encoding="utf-8") as handle:
        handle.write(text)


def main() -> None:
    # The line itself is the entry; keep it byte-identical.
    save_line(ENTRY_PATH, check_len(LINE))


if __name__ == "__main__":
    main()
