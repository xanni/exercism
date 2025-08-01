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
    match category:
        case 1 | 2 | 3 | 4 | 5 | 6 as value:
            return dice.count(value) * value
        case Category.FULL_HOUSE if set(Counter(dice).values()) == {2, 3}:
            return sum(dice)
        case Category.FOUR_OF_A_KIND:
            die, count = Counter(dice).most_common(1)[0]
            if count >= 4:  # noqa: PLR2004
                return die * 4
        case Category.LITTLE_STRAIGHT if set(dice) == {1, 2, 3, 4, 5}:
            return 30
        case Category.BIG_STRAIGHT if set(dice) == {2, 3, 4, 5, 6}:
            return 30
        case Category.CHOICE:
            return sum(dice)
        case Category.YACHT if len(set(dice)) == 1:
            return 50

    return 0
