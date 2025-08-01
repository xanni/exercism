def equilateral(sides: tuple) -> bool:
    a, b, c = sides
    return a > 0 and a == b == c


def triangle(sides: tuple) -> bool:
    return all(sides) and sum(sides) > 2 * max(sides)


def isosceles(sides: tuple) -> bool:
    a, b, c = sides
    return triangle(sides) and (a in (b, c) or b == c)


def scalene(sides: tuple) -> bool:
    a, b, c = sides
    return triangle(sides) and a not in (b, c) and b != c
