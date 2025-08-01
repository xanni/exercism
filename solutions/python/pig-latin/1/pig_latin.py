import re

RULES = re.compile(
    r"""
    ( (?: q(?!u) | x(?!r) | y(?!t) | [bcdfghjklmnprstvwz] )* (?:qu)? )
    ( (?:xr)? (?:yt)? \w+ )
    """,
    re.IGNORECASE | re.VERBOSE,
)


def translate(text: str) -> str:
    return re.sub(RULES, r"\2\1ay", text)
