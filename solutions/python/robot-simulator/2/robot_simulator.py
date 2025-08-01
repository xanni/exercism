from __future__ import annotations

from enum import Enum, global_enum

ERR_COMMAND = "Invalid command"


@global_enum
class Dir(complex, Enum):
    NORTH = 1j
    EAST = 1
    SOUTH = -1j
    WEST = -1


class Robot:
    def __init__(self, direction: Dir = Dir.NORTH, x_pos: int = 0, y_pos: int = 0) -> None:
        self.direction = direction
        self._location = x_pos + y_pos * 1j

    @property
    def coordinates(self) -> tuple[int, int]:
        return (int(self._location.real), int(self._location.imag))

    def move(self, commands: str) -> None:
        for command in commands:
            match command:
                case "A":
                    self._location += self.direction
                case "L":
                    self.direction = Dir(self.direction * 1j)
                case "R":
                    self.direction = Dir(self.direction * -1j)
                case _:
                    raise ValueError(ERR_COMMAND)
