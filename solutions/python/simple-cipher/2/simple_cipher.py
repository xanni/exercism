from __future__ import annotations

from itertools import cycle
from secrets import choice
from string import ascii_lowercase

ALPHABET = ascii_lowercase
DEFAULT_KEY_LENGTH = 100
RANGE = len(ALPHABET)  # Number of valid characters
START = ord(ALPHABET[0])  # First valid character


class Cipher:
    def __init__(self, key: str | None = None) -> None:
        self.key = key or "".join(choice(ALPHABET) for _ in range(DEFAULT_KEY_LENGTH))

    def encode(self, text: str) -> str:
        shift_it = cycle(self.key)
        return "".join(
            chr((ord(char) + ord(next(shift_it)) - 2 * START) % RANGE + START) for char in text
        )

    def decode(self, text: str) -> str:
        shift_it = cycle(self.key)
        return "".join(chr((ord(char) - ord(next(shift_it))) % RANGE + START) for char in text)
