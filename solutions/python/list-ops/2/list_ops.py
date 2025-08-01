from __future__ import annotations

from typing import Any, Callable


def append(list1: list, list2: list) -> list:
    return list1 + list2


def concat(lists: list[list]) -> list:
    return [element for el in lists for element in el]


def filter(function: Callable[[Any], bool], list: list) -> list:
    return [el for el in list if function(el)]


def length(list: list) -> int:
    return sum(1 for _ in list)


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
