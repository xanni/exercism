import re

DECODE = re.compile(r"(\d+) ([a-zA-Z\s])", re.VERBOSE)
ENCODE = re.compile(r"([a-zA-Z\s]) \1+", re.VERBOSE)


def decode(string: str) -> str:
    return DECODE.sub(lambda m: int(m.group(1)) * m.group(2), string)


def encode(string: str) -> str:
    return ENCODE.sub(lambda m: str(len(m.group())) + m.group(1), string)
