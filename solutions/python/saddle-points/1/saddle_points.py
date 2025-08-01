from __future__ import annotations

ERR_IRREGULAR = "irregular matrix"


def saddle_points(matrix: list[list[int]]) -> list[dict[str, int]]:
    if len({len(row) for row in matrix}) > 1:
        raise ValueError(ERR_IRREGULAR)

    rowmax = [max(row) for row in matrix]
    colmin = [min(col) for col in zip(*matrix)]

    result: list[dict[str, int]] = []
    for i, row in enumerate(matrix):
        for j, element in enumerate(row):
            if element == rowmax[i] and element == colmin[j]:
                result.append({"row": i + 1, "column": j + 1})

    return result
