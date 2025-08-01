from __future__ import annotations

from secrets import choice
from string import ascii_lowercase
from typing import Iterator

ALPHABET = ascii_lowercase
DEFAULT_KEY_LENGTH = 100
RANGE = len(ALPHABET)  # Number of valid characters
START = ord(ALPHABET[0])  # First valid character


class Cipher:
    def __init__(self, key: str | None = None) -> None:
        self.key = key or "".join(choice(ALPHABET) for _ in range(DEFAULT_KEY_LENGTH))

    def _offsets(self) -> Iterator[int]:
        """Infinitely iterates over the key"""
        i = 0
        while True:
            yield ord(self.key[i]) - START
            i = (i + 1) % len(self.key)

    def encode(self, text: str) -> str:
        offsets = self._offsets()
        return "".join(chr((ord(char) - START + next(offsets)) % RANGE + START) for char in text)

    def decode(self, text: str) -> str:
        offsets = self._offsets()
        return "".join(chr((ord(char) - START - next(offsets)) % RANGE + START) for char in text)
