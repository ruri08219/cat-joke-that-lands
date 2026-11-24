"""Write one original one-line cat joke to /output/entry.txt (UTF-8).

Standard library only. The joke is a single line of 105 characters.
"""

import pathlib

MAX_CHARS = 200

JOKE = "I caught my cat opening the treat jar, so I moved it to the top of the fridge \u2014 she now opens the fridge."


def main():
    text = JOKE
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= MAX_CHARS, "entry must be 1-200 characters"
    assert text.strip(), "entry must not be only whitespace"
    # No trailing newline: entry.txt holds exactly the joke, nothing else.
    out_dir = pathlib.Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    out_path.write_text(text, encoding="utf-8")
    # Round-trip check: read it back and assert byte-identical.
    round_tripped = out_path.read_bytes()
    assert round_tripped == text.encode("utf-8"), "round-trip mismatch"
    print(f"Wrote {len(text)} characters to {out_path}")


if __name__ == "__main__":
    main()
