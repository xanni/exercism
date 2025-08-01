BRACKET = {"[": "]", "{": "}", "(": ")"}


def is_paired(input_string: str) -> bool:
    stack: list[str] = []

    for char in input_string:
        if char in BRACKET:
            stack += char
        elif char in BRACKET.values() and (not stack or char != BRACKET[stack.pop()]):
            return False

    return not stack
