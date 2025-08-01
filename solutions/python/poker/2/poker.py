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


TIE_BREAK_RANKS = {Rank.FOUR_OF_A_KIND, Rank.FULL_HOUSE, Rank.THREE_OF_A_KIND}


class Card:
    def __init__(self, desc: str) -> None:
        self.value = VALUES.index(desc[:-1])
        self.suit = desc[-1:]

    def __lt__(self, other: Card) -> bool:
        return self.value < other.value

    def __repr__(self) -> str:
        return VALUES[self.value] + self.suit


# ruff: noqa: PLR2004
class Hand:
    def __init__(self, desc: str) -> None:
        self.desc = desc
        self.cards = sorted(Card(card) for card in desc.split())
        most_common = Counter(card.value for card in self.cards).most_common(2)
        self.most_common = most_common[0][0]
        groups = tuple(most_common[i][1] for i in (0, 1))

        is_flush = len({card.suit for card in self.cards}) == 1
        is_straight = groups == (1, 1) and self.cards[4].value - self.cards[0].value == 4
        is_wheel = tuple(card.value for card in self.cards) == (0, 1, 2, 3, ACE)

        if is_straight and is_flush:
            self.rank = Rank.STRAIGHT_FLUSH
        elif is_wheel and is_flush:
            self.rank = Rank.STEEL_WHEEL
        elif groups == (4, 1):
            self.rank = Rank.FOUR_OF_A_KIND
        elif groups == (3, 2):
            self.rank = Rank.FULL_HOUSE
        elif is_flush:
            self.rank = Rank.FLUSH
        elif is_straight:
            self.rank = Rank.STRAIGHT
        elif is_wheel:
            self.rank = Rank.BABY_STRAIGHT
        elif groups == (3, 1):
            self.rank = Rank.THREE_OF_A_KIND
        elif groups == (2, 2):
            self.rank = Rank.TWO_PAIR
        elif groups == (2, 1):
            self.rank = Rank.PAIR
        else:
            self.rank = Rank.HIGH_CARD

    def __lt__(self, other: Hand) -> bool:
        if self.rank != other.rank:
            return self.rank < other.rank

        if self.rank in TIE_BREAK_RANKS and self.most_common != other.most_common:
            return self.most_common < other.most_common

        for i in range(-1, -6, -1):
            if self.cards[i].value != other.cards[i].value:
                return self.cards[i].value < other.cards[i].value

        return False

    def __repr__(self) -> str:
        return f"{self.rank.name}: " + " ".join(repr(card) for card in self.cards)

    def __str__(self) -> str:
        return self.desc


def best_hands(hands: list[str]) -> list[str]:
    ranked_hands = tuple(Hand(hand) for hand in hands)
    best = max(ranked_hands)
    return [str(hand) for hand in ranked_hands if not hand < best]
