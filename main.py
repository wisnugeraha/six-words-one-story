#!/usr/bin/env python3
"""Six Words, One Story — make.fun entry.

Writes exactly one six-word story to /output/entry.txt.
The program is the entry: a complete story in six words.
"""
import os


def story() -> str:
    """The six-word story. Every word earns its place."""
    return "The clock stopped. I wound it"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = story()
    # Exactly six words, a complete story that lands a turn.
    words = text.split()
    assert len(words) == 6, f"expected 6 words, got {len(words)}"
    assert 1 <= len(text) <= 60, "text must be 1-60 chars"
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text + "\n")
    # Leave the output readable by every user (grader collects as another user).
    os.chmod(path, 0o644)
    print(f"wrote {path} ({len(words)} words)")


if __name__ == "__main__":
    main()
