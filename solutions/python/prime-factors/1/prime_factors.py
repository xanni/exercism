from __future__ import annotations

WHEEL = [4, 2, 4, 2, 4, 6, 2, 6]
WHEEL_SIZE = len(WHEEL)


def factors(value: int) -> list[int]:
    f: list[int] = []

    while not value % 2:
        f.append(2)
        value //= 2

    while not value % 3:
        f.append(3)
        value //= 3

    while not value % 5:
        f.append(5)
        value //= 5

    candidate = 7
    i = 0

    while candidate * candidate <= value:
        if value % candidate:
            candidate += WHEEL[i]
            i = (i + 1) % WHEEL_SIZE
        else:
            f.append(candidate)
            value //= candidate

    if value > 1:
        f.append(value)

    return f
