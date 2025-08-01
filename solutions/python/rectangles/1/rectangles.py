from __future__ import annotations


def rectangles(strings: list[str]) -> int:
    def horizontal(y: int, left: int, right: int) -> bool:
        return all(strings[y][x] in ["+", "-"] for x in range(left + 1, right))

    def vertical(x: int, top: int, bottom: int) -> bool:
        return all(strings[y][x] in ["+", "|"] for y in range(top + 1, bottom))

    def is_square(left: int, top: int, right: int, bottom: int) -> bool:
        return (
            strings[bottom][left] == "+"
            and strings[top][right] == "+"
            and horizontal(top, left, right)
            and horizontal(bottom, left, right)
            and vertical(left, top, bottom)
            and vertical(right, top, bottom)
        )

    corners = [(x, y) for y, s in enumerate(strings) for x, c in enumerate(s) if c == "+"]
    squares = 0

    for i, (left, top) in enumerate(corners[:-3]):
        for right, bottom in corners[i + 3 :]:
            if right > left and bottom > top and is_square(left, top, right, bottom):
                squares += 1

    return squares
