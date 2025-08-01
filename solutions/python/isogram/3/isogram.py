def is_isogram(string: str) -> bool:
    text = tuple(filter(str.isalpha, string.lower()))
    return len(text) == len(set(text))
