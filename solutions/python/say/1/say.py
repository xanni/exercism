ERR_RANGE = "input out of range"
MAX_INPUT = int(1e12) - 1
NUMBERS = (
    "",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "ten",
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "fifteen",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen",
)
NUMBERS_LEN = len(NUMBERS)
TENS = ("twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety")
TENS_START = 20
THOUSANDS = ("thousand", "million", "billion", "trillion")


def _small_number(number: int) -> str:
    text = ""
    if number >= 100:
        text = NUMBERS[number // 100] + " hundred"

    if not number % 100:
        return text

    if number >= 100:
        number %= 100
        text += " "

    if number < NUMBERS_LEN:
        return text + NUMBERS[number]

    text += TENS[(number - TENS_START) // 10]
    if number % 10:
        text += "-" + NUMBERS[number % 10]

    return text


def say(number: int) -> str:
    if number < 0 or number > MAX_INPUT:
        raise ValueError(ERR_RANGE)

    if number == 0:
        return "zero"

    text = ""
    for prefix in THOUSANDS:
        text = _small_number(number % 1000) + " " + text

        if number < 1000:
            break

        number //= 1000

        if number % 1000:
            text = prefix + " " + text

    return text.strip()
