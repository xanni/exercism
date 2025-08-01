def flatten(iterable: list) -> list:
    result: list = []

    for element in iterable:
        if isinstance(element, list):
            result += flatten(element)
        elif element is not None:
            result += [element]

    return result
