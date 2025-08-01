#include "space_age.h"

#define EARTH_SECONDS(period) (period * 60 * 60 * 24 * 365.25)

const float ORBITAL_PERIOD[] = {
    EARTH_SECONDS(0.2408467),  // Mercury
    EARTH_SECONDS(0.61519726), // Venus
    EARTH_SECONDS(1.0),        // Earth
    EARTH_SECONDS(1.8808158),  // Mars
    EARTH_SECONDS(11.862615),  // Jupiter
    EARTH_SECONDS(29.447498),  // Saturn
    EARTH_SECONDS(84.016846),  // Uranus
    EARTH_SECONDS(164.79132),  // Neptune
};

float age(planet_t planet, int64_t seconds)
{
    if (planet < MERCURY || planet > NEPTUNE)
        return ERROR;

    return seconds / ORBITAL_PERIOD[planet];
}
