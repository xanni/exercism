from __future__ import annotations


def find_anagrams(word: str, candidates: list[str]) -> list[str]:
    return [
        anagram
        for anagram in candidates
        if anagram.casefold() != word.casefold()
        and sorted(anagram.casefold()) == sorted(word.casefold())
    ]
