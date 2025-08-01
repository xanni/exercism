import re
from string import ascii_letters, ascii_lowercase, punctuation, whitespace

CIPHER = str.maketrans(ascii_letters, ascii_lowercase[::-1] * 2, punctuation + whitespace)
GROUP = re.compile(r".{1,5}")


def encode(plain_text: str) -> str:
    return " ".join(re.findall(GROUP, plain_text.translate(CIPHER)))


def decode(ciphered_text: str) -> str:
    return ciphered_text.translate(CIPHER)
