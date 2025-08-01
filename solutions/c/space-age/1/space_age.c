#include "space_age.h"

#define SECONDS_PER_EARTH_YEAR (60 * 60 * 24 * 365.25)

const float ORBITAL_PERIOD[] = {
    0.2408467,  // Mercury
    0.61519726, // Venus
    1.0,        // Earth
    1.8808158,  // Mars
    11.862615,  // Jupiter
    29.447498,  // Saturn
    84.016846,  // Uranus
    164.79132,  // Neptune
};

float age(planet_t planet, int64_t seconds)
{
    if (planet < MERCURY || planet > NEPTUNE)
        return ERROR;

    return seconds / SECONDS_PER_EARTH_YEAR / ORBITAL_PERIOD[planet];
}
