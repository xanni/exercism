from __future__ import annotations

VERSE = (
    "house that Jack built.",
    "malt that lay in",
    "rat that ate",
    "cat that killed",
    "dog that worried",
    "cow with the crumpled horn that tossed",
    "maiden all forlorn that milked",
    "man all tattered and torn that kissed",
    "priest all shaven and shorn that married",
    "rooster that crowed in the morn that woke",
    "farmer sowing his corn that kept",
    "horse and the hound and the horn that belonged to",
)


def recite(start_verse: int, end_verse: int) -> list[str]:
    rhyme = []
    verse = ""
    for i in range(start_verse - 1):
        verse = f" the {VERSE[i]}{verse}"

    for i in range(start_verse - 1, end_verse):
        verse = f" the {VERSE[i]}{verse}"
        rhyme += ["This is" + verse]

    return rhyme
