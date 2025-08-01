DARTBOARD = ((1, 10), (5, 5), (10, 1))  # (Radius of zone, points scored)


def score(x: float, y: float) -> int:
    distance_squared = x * x + y * y
    for radius, points in DARTBOARD:
        if distance_squared <= radius * radius:
            return points

    return 0
