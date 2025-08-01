#include "collatz_conjecture.h"

int steps(int start)
{
    if (start < 1)
        return ERROR_VALUE;

    int steps;
    for (steps = 0; start != 1; steps++)
    {
        start = start % 2 ? 3 * start + 1 : start / 2;
    }

    return steps;
}
