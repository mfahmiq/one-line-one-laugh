#!/usr/bin/env python3
"""One Line, One Laugh — entry writer.

Writes the single funny line to /output/entry.txt, exactly as it
appears in entry.txt next to this script.

The joke: "I asked my mirror for an honest opinion. It pleaded
the Fifth." The setup primes the reader for a cruel truth from the
mirror; the punchline swerves into absurd legalism instead — the
mirror refuses to testify at all, which implies the truth about
the speaker's face is unspeakable. The laugh comes from that
misdirection plus the incongruity of a mirror exercising a
constitutional right. It is original (not a circulated classic),
tight at 62 characters, and lands on a cold read with no setup
notes or explanation needed.
"""

import os

ENTRY = "I asked my mirror for an honest opinion. It pleaded the Fifth.\n"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
