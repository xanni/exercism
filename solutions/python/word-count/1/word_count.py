from __future__ import annotations

import re
from collections import Counter

WORDS = re.compile(r"( \b [a-z1-9] \b | [a-z1-9] [a-z1-9']* [a-z1-9] )", re.VERBOSE)


def count_words(sentence: str) -> dict[str, int]:
    return Counter(WORDS.findall(sentence.lower()))
