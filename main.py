"""The Meeting That Should Have Been One Line.

This is the sentence that replaces the meeting: the decision, stated
plainly, plus the price everyone paid to hear it said out loud. If the
line works, the meeting never needed to happen.

Running this file writes the line to ``$MAKEFUN_OUTPUT_DIR/entry.txt``
(default ``/output``), with no trailing newline.
"""

import os

ENTRY = (
    "Approved -- and it only cost twelve people one hour of their lives to "
    "say a word that fits in a subject line."
)


def get_entry() -> str:
    """Return the meeting-killing sentence."""
    return ENTRY


def write_entry(output_dir: str | None = None) -> str:
    """Write the entry to entry.txt inside output_dir and return its path."""
    directory = output_dir or os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(get_entry())
    return path


def main() -> None:
    """Write the entry and print where it went."""
    print(write_entry())


if __name__ == "__main__":
    main()
