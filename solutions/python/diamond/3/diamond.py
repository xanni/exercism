from __future__ import annotations

A = ord("A")


def rows(letter: str) -> list[str]:
    r: list[str] = []
    size = ord(letter) - A + 1
    for i in range(1, size + 1):
        half = f"{'': <{size-i}}{A+i-1: <{i}c}"
        r.append(half[:-1] + half[::-1])

    return r[:-1] + r[::-1]
