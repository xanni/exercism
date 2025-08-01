from __future__ import annotations


def transform(legacy_data: dict[int, list]) -> dict[str, int]:
    new_data: dict[str, int] = {}

    for score, letters in legacy_data.items():
        new_data |= ((letter.lower(), score) for letter in letters)

    return new_data
