from __future__ import annotations

NUMBERS = ("no", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten")


def _bottles(quantity: int) -> str:
    return "bottle" if quantity == 1 else "bottles"


def _verse(number: int) -> list[str]:
    return [
        f"{NUMBERS[number].capitalize()} green {_bottles(number)} hanging on the wall,",
        f"{NUMBERS[number].capitalize()} green {_bottles(number)} hanging on the wall,",
        "And if one green bottle should accidentally fall,",
        f"There'll be {NUMBERS[number-1]} green {_bottles(number-1)} hanging on the wall.",
    ]


def recite(start: int, take: int = 1) -> list[str]:
    verses = _verse(start)

    for number in range(start - 1, start - take, -1):
        verses.append("")
        verses.extend(_verse(number))

    return verses
