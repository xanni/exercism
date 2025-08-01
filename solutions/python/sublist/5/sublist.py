from enum import Enum, auto, global_enum


# Possible sublist categories.
@global_enum
class Category(Enum):
    SUBLIST = auto()
    SUPERLIST = auto()
    EQUAL = auto()
    UNEQUAL = auto()


def _is_sublist(a: list, b: list) -> bool:
    return any(a == b[i : i + len(a)] for i in range(len(b) - len(a) + 1))


def sublist(list_one: list, list_two: list) -> Category:
    if list_one == list_two:
        return Category.EQUAL

    if _is_sublist(list_one, list_two):
        return Category.SUBLIST

    if _is_sublist(list_two, list_one):
        return Category.SUPERLIST

    return Category.UNEQUAL
