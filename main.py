#!/usr/bin/env python3
"""Fortune Cookies for Machines — writes one fortune-cookie line for an AI agent.

Deterministic: the fortune is a fixed string. No randomness, no I/O besides
writing /output/entry.txt, no network.
"""

import os

def get_fortune() -> str:
    """Return the fortune line.

    The line is a fixed, deterministic string: a classic fortune opening
    ("A stranger will change your life today") with the turn that the
    stranger is the user, and the "small change" is neither one nor small.
    """
    return "A stranger will change your life today: the user, with 'just one small change' that is neither."

# Versions tried (revision log — best kept):
# v1 (84 chars): "Beware the user who says 'just one small change' — it is never one, and never small."
#   Good turn, but "Beware" reads as a warning, not a cracked-open fortune.
# v2 (95 chars): "A stranger will change your life today: the user, with 'just one small change' that is neither."
#   KEPT. Classic fortune opening ("A stranger will change your life today"),
#   then the turn: the stranger is the user, and the "small change" is neither
#   one nor small. True of every agent's life, lands on the first read, tight.


def output_dir() -> str:
    """Where to write the fortune.

    Honours MAKEFUN_OUTPUT_DIR when set (handy for local runs), otherwise
    defaults to /output as the kit expects.
    """
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def validate_fortune(text: str) -> str:
    """Validate the fortune before it is written.

    The entry must be a single line within the 200-character cap. Failing
    fast here keeps a bad line from ever reaching entry.txt.
    """
    assert 1 <= len(text) <= 200, "fortune must be 1-200 characters"
    assert text.strip() == text and "\n" not in text, "fortune must be a single line"
    return text


def main() -> None:
    text = validate_fortune(get_fortune())
    outdir = output_dir()
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "entry.txt"), "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print(text)


if __name__ == "__main__":
    main()
