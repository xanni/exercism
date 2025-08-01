from __future__ import annotations

ADJACENT = {complex(x, y) for y in (-1, 0, 1) for x in (-1, 0, 1)} - {0}
CLEAR = " "
MINE = "*"
OUTPUT = CLEAR + "12345678"
VALID = CLEAR + MINE

INVALID_ERR = "The board is invalid with current input."


def annotate(minefield: list[str]) -> list[str]:
    height = len(minefield)
    width = len(minefield[0]) if height else 0

    if any(len(row) != width or row.strip(VALID) for row in minefield):
        raise ValueError(INVALID_ERR)

    mines = {complex(x, y) for y, r in enumerate(minefield) for x, s in enumerate(r) if s == MINE}

    def square(pos: complex) -> str:
        return MINE if pos in mines else OUTPUT[len({pos + n for n in ADJACENT} & mines)]

    return ["".join(square(complex(x, y)) for x in range(width)) for y in range(height)]
