from string import ascii_uppercase


def is_pangram(sentence: str) -> bool:
    return set(sentence.upper()) >= set(ascii_uppercase)
