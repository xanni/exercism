from __future__ import annotations


class Clock:
    def __init__(self, hour: int, minute: int) -> None:
        carry, self.minute = divmod(minute, 60)
        self.hour = (hour + carry) % 24

    def __repr__(self) -> str:
        return f"{type(self).__name__}{(self.hour, self.minute)}"

    def __str__(self) -> str:
        return f"{self.hour:02}:{self.minute:02}"

    def __eq__(self, other: object) -> bool:
        return self.__dict__ == other.__dict__

    def __add__(self, minutes: int) -> Clock:
        return Clock(self.hour, self.minute + minutes)

    def __sub__(self, minutes: int) -> Clock:
        return Clock(self.hour, self.minute - minutes)
