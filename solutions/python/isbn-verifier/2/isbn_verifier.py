import re

REGEX = re.compile(r"(\d)-?" * 9 + r"([X\d])")


def is_valid(isbn: str) -> bool:
    match = REGEX.fullmatch(isbn)
    if not match:
        return False

    check_digits = list(match.groups())
    if check_digits[-1] == "X":
        check_digits[-1] = "10"

    return not sum(int(check_digits[-i]) * i for i in range(1, 11)) % 11
