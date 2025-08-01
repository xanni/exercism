from __future__ import annotations

ERR_NOT_FOUND = "value not in array"


def find(search_list: list[int], value: int) -> int:
    lower_bound = 0
    upper_bound = len(search_list)

    while lower_bound < upper_bound:
        pivot = lower_bound + (upper_bound - lower_bound) // 2
        candidate = search_list[pivot]
        if candidate == value:
            return pivot

        if candidate < value:
            lower_bound = pivot + 1
        else:  # candidate > value
            upper_bound = pivot

    raise ValueError(ERR_NOT_FOUND)
