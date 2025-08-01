#include "perfect_numbers.h"

#include <stdint.h>

kind classify_number(int number)
{
    if (number < 1)
        return ERROR;

    if (number == 1)
        return DEFICIENT_NUMBER;

    int aliquot_sum = 1;

    for (int i = 2; i * i < number; i++)
        aliquot_sum += (number % i) ? 0 : i + number / i;

    return number < aliquot_sum ? ABUNDANT_NUMBER : number > aliquot_sum ? DEFICIENT_NUMBER
                                                                         : PERFECT_NUMBER;
}
