#include "armstrong_numbers.h"

#include <math.h>

bool is_armstrong_number(int candidate)
{
    int digits = (int)log10(candidate) + 1, sum = 0;

    for (int n = candidate; n; n /= 10)
        sum += pow(n % 10, digits);

    return candidate == sum;
}
