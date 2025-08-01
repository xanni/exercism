from __future__ import annotations

from enum import IntEnum, global_enum


@global_enum
class Dir(IntEnum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3


class Robot:
    def __init__(self, direction: Dir = Dir.NORTH, x_pos: int = 0, y_pos: int = 0) -> None:
        self.direction = direction
        self.x_pos = x_pos
        self.y_pos = y_pos

    @property
    def coordinates(self) -> tuple[int, int]:
        return (self.x_pos, self.y_pos)

    def move(self, commands: str) -> None:
        for command in commands:
            match command:
                case "A":
                    match self.direction:
                        case Dir.NORTH:
                            self.y_pos += 1
                        case Dir.EAST:
                            self.x_pos += 1
                        case Dir.SOUTH:
                            self.y_pos -= 1
                        case Dir.WEST:
                            self.x_pos -= 1
                case "L":
                    self.direction = Dir((self.direction - 1) % 4)
                case "R":
                    self.direction = Dir((self.direction + 1) % 4)
