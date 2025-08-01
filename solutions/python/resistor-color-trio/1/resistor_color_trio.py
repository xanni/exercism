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
    value = RESISTOR_COLORS.index(colors[0])

    if colors[1] == "black":
        exponent += 1
    else:
        value = 10 * value + RESISTOR_COLORS.index(colors[1])

    prefix, exponent = divmod(exponent, 3)
    return f"{value*10**exponent} {METRIC_PREFIXES[prefix]}ohms"
