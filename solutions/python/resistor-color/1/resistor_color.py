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


def color_code(color: str) -> int:
    return RESISTOR_COLORS.index(color)


def colors() -> list[str]:
    return RESISTOR_COLORS
