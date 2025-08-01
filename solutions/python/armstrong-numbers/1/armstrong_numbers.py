def is_armstrong_number(number: int) -> bool:
    digits = str(number)
    return number == sum(int(digit) ** len(digits) for digit in digits)
