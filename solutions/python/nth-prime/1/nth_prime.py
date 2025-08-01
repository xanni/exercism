ERR_ZERO = "there is no zeroth prime"


primes = [2, 3]


def prime(number: int) -> int:
    if number == 0:
        raise ValueError(ERR_ZERO)

    candidate = primes[-1]
    while len(primes) < number:
        candidate += 2
        for divisor in primes[1:]:
            if not candidate % divisor:
                break
            if divisor * divisor > candidate:
                primes.append(candidate)
                break

    return primes[number - 1]
