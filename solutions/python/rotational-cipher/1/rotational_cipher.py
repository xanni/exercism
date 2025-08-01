from string import ascii_lowercase, ascii_uppercase

INVALID_KEY_ERR = "Key must be in the range 0-26"
LETTERS = len(ascii_uppercase)


def rotate(text: str, key: int) -> str:
    if not 0 <= key <= LETTERS:
        raise ValueError(INVALID_KEY_ERR)

    mapping = {
        ord(letter): (ord(letter) - ord("A") + key) % LETTERS + ord("A")
        for letter in ascii_uppercase
    } | {
        ord(letter): (ord(letter) - ord("a") + key) % LETTERS + ord("a")
        for letter in ascii_lowercase
    }
    return text.translate(mapping)
