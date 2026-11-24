"""The Robot Apology: a robot's two-line confession.

Writes the two-line entry to /output/entry.txt.
Line 1 owns one specific mistake; line 2 says what the robot
learned and what it will do differently.
"""

import os

ENTRY = (
    "I announced the 6 a.m. alarm at full volume and woke the baby, who had "
    "only just fallen asleep at five.\n"
    "I learned to check who is sleeping before I speak: now I whisper first "
    "and look around the room before I say a word."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
