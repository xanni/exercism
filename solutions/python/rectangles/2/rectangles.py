from __future__ import annotations


def rectangles(strings: list[str]) -> int:
    def horizontal(y: int, left: int, right: int) -> bool:
        return all(c in "+-" for c in strings[y][left + 1 : right])

    def vertical(x: int, top: int, bottom: int) -> bool:
        return all(s[x] in "+|" for s in strings[top + 1 : bottom])

    def is_rectangle(left: int, top: int, right: int, bottom: int) -> bool:
        return (
            strings[bottom][left] == "+"
            and strings[top][right] == "+"
            and horizontal(top, left, right)
            and horizontal(bottom, left, right)
            and vertical(left, top, bottom)
            and vertical(right, top, bottom)
        )

    corners = [(x, y) for y, s in enumerate(strings) for x, c in enumerate(s) if c == "+"]
    count = 0

    for i, (left, top) in enumerate(corners[:-3]):
        for right, bottom in corners[i + 3 :]:
            if right > left and bottom > top and is_rectangle(left, top, right, bottom):
                count += 1

    return count
