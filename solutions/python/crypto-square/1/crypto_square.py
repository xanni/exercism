from math import ceil, sqrt
from string import punctuation


def cipher_text(plain_text: str) -> str:
    source = plain_text.translate(str.maketrans("", "", punctuation + " ")).lower()
    if not source:
        return ""

    cols = ceil(sqrt(len(source)))
    source += " " * (-len(source) % cols)

    return " ".join(source[start::cols] for start in range(cols))
