ERR_POSINT_REQUIRED = "Only positive integers are allowed"


def steps(number: int) -> int:
    if number < 1:
        raise ValueError(ERR_POSINT_REQUIRED)

    steps = 0
    while number > 1:
        steps += 1
        number = 3 * number + 1 if number % 2 else number // 2

    return steps
