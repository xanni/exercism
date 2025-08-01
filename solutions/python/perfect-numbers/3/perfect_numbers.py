from __future__ import annotations

ERR_NOT_POSINT = "Classification is only possible for positive integers."


def factors(n: int) -> set[int]:
    "Returns the set of factors of n excluding 1 and n itself"
    return {f for i in range(2, int(n**0.5) + 1) if not n % i for f in (i, n // i)}


def classify(number: int) -> str:
    """A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1:
        raise ValueError(ERR_NOT_POSINT)

    if number == 1:
        return "deficient"

    aliquot_sum = sum(factors(number)) + 1
    if number > aliquot_sum:
        return "deficient"

    if number < aliquot_sum:
        return "abundant"

    return "perfect"
