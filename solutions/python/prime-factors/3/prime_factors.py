from __future__ import annotations


def factors(value: int) -> list[int]:
    f: list[int] = []

    for divisor in (2, 3):
        while not value % divisor:
            f.append(divisor)
            value //= divisor

    divisor, skip = 5, 4

    while divisor * divisor <= value:
        if value % divisor:
            divisor += skip
            skip = 6 - skip  # skip 6-coprime divisors
        else:
            f.append(divisor)
            value //= divisor

    if value > 1:
        f.append(value)

    return f
