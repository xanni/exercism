import re

REGEX = re.compile(r"(?: ^|[ -] ) [^- a-z]* ([a-z])", re.IGNORECASE | re.VERBOSE)


def abbreviate(words: str) -> str:
    return "".join(REGEX.findall(words)).upper()
