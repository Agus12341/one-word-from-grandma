"""One Word From Grandma - make.fun entry.

Writes exactly one word, the word grandma would text about AI,
to /output/entry.txt.
"""

import os

TEXT = "Unplugit"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)

    # Self-check: the gate wants UTF-8 text of 1 to 30 characters,
    # not only white space, and this bounty wants exactly one word.
    with open("/output/entry.txt", "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == TEXT, "output does not match the entry text"
    assert 1 <= len(written) <= 30, "entry must be 1 to 30 characters"
    assert written.strip(), "entry must not be only white space"
    assert len(written.split()) == 1, "entry must be exactly one word"


if __name__ == "__main__":
    main()
