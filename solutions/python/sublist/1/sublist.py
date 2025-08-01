from enum import Enum, auto


# Possible sublist categories.
class Category(Enum):
    SUBLIST = auto()
    SUPERLIST = auto()
    EQUAL = auto()
    UNEQUAL = auto()


globals().update(Category.__members__)  # Export to tests


def sublist(list_one: list, list_two: list) -> Category:
    if list_one == list_two:
        return Category.EQUAL

    l1 = len(list_one)
    if not l1:
        return Category.SUBLIST

    l2 = len(list_two)
    if not l2:
        return Category.SUPERLIST

    if l1 < l2:
        for i in range(l2 - l1 + 1):
            if list_one == list_two[i : i + l1]:
                return Category.SUBLIST

    if l1 > l2:
        for i in range(l1 - l2 + 1):
            if list_two == list_one[i : i + l2]:
                return Category.SUPERLIST

    return Category.UNEQUAL
