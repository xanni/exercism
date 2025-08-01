def square_root(number: int) -> int:
    if number <= 1:
        return number

    estimate = 2 << (number.bit_length() >> 1)  # Initial estimate

    while True:
        update = (estimate + number // estimate) >> 1
        if update >= estimate:
            return estimate

        estimate = update
