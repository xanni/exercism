from __future__ import annotations

from collections import Counter
from enum import IntEnum, auto

VALUES = tuple("2 3 4 5 6 7 8 9 10 J Q K A".split())
ACE = len(VALUES) - 1


class Rank(IntEnum):
    HIGH_CARD = auto()
    PAIR = auto()
    TWO_PAIR = auto()
    THREE_OF_A_KIND = auto()
    BABY_STRAIGHT = auto()
    STRAIGHT = auto()
    FLUSH = auto()
    FULL_HOUSE = auto()
    FOUR_OF_A_KIND = auto()
    STEEL_WHEEL = auto()
    STRAIGHT_FLUSH = auto()


class Card:
    def __init__(self, desc: str) -> None:
        self.value = VALUES.index(desc[:-1])
        self.suit = desc[-1:]

    def __lt__(self, other: Card) -> bool:
        return self.value < other.value

    def __repr__(self) -> str:
        return VALUES[self.value] + self.suit


class Hand:
    def __init__(self, desc: str) -> None:
        self.desc = desc
        self.cards = sorted(Card(card) for card in desc.split())
        self.most_common = Counter(card.value for card in self.cards).most_common(2)

        is_flush = all(card.suit == self.cards[0].suit for card in self.cards)
        is_straight = all(self.cards[i].value + 1 == self.cards[i + 1].value for i in range(4))
        is_wheel = self.cards[-1].value == ACE and all(self.cards[i].value == i for i in range(4))

        if is_straight and is_flush:
            self.rank = Rank.STRAIGHT_FLUSH
        elif is_wheel and is_flush:
            self.rank = Rank.STEEL_WHEEL
        elif self.most_common[0][1] == 4:  # noqa: PLR2004
            self.rank = Rank.FOUR_OF_A_KIND
        elif self.most_common[0][1] == 3 and self.most_common[1][1] == 2:  # noqa: PLR2004
            self.rank = Rank.FULL_HOUSE
        elif is_flush:
            self.rank = Rank.FLUSH
        elif is_straight:
            self.rank = Rank.STRAIGHT
        elif is_wheel:
            self.rank = Rank.BABY_STRAIGHT
        elif self.most_common[0][1] == 3:  # noqa: PLR2004
            self.rank = Rank.THREE_OF_A_KIND
        elif self.most_common[0][1] == 2 and self.most_common[1][1] == 2:  # noqa: PLR2004
            self.rank = Rank.TWO_PAIR
        elif self.most_common[0][1] == 2:  # noqa: PLR2004
            self.rank = Rank.PAIR
        else:
            self.rank = Rank.HIGH_CARD

    def __lt__(self, other: Hand) -> bool:
        if self.rank != other.rank:
            return self.rank < other.rank

        if (
            self.rank in {Rank.FOUR_OF_A_KIND, Rank.FULL_HOUSE, Rank.THREE_OF_A_KIND}
            and self.most_common[0][0] != other.most_common[0][0]
        ):
            return self.most_common[0][0] < other.most_common[0][0]

        for i in range(-1, -6, -1):
            if self.cards[i].value != other.cards[i].value:
                return self.cards[i].value < other.cards[i].value

        return False

    def __repr__(self) -> str:
        return f"{self.rank.name}: " + " ".join(repr(card) for card in self.cards)

    def __str__(self) -> str:
        return self.desc


def best_hands(hands: list[str]) -> list[str]:
    sorted_hands = sorted(Hand(hand) for hand in hands)
    best = sorted_hands[-1]
    return [str(hand) for hand in sorted_hands if not hand < best]
