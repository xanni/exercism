from __future__ import annotations

from enum import Enum, auto


class Protein(Enum):
    STOP = auto()
    CYSTEINE = auto()
    LEUCINE = auto()
    METHIONINE = auto()
    PHENYLALANINE = auto()
    SERINE = auto()
    TRYPTOPHAN = auto()
    TYROSINE = auto()


CODONS = {
    "AUG": Protein.METHIONINE,
    **dict.fromkeys(("UUU", "UUC"), Protein.PHENYLALANINE),
    **dict.fromkeys(("UUA", "UUG"), Protein.LEUCINE),
    **dict.fromkeys(("UCU", "UCC", "UCA", "UCG"), Protein.SERINE),
    **dict.fromkeys(("UAU", "UAC"), Protein.TYROSINE),
    **dict.fromkeys(("UGU", "UGC"), Protein.CYSTEINE),
    "UGG": Protein.TRYPTOPHAN,
    **dict.fromkeys(("UAA", "UAG", "UGA"), Protein.STOP),
}


def proteins(strand: str) -> list[str]:
    p: list[str] = []
    for i in range(0, len(strand), 3):
        codon = strand[i : i + 3]
        if CODONS[codon] == Protein.STOP:
            break

        p.append(CODONS[codon].name.title())

    return p
