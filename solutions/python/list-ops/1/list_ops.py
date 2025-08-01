from __future__ import annotations

from typing import Any, Callable


def append(list1: list, list2: list) -> list:
    return list1 + list2


def concat(lists: list[list]) -> list:
    result = []
    for el in lists:
        result += el

    return result


def filter(function: Callable[[Any], bool], list: list) -> list:
    return [el for el in list if function(el)]


def length(list: list) -> int:
    i = 0
    for _ in list:
        i += 1

    return i


def map(function: Callable, list: list) -> list:
    return [function(el) for el in list]


def foldl(function: Callable, list: list, initial: Any) -> Any:
    for el in list:
        initial = function(initial, el)

    return initial


def foldr(function: Callable, list: list, initial: Any) -> Any:
    for el in list[::-1]:
        initial = function(initial, el)

    return initial


def reverse(list: list) -> list:
    return list[::-1]
