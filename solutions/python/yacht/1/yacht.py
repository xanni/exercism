from __future__ import annotations

from collections import Counter
from enum import IntEnum, auto


# Score categories.
class Category(IntEnum):
    ONES = 1
    TWOS = 2
    THREES = 3
    FOURS = 4
    FIVES = 5
    SIXES = 6
    FULL_HOUSE = auto()
    FOUR_OF_A_KIND = auto()
    LITTLE_STRAIGHT = auto()
    BIG_STRAIGHT = auto()
    CHOICE = auto()
    YACHT = auto()


globals().update(Category.__members__)


def score(dice: list[int], category: Category) -> int:  # noqa: PLR0911
    counted = Counter(dice).most_common(2)
    match category:
        case 1 | 2 | 3 | 4 | 5 | 6 as value:
            return sum(die for die in dice if die == value)
        case Category.FULL_HOUSE if counted[0][1] == 3 and counted[1][1] == 2:  # noqa: PLR2004
            return sum(dice)
        case Category.FOUR_OF_A_KIND if counted[0][1] >= 4:  # noqa: PLR2004
            return counted[0][0] * 4
        case Category.LITTLE_STRAIGHT if sorted(dice) == [1, 2, 3, 4, 5]:
            return 30
        case Category.BIG_STRAIGHT if sorted(dice) == [2, 3, 4, 5, 6]:
            return 30
        case Category.CHOICE:
            return sum(dice)
        case Category.YACHT if len(set(dice)) == 1:
            return 50

    return 0
