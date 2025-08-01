#include "resistor_color.h"

static const resistor_band_t Colors[] = COLORS;

int color_code(resistor_band_t color) { return color; }

resistor_band_t *colors(void) { return (resistor_band_t *)Colors; }
