#include "resistor_color.h"

static const resistor_band_t Colors[] = COLORS;

resistor_band_t *colors(void) { return (resistor_band_t *)Colors; }
