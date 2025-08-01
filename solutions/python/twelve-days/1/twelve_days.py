from __future__ import annotations

GIFTS = (
    "a Partridge in a Pear Tree.",
    "two Turtle Doves",
    "three French Hens",
    "four Calling Birds",
    "five Gold Rings",
    "six Geese-a-Laying",
    "seven Swans-a-Swimming",
    "eight Maids-a-Milking",
    "nine Ladies Dancing",
    "ten Lords-a-Leaping",
    "eleven Pipers Piping",
    "twelve Drummers Drumming",
)

NUMBERS = (
    "first",
    "second",
    "third",
    "fourth",
    "fifth",
    "sixth",
    "seventh",
    "eighth",
    "ninth",
    "tenth",
    "eleventh",
    "twelfth",
)


def verse(number: int) -> str:
    return (
        f"On the {NUMBERS[number-1]} day of Christmas my true love gave to me: "
        + (", ".join(GIFTS[number - 1 : 0 : -1]) + ", and " if number > 1 else "")
        + GIFTS[0]
    )


def recite(start_verse: int, end_verse: int) -> list[str]:
    return [verse(n) for n in range(start_verse, end_verse + 1)]
