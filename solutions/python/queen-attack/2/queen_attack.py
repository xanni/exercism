from __future__ import annotations

BOARD_SIZE = 8

ERR_COL_MAX = "column not on board"
ERR_COL_MIN = "column not positive"
ERR_DUPLICATE = "Invalid queen position: both queens in the same square"
ERR_ROW_MAX = "row not on board"
ERR_ROW_MIN = "row not positive"


class Queen:
    def __init__(self, row: int, column: int) -> None:
        if row < 0:
            raise ValueError(ERR_ROW_MIN)
        if row >= BOARD_SIZE:
            raise ValueError(ERR_ROW_MAX)
        if column < 0:
            raise ValueError(ERR_COL_MIN)
        if column >= BOARD_SIZE:
            raise ValueError(ERR_COL_MAX)

        self.row = row
        self.column = column

    def can_attack(self, another_queen: Queen) -> bool:
        if (another_queen.row, another_queen.column) == (self.row, self.column):
            raise ValueError(ERR_DUPLICATE)

        return (
            another_queen.row == self.row
            or another_queen.column == self.column
            or abs(another_queen.row - self.row) == abs(another_queen.column - self.column)
        )
