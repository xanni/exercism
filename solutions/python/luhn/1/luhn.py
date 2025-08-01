import string

DOUBLE = str.maketrans(string.digits, "0246813579")


class Luhn:
    card_num: str

    def __init__(self, card_num: str) -> None:
        self.card_num = card_num.replace(" ", "")

    def valid(self) -> bool:
        if len(self.card_num) <= 1 or not all(digit in string.digits for digit in self.card_num):
            return False

        return (
            not (
                sum(int(digit) for digit in self.card_num[::-2])
                + sum(int(digit.translate(DOUBLE)) for digit in self.card_num[-2::-2])
            )
            % 10
        )
