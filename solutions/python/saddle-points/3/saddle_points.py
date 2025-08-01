from __future__ import annotations

ERR_IRREGULAR = "irregular matrix"


def saddle_points(matrix: list[list[int]]) -> list[dict[str, int]]:
    try:
        transposed = list(zip(*matrix, strict=True))
    except ValueError as err:
        raise ValueError(ERR_IRREGULAR) from err

    col_min = list(map(min, transposed))
    return [
        {"row": i, "column": j}
        for i, m in enumerate(map(max, matrix), start=1)
        for j, n in enumerate(col_min, start=1)
        if m == n
    ]
