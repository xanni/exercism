#include "pangram.h"

#include <ctype.h>

#define ALL_LETTERS ((1 << 26) - 1)

bool is_pangram(const char *sentence)
{
    int letters = 0;

    if (sentence)
        for (char c; (c = *sentence); sentence++)
            if (isalpha(c))
                letters |= 1 << (toupper(c) - 'A');

    return letters == ALL_LETTERS;
}
