from typing import Any


def is_iterable(obj: Any) -> bool:
    try:
        iter(obj)
    except TypeError:
        return False

    return True


def flatten(iterable: list) -> list:
    result: list = []

    for element in iterable:
        if is_iterable(element):
            result += flatten(element)
        elif element is not None:
            result += [element]

    return result
