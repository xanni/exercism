from __future__ import annotations


def primes(limit: int) -> list[int]:
    candidates = [False] + [True] * (limit - 1)  # 1 is not prime

    for divisor in range(2, limit):
        square = divisor * divisor
        if square > limit:
            break

        if candidates[divisor - 1]:
            for i in range(square - 1, len(candidates), divisor):
                candidates[i] = False

    return [i + 1 for i, prime in enumerate(candidates) if prime]
