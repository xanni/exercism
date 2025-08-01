#include "hamming.h"

int compute(const char *lhs, const char *rhs)
{
    if (!lhs || !rhs)
        return ERROR;

    int count = 0;

    while (*lhs && *rhs)
    {
        count += (*lhs++ != *rhs++);
    }

    return (*lhs || *rhs) ? ERROR : count;
}
