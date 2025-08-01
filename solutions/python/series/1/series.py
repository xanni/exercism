from __future__ import annotations

ERR_LENGTH_INVALID = "slice length cannot be greater than series length"
ERR_LENGTH_NEGATIVE = "slice length cannot be negative"
ERR_LENGTH_ZERO = "slice length cannot be zero"
ERR_SERIES_EMPTY = "series cannot be empty"


def slices(series: str, length: int) -> list[str]:
    if not series:
        raise ValueError(ERR_SERIES_EMPTY)

    if length < 0:
        raise ValueError(ERR_LENGTH_NEGATIVE)

    if length == 0:
        raise ValueError(ERR_LENGTH_ZERO)

    if length > len(series):
        raise ValueError(ERR_LENGTH_INVALID)

    return [series[start : start + length] for start in range(len(series) - length + 1)]
