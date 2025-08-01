from random import choice, randrange, seed
from string import ascii_uppercase
from typing import ClassVar


class Robot:
    names: ClassVar[set] = set()

    def __init__(self) -> None:
        self.name = ""
        seed()
        self.reset()

    def reset(self) -> None:
        while True:
            name = f"{choice(ascii_uppercase)}{choice(ascii_uppercase)}{randrange(1000):03}"
            if name not in Robot.names:
                break

        Robot.names.discard(self.name)
        Robot.names.add(name)
        self.name = name
