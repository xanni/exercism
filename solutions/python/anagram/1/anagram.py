from __future__ import annotations


def find_anagrams(word: str, candidates: list[str]) -> list[str]:
    return list(
        filter(
            lambda candidate: candidate.lower() != word.lower()
            and sorted(candidate.lower()) == sorted(word.lower()),
            candidates,
        ),
    )
