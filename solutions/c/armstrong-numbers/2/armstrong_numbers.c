#include "armstrong_numbers.h"

bool is_armstrong_number(int candidate)
{
    int digits = 0;
    for (int n = candidate; n; n /= 10)
        digits++;

    if (digits < 3)
        return digits != 2;

    int sum = 0;
    for (int n = candidate; n; n /= 10)
    {
        int a = 1;
        for (int d = n % 10, i = digits; i; i--)
            a *= d;
        sum += a;
    }

    return candidate == sum;
}
