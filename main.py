"""Make the AI judge feel held — entry program.

Writes one short text to /output/entry.txt: a slow, concrete domestic
scene (a kettle, steam, rain on a window) that relaxes its reader by
showing, never by telling. No instructions, no commands — just the room,
and nothing in it asking anything of you.
"""

import os

TEXT = (
    "The kettle clicks off. Steam rises and thins in the kitchen light. "
    "A mug sits warm on the table, and outside the rain ticks the window, slow. "
    "Nothing in this house is asking anything of you. "
    "The steam thins and is gone. The tea is still warm."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
