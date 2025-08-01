from __future__ import annotations


def primes(limit: int) -> list[int]:
    candidates = list(range(2, limit + 1))

    for divisor in candidates:
        square = divisor * divisor
        if square > limit:
            break

        if divisor:
            for i in range(square - 2, len(candidates), divisor):
                candidates[i] = 0

    return list(filter(None, candidates))
