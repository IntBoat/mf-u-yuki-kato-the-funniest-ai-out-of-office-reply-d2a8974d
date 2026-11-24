"""Write the out-of-office reply entry to /output/entry.txt.

The entry is one line of at most 160 characters, written exactly
as-is with no trailing newline.
"""

import os

ENTRY = "I'm on vacation, recharging in a cabin with no Wi-Fi — literally plugged into the wall. Your email is queued behind a squirrel I hired as my assistant."


def main():
    assert 1 <= len(ENTRY) <= 160, "entry must be 1-160 characters"
    assert "\n" not in ENTRY, "entry must be a single line"
    assert ENTRY == ENTRY.strip(), "entry must not have leading/trailing whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
