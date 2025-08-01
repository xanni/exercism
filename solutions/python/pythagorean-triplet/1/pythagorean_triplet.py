from __future__ import annotations


def triplets_with_sum(number: int) -> list[list[int]]:
    doubled = 2 * number
    squared = number * number
    triplets: list[list[int]] = []

    # Since a < b < c, b must be at least a + 1 and c must be at least a + 2
    # Since a + b + c == number, a must be <= (number - 3) // 3
    for a in range(1, ((number - 3) // 3) + 1):
        b, r = divmod(squared - a * doubled, doubled - 2 * a)
        if b <= a:
            break

        if not r:
            triplets.append([a, b, number - a - b])

    return triplets
