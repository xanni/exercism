#include "resistor_color_trio.h"

resistor_value_t color_code(resistor_band_t *bands)
{
    uint16_t value = bands[0] * (bands[1] ? 10 : 1) + bands[1];
    int exponent = bands[2] + !bands[1];

    if (exponent % 3)
        value *= exponent % 3 == 1 ? 10 : 100;

    return (resistor_value_t){value, (enum Prefix)exponent / 3};
}
