from __future__ import annotations


def triplets_with_sum(number: int) -> list[list[int]]:
    doubled = 2 * number
    squared = number * number
    triplets: list[list[int]] = []

    # Since a < b < c, b >= a + 1 and c >= a + 2
    # Since a + b + c == number, a <= (number - 3) // 3
    for a in range(1, ((number - 3) // 3) + 1):
        # Since a + b + c == number, b == number - a - c and c == number - a - b
        # Then b^2 == (number - a - c)^2 and c^2 == (number - a - b)^2
        # Expanded: b^2 == number^2 + a^2 + c^2 - 2*number - 2*a + 2*a*c
        # and c^2 == number^2 + a^2 + b^2 - 2*number - 2*a + 2*a*b
        # Therefore b = (number^2 - 2*number*a) // (2*number - 2*a)
        b, r = divmod(squared - a * doubled, doubled - 2 * a)
        if b <= a:
            break

        if not r:
            triplets.append([a, b, number - a - b])

    return triplets
