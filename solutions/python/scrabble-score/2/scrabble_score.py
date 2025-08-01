from enum import IntEnum


class Scores(IntEnum):
    A = E = I = O = U = L = N = R = S = T = 1  # noqa: E741
    D = G = 2
    B = C = M = P = 3
    F = H = V = W = Y = 4
    K = 5
    J = X = 8
    Q = Z = 10


def score(word: str) -> int:
    return sum(Scores[letter] for letter in word.upper())
