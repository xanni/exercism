ERR_LENGTH = "Strands must be of equal length."


def distance(strand_a: str, strand_b: str) -> int:
    if len(strand_a) != len(strand_b):
        raise ValueError(ERR_LENGTH)

    return sum(a != b for a, b in zip(strand_a, strand_b))
