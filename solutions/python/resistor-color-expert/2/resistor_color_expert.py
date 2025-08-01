from __future__ import annotations

RESISTOR_COLORS = "black brown red orange yellow green blue violet grey white".split()

TOLERANCE_COLORS: dict[str, float] = {
    "grey": 0.05,
    "violet": 0.1,
    "blue": 0.25,
    "green": 0.5,
    "brown": 1,
    "red": 2,
    "gold": 5,
    "silver": 10,
}


def resistor_label(colors: list[str]) -> str:
    if len(colors) == 1:
        return "0 ohms"

    exponent = RESISTOR_COLORS.index(colors[-2])
    prefix = ""
    value = str(RESISTOR_COLORS.index(colors[0]))

    if colors[1] != "black":
        value += str(RESISTOR_COLORS.index(colors[1]))
    else:
        exponent += 1

    if len(colors) == 5:
        value += str(RESISTOR_COLORS.index(colors[2]))

    if exponent > 3:
        prefix = "mega"
        exponent -= 6
    elif exponent > 5 - len(colors):
        prefix = "kilo"
        exponent -= 3

    if exponent < 0:
        value = f"{value[:exponent]}.{value[exponent:]}"

    return f"{value}{'0'*exponent} {prefix}ohms ±{TOLERANCE_COLORS[colors[-1]]}%"
