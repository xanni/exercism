from __future__ import annotations

ERR_COLS = "Number of input columns is not a multiple of three"
ERR_LINES = "Number of input lines is not a multiple of four"

FONT: list[str] = [
    " _ | ||_|",  # 0
    "     |  |",  # 1
    " _  _||_ ",  # 2
    " _  _| _|",  # 3
    "   |_|  |",  # 4
    " _ |_  _|",  # 5
    " _ |_ |_|",  # 6
    " _   |  |",  # 7
    " _ |_||_|",  # 8
    " _ |_| _|",  # 9
]


def _digit(a: str, b: str, c: str) -> str:
    """Given three rows of three characters each,
    returns the single digit found if in the FONT else a question mark"""
    try:
        return str(FONT.index(f"{a}{b}{c}"))
    except ValueError:
        return "?"


def _line(a: str, b: str, c: str) -> str:
    "Given three rows, return the string of digits represented by each group of three columns"
    if len(a) % 3:
        raise ValueError(ERR_COLS)

    return "".join([_digit(a[n : n + 3], b[n : n + 3], c[n : n + 3]) for n in range(0, len(a), 3)])


def convert(input_grid: list[str]) -> str:
    if len(input_grid) % 4:
        raise ValueError(ERR_LINES)

    return ",".join([_line(*input_grid[n : n + 3]) for n in range(0, len(input_grid), 4)])
