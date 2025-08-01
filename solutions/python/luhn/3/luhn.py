import string

DOUBLE = str.maketrans(string.digits, "0246813579")


class Luhn:
    card_num: str

    def __init__(self, card_num: str) -> None:
        self.card_num = card_num.replace(" ", "")

    def valid(self) -> bool:
        return (
            len(self.card_num) > 1
            and self.card_num.isdigit()
            and not sum(
                int(digit.translate(DOUBLE) if index % 2 else digit)
                for index, digit in enumerate(self.card_num[::-1])
            )
            % 10
        )
