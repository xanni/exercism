COUNTRY_CODE = "1"

ERR_AREA_CODE_0 = "area code cannot start with zero"
ERR_AREA_CODE_1 = "area code cannot start with one"
ERR_COUNTRY_CODE = "11 digits must start with 1"
ERR_LETTERS = "letters not permitted"
ERR_MAX_11 = "must not be greater than 11 digits"
ERR_MIN_10 = "must not be fewer than 10 digits"
ERR_PUNCTUATION = "punctuations not permitted"
ERR_EXCH_CODE_0 = "exchange code cannot start with zero"
ERR_EXCH_CODE_1 = "exchange code cannot start with one"

MIN_LENGTH = 10
MAX_LENGTH = 11
PUNCTUATION = "`~!@#$%^&*_=[]{}\\|;:'\",<>/?"


class PhoneNumber:
    def __init__(self, number: str) -> None:
        if any(c.isalpha() for c in number):
            raise ValueError(ERR_LETTERS)
        if any(c in PUNCTUATION for c in number):
            raise ValueError(ERR_PUNCTUATION)

        self.number = "".join(digit for digit in filter(lambda d: d.isdigit(), number))
        if len(self.number) < MIN_LENGTH:
            raise ValueError(ERR_MIN_10)
        if len(self.number) > MAX_LENGTH:
            raise ValueError(ERR_MAX_11)

        if len(self.number) == MAX_LENGTH:
            if self.number[0] == COUNTRY_CODE:
                self.number = self.number[1:]
            else:
                raise ValueError(ERR_COUNTRY_CODE)

        if self.number[0] == "0":
            raise ValueError(ERR_AREA_CODE_0)
        if self.number[0] == "1":
            raise ValueError(ERR_AREA_CODE_1)

        if self.number[3] == "0":
            raise ValueError(ERR_EXCH_CODE_0)
        if self.number[3] == "1":
            raise ValueError(ERR_EXCH_CODE_1)

        self.area_code = self.number[:3]

    def pretty(self) -> str:
        return f"({self.area_code})-{self.number[3:6]}-{self.number[6:]}"
