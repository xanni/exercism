from __future__ import annotations

INVALID_ERR = "The board is invalid with current input."

CLEAR = " "
MINE = "*"


def _adjacent(row: str, i: int) -> int:
    "Returns the number of mines left and right of a given square in a padded row"
    return (row[i] == MINE) + (row[i + 2] == MINE)


def annotate(minefield: list[str]) -> list[str]:
    height = len(minefield)
    width = len(minefield[0]) if height else 0

    if any(len(row) != width for row in minefield):
        raise ValueError(INVALID_ERR)

    minefield = [CLEAR * width, *minefield, CLEAR * width]
    adjacencies = tuple(tuple(_adjacent(f" {row} ", i) for i in range(width)) for row in minefield)
    output: list[str] = []

    for y in range(1, height + 1):
        row = ""

        for x in range(width):
            if minefield[y][x] == MINE:
                row += MINE
                continue

            if minefield[y][x] != CLEAR:
                raise ValueError(INVALID_ERR)

            count = (
                adjacencies[y - 1][x]  # NW and NE
                + (minefield[y - 1][x] == MINE)  # N
                + adjacencies[y][x]  # W and E
                + (minefield[y + 1][x] == MINE)  # S
                + adjacencies[y + 1][x]  # SW and SE
            )

            row += str(count) if count else CLEAR

        output.append(row)

    return output
