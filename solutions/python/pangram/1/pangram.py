import re

ENGLISH_LETTERS = 26
REGEX = re.compile("[A-Z]")


def is_pangram(sentence: str) -> bool:
    return len(set(re.findall(REGEX, sentence.upper()))) == ENGLISH_LETTERS
