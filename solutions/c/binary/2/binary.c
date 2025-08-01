#include "binary.h"

int convert(const char *input)
{
    int result = 0;

    while (*input)
    {
        int digit = *input++ - '0';
        
        if (digit & ~1)
            return INVALID;

        result = (result << 1) + digit;
    }

    return result;
}
