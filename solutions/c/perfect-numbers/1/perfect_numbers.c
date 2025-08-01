#include "perfect_numbers.h"

#include <stdint.h>

// Integer square root
static uint16_t int_sqrt(uint32_t n)
{
    uint32_t rem = 0, root = 0;

    for (int i = 16; i > 0; i--)
    {
        root <<= 1;
        rem = (rem << 2) | (n >> 30);
        n <<= 2;
        if (root < rem)
        {
            rem -= root | 1;
            root += 2;
        }
    }
    return root >> 1;
}

kind classify_number(int number)
{
    if (number < 1)
        return ERROR;

    if (number == 1)
        return DEFICIENT_NUMBER;

    int aliquot_sum = 1;
    int root = int_sqrt(number);

    for (int i = 2; i <= root; i++)
    {
        if (number % i)
            continue;

        int factor = number / i;
        aliquot_sum += i + (factor == i ? 0 : factor);
    }

    return number < aliquot_sum ? ABUNDANT_NUMBER : number > aliquot_sum ? DEFICIENT_NUMBER
                                                                         : PERFECT_NUMBER;
}
