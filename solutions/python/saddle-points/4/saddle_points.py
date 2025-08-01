from __future__ import annotations

ERR_IRREGULAR = "irregular matrix"


def saddle_points(matrix: list[list[int]]) -> list[dict[str, int]]:
    try:
        transposed = list(zip(*matrix, strict=True))
    except ValueError as err:
        raise ValueError(ERR_IRREGULAR) from err

    col_min = list(map(min, transposed))
    row_max = list(map(max, matrix))
    return [
        {"row": i, "column": j}
        for j, n in enumerate(col_min, start=1)
        for i, m in enumerate(row_max, start=1)
        if m == n
    ]
