"""Solution to Ellen's Alien Game exercise."""

from __future__ import annotations

from typing import Any


class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes
    ----------
    (class)total_aliens_created: int
    x_coordinate: int - Position on the x-axis.
    y_coordinate: int - Position on the y-axis.
    health: int - Number of health points.

    Methods
    -------
    hit(): Decrement Alien health by one point.
    is_alive(): Return a boolean for if Alien is alive (if health is > 0).
    teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
    collision_detection(other): Implementation TBD.
    """

    total_aliens_created = 0

    def __init__(self, x_coordinate: int, y_coordinate: int) -> None:
        self.health = 3
        self.teleport(x_coordinate, y_coordinate)
        Alien.total_aliens_created += 1

    def collision_detection(self, other: Any) -> None:
        pass

    def hit(self) -> None:
        if self.is_alive():
            self.health -= 1

    def is_alive(self) -> bool:
        return self.health > 0

    def teleport(self, x_coordinate: int, y_coordinate: int) -> None:
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate


def new_aliens_collection(positions: list[tuple[int, int]]) -> list[Alien]:
    return [Alien(*position) for position in positions]
