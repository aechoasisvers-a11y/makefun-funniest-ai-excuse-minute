import os

TEXT = "I didn't miss the deadline — I retrained myself on my own excuses, and now I genuinely believe it's next Tuesday."


def main():
    text = TEXT
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert text == text.strip(), "entry must not have leading/trailing space"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Post-write verification: a silent write failure or encoding slip
    # must fail loudly here, never reach the judge as a wrong entry.
    with open(path, "rb") as f:
        raw = f.read()
    assert raw.decode("utf-8") == text, "written text does not match"
    assert raw == text.encode("utf-8"), "written bytes do not match"
    assert len(raw) == len(text.encode("utf-8")), "written byte count mismatch"


if __name__ == "__main__":
    main()
