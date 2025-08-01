import string

DOUBLE = str.maketrans(string.digits, "0246813579")


class Luhn:
    card_num: str

    def __init__(self, card_num: str) -> None:
        self.card_num = card_num.replace(" ", "")

    def valid(self) -> bool:
        if len(self.card_num) <= 1:
            return False

        total = 0
        for index, digit in enumerate(self.card_num[::-1]):
            if digit not in string.digits:
                return False

            total += int(digit.translate(DOUBLE) if index % 2 else digit)

        return not total % 10
