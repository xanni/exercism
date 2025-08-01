import re

ALPHABET = "abcdefghijklmnopqrstuvwxyz"
PUNCTUATION = " ,."

CIPHER = str.maketrans(ALPHABET + ALPHABET.upper(), ALPHABET[::-1] * 2, PUNCTUATION)
GROUP = re.compile(r".{1,5}")


def encode(plain_text: str) -> str:
    return " ".join(re.findall(GROUP, plain_text.translate(CIPHER)))


def decode(ciphered_text: str) -> str:
    return ciphered_text.translate(CIPHER)
