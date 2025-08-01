from __future__ import annotations

METRIC_PREFIXES = ["", "kilo", "mega", "giga"]

RESISTOR_COLORS = [
    "black",
    "brown",
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "violet",
    "grey",
    "white",
]


def label(colors: list[str]) -> str:
    exponent = RESISTOR_COLORS.index(colors[2])
    first_digit = second_digit = ""

    if colors[0] != "black":
        first_digit = str(RESISTOR_COLORS.index(colors[0]))

    if colors[1] != "black":
        second_digit = str(RESISTOR_COLORS.index(colors[1]))
    else:
        exponent += 1

    prefix, exponent = divmod(exponent, 3)
    return f"{first_digit}{second_digit}{"0"*exponent} {METRIC_PREFIXES[prefix]}ohms"
