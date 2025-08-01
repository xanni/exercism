#include "eliuds_eggs.h"

unsigned egg_count(unsigned eggs)
{
    unsigned count = 0;

    for (; eggs; eggs &= (eggs - 1))
        count++;

    return count;
}
