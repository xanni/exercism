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

    len_one, len_two = len(list_one), len(list_two)

    if len_one < len_two:
        for i in range(len_two - len_one + 1):
            if list_one == list_two[i : i + len_one]:
                return Category.SUBLIST

    if len_one > len_two:
        for i in range(len_one - len_two + 1):
            if list_two == list_one[i : i + len_two]:
                return Category.SUPERLIST

    return Category.UNEQUAL
