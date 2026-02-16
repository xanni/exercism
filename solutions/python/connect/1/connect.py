class ConnectGame:
    def __init__(self, board: str) -> None:
        self.board = [line.lstrip() for line in board.split("\n")]
        self.o_connectome: list[set] = []
        self.x_connectome: list[set] = []
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                if self.board[row][col] == "O":
                    self.__build_path(self.o_connectome, row, col)
                if self.board[row][col] == "X":
                    self.__build_path(self.x_connectome, row, col)

    def __build_path(self, connectome: list[set], row: int, col: int) -> None:
        matches = [
            index
            for index, path in enumerate(connectome)
            if any(n in path for n in [(row - 1, col), (row - 1, col + 2), (row, col - 2)])
        ]

        if not matches:
            connectome.append({(row, col)})  # New path
            return

        first = matches[0]
        connectome[first].add((row, col))
        if len(matches) == 1:
            return

        # There can be at most two, so merge them into one path
        second = matches[1]
        connectome[first] |= connectome[second]
        del connectome[second]

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
