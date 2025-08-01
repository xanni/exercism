def is_isogram(string: str) -> bool:
    letters = string.replace(" ", "").replace("-", "").lower()
    return len(letters) == len(set(letters))
