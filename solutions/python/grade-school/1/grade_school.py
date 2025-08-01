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
        return [s[0] for s in sorted(self._roster.items(), key=lambda e: (e[1], e[0]))]

    def grade(self, grade_number: int) -> list[str]:
        "Return sorted student names that are in the given grade_number"
        return sorted([s[0] for s in self._roster.items() if s[1] == grade_number])

    def added(self) -> list[bool]:
        return self._success
