from __future__ import annotations


class School:
    def __init__(self) -> None:
        self._roster: dict[str, int] = {}  # Mapping of student names to grade numbers
        self._success: list[bool] = []

    def add_student(self, name: str, grade: int) -> None:
        ok = name not in self._roster
        self._success.append(ok)
        if ok:
            self._roster[name] = grade

    def roster(self) -> list[str]:
        "Return student names sorted by grade and name"
        return [name for name, _ in sorted(self._roster.items(), key=lambda s: (s[1], s[0]))]

    def grade(self, grade_number: int) -> list[str]:
        "Return sorted student names that are in the given grade_number"
        return sorted([name for name, grade in self._roster.items() if grade == grade_number])

    def added(self) -> list[bool]:
        return self._success
