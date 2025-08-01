from __future__ import annotations

from random import choices, seed
from string import ascii_uppercase, digits

names: set[str] = set()


class Robot:
    def __init__(self) -> None:
        self.name = ""
        seed()
        self.reset()

    def reset(self) -> None:
        while (name := "".join(choices(ascii_uppercase, k=2) + choices(digits, k=3))) in names:
            pass

        names.discard(self.name)
        names.add(name)
        self.name = name
