from itertools import zip_longest

FILLER = "_"


def transpose(text: str) -> str:
    transposed = zip_longest(*text.splitlines(), fillvalue=FILLER)

    return "\n".join("".join(row).rstrip(FILLER) for row in transposed).replace(FILLER, " ")
