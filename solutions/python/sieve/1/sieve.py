from __future__ import annotations


def primes(limit: int) -> list[int]:
    candidates = list(range(2, limit + 1))

    for i, divisor in enumerate(candidates):
        if divisor:
            for j in range(i + divisor, len(candidates), divisor):
                candidates[j] = 0

    return list(filter(None, candidates))
