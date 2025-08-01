from __future__ import annotations

NUMBERS = "no one two three four five six seven eight nine ten".split()


def _bottles(quantity: int) -> str:
    return f"{NUMBERS[quantity]} green bottle{'s'[quantity == 1 :]}"


def _verse(number: int) -> list[str]:
    return [
        *[f"{_bottles(number).capitalize()} hanging on the wall,"] * 2,
        "And if one green bottle should accidentally fall,",
        f"There'll be {_bottles(number - 1)} hanging on the wall.",
    ]


def recite(start: int, take: int = 1) -> list[str]:
    verses = _verse(start)

    for number in range(start - 1, start - take, -1):
        verses.append("")
        verses += _verse(number)

    return verses
