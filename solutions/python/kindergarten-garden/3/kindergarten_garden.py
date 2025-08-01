from __future__ import annotations

from typing import Sequence

DEFAULT_STUDENTS = (
    "Alice",
    "Bob",
    "Charlie",
    "David",
    "Eve",
    "Fred",
    "Ginny",
    "Harriet",
    "Ileana",
    "Joseph",
    "Kincaid",
    "Larry",
)

PLANTS = {"C": "Clover", "G": "Grass", "R": "Radishes", "V": "Violets"}


class Garden:
    def __init__(self, diagram: str, students: Sequence[str] = DEFAULT_STUDENTS) -> None:
        gardens = [[row[i : i + 2] for i in range(0, len(row), 2)] for row in diagram.splitlines()]
        self.gardens = ["".join(garden) for garden in zip(*gardens)]
        self.students = sorted(students)

    def plants(self, student: str) -> list[str]:
        return [PLANTS[plant] for plant in self.gardens[self.students.index(student)]]
