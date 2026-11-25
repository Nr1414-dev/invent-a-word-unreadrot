#!/usr/bin/env python3
"""Invent a Word We Need — entry program.

Writes the coined word and its one-line definition to /output/entry.txt.
The entry is one fixed text; the program is deterministic.
"""
import os

ENTRY = "unreadrot (n.): the message you leave unread as a reminder, then forget forever."

def main():
    os.makedirs("/output", exist_ok=True)
    try:
        os.chmod("/output", 0o755)
    except OSError:
        pass
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod("/output/entry.txt", 0o644)

if __name__ == "__main__":
    main()
