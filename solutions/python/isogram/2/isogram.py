def is_isogram(string: str) -> bool:
    seen: set[str] = set()
    for char in string.lower():
        if not char.isalpha():
            continue
        if char in seen:
            return False
        seen.add(char)

    return True
