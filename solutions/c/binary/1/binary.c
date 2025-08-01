#include "binary.h"

int convert(const char *input)
{
    int result = 0;

    while (*input)
    {
        if ((*input - '0') & ~1)
            return INVALID;

        result = (result << 1) + (*input++ & 1);
    }

    return result;
}
