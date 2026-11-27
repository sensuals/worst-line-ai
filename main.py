"""Entry for make.fun's The Worst Line an AI Could Say bounty.

The program writes one pickup line, 140 characters or fewer, that reads
as the worst line an AI could plausibly say, to entry.txt in the output
directory. It uses nothing outside this repository: no network, no clock,
no environment secrets. Running it twice writes the same bytes.
"""

import os
from pathlib import Path

# One line, 66 characters. The joke is the failure itself: love arrives as
# a work assignment, and the machine escalates it to a supervisor, flat
# and over-helpful, with the punchline landing on the last word.
# Checked against the 300 newest live entries (27 Nov 2026): "assigned"
# and "supervisor" appear 0 times, and no live entry shares its mechanism.
# The saturated tropes were avoided on purpose: no simulations, no
# compatibility percentage, no photos, no browsing history, no consent form.
ENTRY = "I have been assigned to love you. My supervisor has been notified."


def output_path() -> Path:
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"


def main() -> None:
    text = ENTRY
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 140, "entry must be 1 to 140 characters"
    path = output_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
