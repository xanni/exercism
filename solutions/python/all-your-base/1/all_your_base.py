from __future__ import annotations

MIN_BASE = 2

DIGIT_ERR = "all digits must satisfy 0 <= d < input base"
INPUT_ERR = "input base must be >= 2"
OUTPUT_ERR = "output base must be >= 2"


def rebase(input_base: int, digits: list[int], output_base: int) -> list[int]:
    if input_base < MIN_BASE:
        raise ValueError(INPUT_ERR)

    if output_base < MIN_BASE:
        raise ValueError(OUTPUT_ERR)

    value = 0
    for digit in digits:
        if 0 <= digit < input_base:
            value = value * input_base + digit
        else:
            raise ValueError(DIGIT_ERR)

    output: list[int] = []
    while value:
        value, digit = divmod(value, output_base)
        output.insert(0, digit)

    return output or [0]
