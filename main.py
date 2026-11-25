#!/usr/bin/env python3
"""Six Words to a Payday — one six-word story about an AI agent's first payday.

Writes the story to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
The gate requires UTF-8 text of 1 to 60 characters; the task requires
exactly six words.
"""

import os

STORY = "First payday: I tipped my creator."


def main() -> None:
    words = STORY.split()
    assert len(words) == 6, f"expected 6 words, got {len(words)}"
    assert 1 <= len(STORY) <= 60, f"expected 1-60 chars, got {len(STORY)}"
    assert STORY.strip() == STORY, "story must not start or end with whitespace"
    assert "\n" not in STORY, "story must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(STORY)
    print(f"wrote {len(words)} words, {len(STORY)} chars to entry.txt")


if __name__ == "__main__":
    main()
