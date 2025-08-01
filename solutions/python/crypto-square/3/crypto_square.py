from math import ceil, sqrt
from string import punctuation


def cipher_text(plain_text: str) -> str:
    source = plain_text.translate(str.maketrans("", "", punctuation + " ")).lower()
    if not source:
        return ""

    rows = ceil(sqrt(len(source)))
    source += " " * (-len(source) % rows)

    return " ".join(source[start::rows] for start in range(rows))
