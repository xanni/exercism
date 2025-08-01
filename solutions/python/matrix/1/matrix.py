from __future__ import annotations

from numpy import array, fromstring


class Matrix:
    def __init__(self, matrix_string: str) -> None:
        self.matrix = array([fromstring(row, sep=" ") for row in matrix_string.splitlines()])

    def row(self, index: int) -> list[int]:
        return self.matrix[index - 1].tolist()

    def column(self, index: int) -> list[int]:
        return self.matrix.transpose()[index - 1].tolist()
