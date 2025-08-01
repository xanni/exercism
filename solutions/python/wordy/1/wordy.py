import operator

OP_ERR = "unknown operation"
SYNTAX_ERR = "syntax error"

OPS = {
    "plus": operator.add,
    "minus": operator.sub,
    "multiplied": operator.mul,
    "divided": operator.floordiv,
}


def _is_int(s: str) -> bool:
    negative = s[0] == "-"
    return s[negative:].isdigit()


def answer(question: str) -> int:
    words = question[:-1].split()[2:]  # Omit "What is" at start and "?" at end

    if not words or not _is_int(words[0]):  # First operand is required
        raise ValueError(SYNTAX_ERR)

    result = int(words.pop(0))

    while words:
        op = words.pop(0)
        if op in ["multiplied", "divided"]:
            if words.pop(0) != "by":
                raise ValueError(SYNTAX_ERR)
        elif op not in ["plus", "minus"]:
            if _is_int(op):  # Missing operator
                raise ValueError(SYNTAX_ERR)
            raise ValueError(OP_ERR)

        if not words or not _is_int(words[0]):
            raise ValueError(SYNTAX_ERR)

        result = OPS[op](result, int(words.pop(0)))

    return result
