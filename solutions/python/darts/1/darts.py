import math

DARTBOARD = ((1, 10), (5, 5), (10, 1))  # (Radius of zone, points scored)


def score(x: float, y: float) -> int:
    distance = math.hypot(x, y)
    for radius, points in DARTBOARD:
        if distance <= radius:
            return points

    return 0
