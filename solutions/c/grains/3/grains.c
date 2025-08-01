#include "grains.h"
#include <limits.h>

uint64_t square(uint8_t index)
{
    return index < 1 || index > 64 ? 0 : 1ull << --index;
}

uint64_t total(void) { return UINT64_MAX; }
