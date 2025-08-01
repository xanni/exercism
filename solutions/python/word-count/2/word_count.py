from __future__ import annotations

import re
from collections import Counter

WORDS = re.compile(r"[a-z0-9]+ (?: ' [a-z]+ )?", re.VERBOSE)


def count_words(sentence: str) -> dict[str, int]:
    return Counter(WORDS.findall(sentence.lower()))
