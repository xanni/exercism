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
    "UUU": Protein.PHENYLALANINE,
    "UUC": Protein.PHENYLALANINE,
    "UUA": Protein.LEUCINE,
    "UUG": Protein.LEUCINE,
    "UCU": Protein.SERINE,
    "UCC": Protein.SERINE,
    "UCA": Protein.SERINE,
    "UCG": Protein.SERINE,
    "UAU": Protein.TYROSINE,
    "UAC": Protein.TYROSINE,
    "UGU": Protein.CYSTEINE,
    "UGC": Protein.CYSTEINE,
    "UGG": Protein.TRYPTOPHAN,
    "UAA": Protein.STOP,
    "UAG": Protein.STOP,
    "UGA": Protein.STOP,
}


def proteins(strand: str) -> list[str]:
    p: list[str] = []
    for i in range(0, len(strand), 3):
        codon = strand[i : i + 3]
        if CODONS[codon] == Protein.STOP:
            break

        p.append(CODONS[codon].name.title())

    return p
