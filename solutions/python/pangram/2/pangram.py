from string import ascii_uppercase

ALPHABET = set(ascii_uppercase)


def is_pangram(sentence: str) -> bool:
    return ALPHABET.issubset(sentence.upper())
