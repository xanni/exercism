from __future__ import annotations

DEFAULT_STUDENTS = [
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
]

PLANTS = {"C": "Clover", "G": "Grass", "R": "Radishes", "V": "Violets"}


class Garden:
    def __init__(self, diagram: str, students: list[str] = DEFAULT_STUDENTS) -> None:
        gardens = [[row[i : i + 2] for i in range(0, len(row), 2)] for row in diagram.splitlines()]
        self.gardens = [row[0] + row[1] for row in zip(*gardens)]
        self.students = sorted(students)

    def plants(self, student: str) -> list[str]:
        return [PLANTS[plant] for plant in self.gardens[self.students.index(student)]]
