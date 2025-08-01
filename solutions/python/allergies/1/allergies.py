from __future__ import annotations

from enum import IntFlag, unique


@unique
class Allergies(IntFlag):
    EGGS = 1 << 0
    PEANUTS = 1 << 1
    SHELLFISH = 1 << 2
    STRAWBERRIES = 1 << 3
    TOMATOES = 1 << 4
    CHOCOLATE = 1 << 5
    POLLEN = 1 << 6
    CATS = 1 << 7

    def allergic_to(self, item: str) -> bool:
        return Allergies[item.upper()] in self

    @property
    def lst(self) -> list[str]:
        return [flag.name.lower() for flag in self]  # type: ignore
