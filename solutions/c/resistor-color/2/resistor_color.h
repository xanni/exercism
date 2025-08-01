#ifndef RESISTOR_COLOR_H
#define RESISTOR_COLOR_H

#include <stdint.h>

#define COLORS BLACK, BROWN, RED, ORANGE, YELLOW, GREEN, BLUE, VIOLET, GREY, WHITE

typedef enum
{
    COLORS
} resistor_band_t;

#define color_code(color) color

resistor_band_t *colors(void);

#endif
