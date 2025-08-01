from __future__ import annotations


def primes(limit: int) -> list[int]:
    candidates = list(range(2, limit + 1))

    for divisor in candidates:
        if divisor:
            for i in range(divisor * divisor - 2, len(candidates), divisor):
                candidates[i] = 0

    return list(filter(None, candidates))
