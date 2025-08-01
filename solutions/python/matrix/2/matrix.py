from __future__ import annotations


class Matrix:
    def __init__(self, matrix_string: str) -> None:
        self.matrix = [[int(e) for e in row.split()] for row in matrix_string.splitlines()]

    def row(self, index: int) -> list[int]:
        return self.matrix[index - 1]

    def column(self, index: int) -> list[int]:
        return list(list(zip(*self.matrix))[index - 1])
