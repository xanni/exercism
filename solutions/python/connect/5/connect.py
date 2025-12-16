class ConnectGame:
    @staticmethod
    def __build_path(connectome: list[set], row: int, col: int) -> None:
        """Given a connectome (a list of paths, each of which is a set of coordinates)
        and a coordinate, add the coordinate to any path that is hexagonally adjacent,
        merging any paths that are joined together by the new coordinate."""
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

    def __init__(self, board: str) -> None:
        self.board = board.replace(" ", "").split("\n")
        self.last_col, self.last_row = len(self.board[0]) - 1, len(self.board) - 1
        self.o_connectome: list[set] = []
        self.x_connectome: list[set] = []

        for row, line in enumerate(self.board):
            for col, field in enumerate(line):
                if field == "O":
                    self.__build_path(self.o_connectome, row, col)
                elif field == "X":
                    self.__build_path(self.x_connectome, row, col)

    def get_winner(self) -> str:
        for path in self.o_connectome:
            if {0, self.last_row} <= {row for row, _ in path}:
                return "O"

        for path in self.x_connectome:
            if {0, self.last_col} <= {col for _, col in path}:
                return "X"

        return ""
