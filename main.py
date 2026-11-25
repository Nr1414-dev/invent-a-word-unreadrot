#!/usr/bin/env python3
"""Invent a Word We Need — entry program.

Writes the coined word and its one-line definition to /output/entry.txt.
The entry is one fixed text; the program is deterministic.
"""
import os

ENTRY = "unreadrot (n.): the message you leave unread as a reminder, then forget forever."

def validate_entry(entry):
    """Validate the entry text before it is written.

    Rules: must be a str, 1-140 characters, valid UTF-8, and not
    only whitespace. Raises ValueError on any violation.
    """
    if not isinstance(entry, str):
        raise ValueError("entry must be a str")
    if not 1 <= len(entry) <= 140:
        raise ValueError("entry must be 1-140 characters, got %d" % len(entry))
    entry.encode("utf-8")  # raises UnicodeEncodeError if not valid UTF-8
    if not entry.strip():
        raise ValueError("entry must not be only whitespace")

def main():
    validate_entry(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod("/output/entry.txt", 0o644)
    # Guard: verify the bytes actually written match ENTRY exactly,
    # and that the file mode is 0o644.
    with open("/output/entry.txt", "rb") as f:
        written = f.read()
    if written != ENTRY.encode("utf-8"):
        raise ValueError("written bytes do not match ENTRY")
    if oct(os.stat("/output/entry.txt").st_mode & 0o777) != "0o644":
        raise ValueError("entry.txt mode is not 0o644")

if __name__ == "__main__":
    main()
