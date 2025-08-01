from __future__ import annotations


def proverb(*items: list[str], qualifier: str) -> list[str]:
    if not items:
        return []

    return [
        f"For want of a {first} the {second} was lost." for first, second in zip(items, items[1:])
    ] + [f"And all for the want of a {qualifier+' ' if qualifier else ''}{items[0]}."]
