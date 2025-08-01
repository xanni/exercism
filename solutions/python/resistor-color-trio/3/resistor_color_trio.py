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
    value = ""

    if colors[0] != "black":
        value = str(RESISTOR_COLORS.index(colors[0]))

    if colors[1] != "black":
        value += str(RESISTOR_COLORS.index(colors[1]))
    else:
        exponent += 1

    prefix, exponent = divmod(exponent, 3)
    return f"{value}{"0"*exponent} {METRIC_PREFIXES[prefix]}ohms"
