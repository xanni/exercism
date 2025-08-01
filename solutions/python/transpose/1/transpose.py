FILLER = "_"


def transpose(text: str) -> str:
    if not text:
        return ""

    rows = text.splitlines()
    height = len(rows)
    width = max(len(s) for s in rows)

    return "\n".join(
        "".join(rows[j].ljust(width, FILLER)[i] for j in range(height))
        .rstrip(FILLER)
        .replace(FILLER, " ")
        for i in range(width)
    )
