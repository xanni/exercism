from __future__ import annotations

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


def value(colors: list[str]) -> int:
    return RESISTOR_COLORS.index(colors[0]) * 10 + RESISTOR_COLORS.index(colors[1])
