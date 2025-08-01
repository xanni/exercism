from __future__ import annotations

A = ord("A")


def _row(size: int, row: int) -> str:
    s = f"{'': <{size-row}}{A+row-1: <{row}c}"

    return s[: size - 1] + s[::-1]


def rows(letter: str) -> list[str]:
    size = ord(letter) - A + 1

    return [_row(size, i) for i in range(1, size)] + [_row(size, size - i) for i in range(size)]
