# Given a connectome (a list of paths, each of which is a set of coordinates)
# and a coordinate, add the coordinate to any path that is hexagonally adjacent,
# merging any paths that are joined together by the new coordinate.
def __build_path(connectome: list[set], row: int, col: int) -> None:
    matches = [
        index
        for index, path in enumerate(connectome)
        if any(n in path for n in [(row - 1, col), (row - 1, col + 1), (row, col - 1)])
    ]

    if not matches:
        connectome.append({(row, col)})  # New path
        return

    first = matches[0]
    connectome[first].add((row, col))
    if len(matches) == 1:
        return

    # There can be at most two existing paths connected to this coordinate.
    second = matches[1]
    connectome[first] |= connectome[second]  # Merge them into one path.
    del connectome[second]


class ConnectGame:
    def __init__(self, board: str) -> None:
        self.board = board.replace(" ", "").split("\n")
        self.o_connectome: list[set] = []
        self.x_connectome: list[set] = []

        for row, line in enumerate(self.board):
            for col, field in enumerate(line):
                if field == "O":
                    __build_path(self.o_connectome, row, col)
                elif field == "X":
                    __build_path(self.x_connectome, row, col)

    def get_winner(self) -> str:
        last_col, last_row = len(self.board[0]) - 1, len(self.board) - 1

        for path in self.o_connectome:
            top, bottom = False, False
            for row, _ in path:
                if row == 0:
                    top = True
                if row == last_row:
                    bottom = True
            if top and bottom:
                return "O"

        for path in self.x_connectome:
            left, right = False, False
            for _, col in path:
                if col == 0:
                    left = True
                if col == last_col:
                    right = True
            if left and right:
                return "X"

        return ""
