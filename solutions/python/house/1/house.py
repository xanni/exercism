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
    verse = VERSE[0]
    for i in range(1, end_verse + 1):
        if i >= start_verse:
            rhyme += ["This is the " + verse]
        if i < end_verse:
            verse = f"{VERSE[i]} the {verse}"

    return rhyme
