#include "hamming.h"

#include <string.h>

int compute(const char *lhs, const char *rhs)
{
    unsigned count = 0, length = strlen(lhs); // Flawfinder: ignore

    if (strlen(rhs) != length) // Flawfinder: ignore
        return ERROR;

    for (unsigned i = 0; i < length; i++)
        count += (lhs[i] != rhs[i]);

    return count;
}
