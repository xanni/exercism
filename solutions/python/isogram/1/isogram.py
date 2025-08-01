from string import ascii_lowercase


def is_isogram(string: str) -> bool:
    seen: set[str] = set()
    for char in string.lower():
        if char not in ascii_lowercase:
            continue
        if char in seen:
            return False
        seen.add(char)

    return True
