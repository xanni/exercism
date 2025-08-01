from __future__ import annotations

FIRST_PRIME = 2


def primes(limit: int) -> list[int]:
    candidates = [True] * (limit - 1)

    for divisor in range(FIRST_PRIME, limit):
        square = divisor * divisor
        if square > limit:
            break

        if candidates[divisor - FIRST_PRIME]:
            for i in range(square - FIRST_PRIME, len(candidates), divisor):
                candidates[i] = False

    return [i + FIRST_PRIME for i, is_prime in enumerate(candidates) if is_prime]
