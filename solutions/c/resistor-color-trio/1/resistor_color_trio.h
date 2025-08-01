#ifndef RESISTOR_COLOR_TRIO_H
#define RESISTOR_COLOR_TRIO_H

#include <stdint.h>

typedef enum Color
{
    BLACK,
    BROWN,
    RED,
    ORANGE,
    YELLOW,
    GREEN,
    BLUE,
    VIOLET,
    GREY,
    WHITE
} resistor_band_t;

enum Prefix
{
    OHMS,
    KILOOHMS,
    MEGAOHMS,
    GIGAOHMS
};

typedef struct
{
    uint16_t value; // cppcheck-suppress unusedStructMember
    enum Prefix unit;
} resistor_value_t;

resistor_value_t color_code(resistor_band_t *);

#endif
