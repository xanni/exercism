from __future__ import annotations


def transform(legacy_data: dict[int, list]) -> dict[str, int]:
    return {letter.lower(): score for score, letters in legacy_data.items() for letter in letters}
