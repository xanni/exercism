from __future__ import annotations


def factors(value: int) -> list[int]:
    f: list[int] = []

    while not value % 2:
        f.append(2)
        value //= 2

    while not value % 3:
        f.append(3)
        value //= 3

    divisor, skip = 5, 4

    while divisor * divisor <= value:
        if value % divisor:
            divisor += skip
            skip = 2 - skip + 4  # skip 6-coprime divisors
        else:
            f.append(divisor)
            value //= divisor

    if value > 1:
        f.append(value)

    return f
