from string import ascii_letters, ascii_lowercase


def rotate(text: str, key: int) -> str:
    cipher = ascii_lowercase[key:] + ascii_lowercase[:key]
    return text.translate(str.maketrans(ascii_letters, cipher + cipher.upper()))
