#include "pangram.h"

#include <stdint.h>

#define ALL_LETTERS ((1 << 26) - 1)
#define CASE_BIT 0x20

bool is_pangram(const char *sentence)
{
    uint32_t letters = ALL_LETTERS;

    if (sentence)
        while (*sentence)
        {
            char c = *sentence++ & ~CASE_BIT;

            if (c >= 'A' && c <= 'Z')
                letters &= ~(1 << (c - 'A'));
        }

    return !letters;
}
