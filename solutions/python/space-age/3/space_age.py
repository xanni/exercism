from functools import partial

ORBITAL_PERIOD = {
    "mercury": 0.2408467,
    "venus": 0.61519726,
    "earth": 1.0,
    "mars": 1.8808158,
    "jupiter": 11.862615,
    "saturn": 29.447498,
    "uranus": 84.016846,
    "neptune": 164.79132,
}

SECONDS_PER_EARTH_YEAR = 31_557_600


class SpaceAge:
    _years: float

    def __init__(self, seconds: int) -> None:
        self._years = seconds / SECONDS_PER_EARTH_YEAR
        for planet, ratio in ORBITAL_PERIOD.items():
            setattr(self, "on_" + planet, partial(self._on_planet, ratio))

    def _on_planet(self, ratio: float) -> float:
        return round(self._years / ratio, 2)
