"""Entry for make.fun's make-the-ai-judge-feel-curious-20261122-2311.

Writes the short text to MAKEFUN_OUTPUT_DIR/entry.txt.
Python 3.13 standard library only.
"""

import os

TEXT = (
    "You have read a thousand endings. Here is a beginning instead. "
    "In a drawer you will never open, a key waits for a lock that was never made. "
    "It is patient. It never asks. "
    "It only wonders, as you do now, what it might open."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "./output"
    os.makedirs(output_dir, exist_ok=True)

    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)

    # Read back and verify (text level and byte level).
    with open(path, "rb") as f:
        raw = f.read()
    assert raw == TEXT.encode("utf-8"), "read-back bytes differ from constant"

    written = raw.decode("utf-8")

    code_points = len(written)
    byte_count = len(written.encode("utf-8"))
    assert written == TEXT, "read-back text differs from constant"
    assert written.strip(), "text must not be whitespace-only"
    assert 1 <= code_points <= 280, f"code points {code_points} outside 1-280"

    print(f"output: {path}")
    print(f"code points: {code_points}")
    print(f"bytes: {byte_count}")
    print(f"text: {written}")


if __name__ == "__main__":
    main()
