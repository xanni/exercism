from __future__ import annotations

ERR_IRREGULAR = "irregular matrix"


def saddle_points(matrix: list[list[int]]) -> list[dict[str, int]]:
    if len({len(row) for row in matrix}) > 1:
        raise ValueError(ERR_IRREGULAR)

    row_max = [max(row) for row in matrix]
    col_min = [min(col) for col in zip(*matrix)]

    return [
        {"row": i + 1, "column": j + 1}
        for i, m in enumerate(row_max)
        for j, n in enumerate(col_min)
        if m == n
    ]
