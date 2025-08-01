#define _DEFAULT_SOURCE

#include "raindrops.h"

#include <stdio.h>
#include <string.h>

#define MAXLEN 16

void convert(char result[], int drops)
{
    char *start = result;

    if (!(drops % 3))
        result = stpcpy(result, "Pling");

    if (!(drops % 5))
        result = stpcpy(result, "Plang");

    if (!(drops % 7))
        result = stpcpy(result, "Plong");

    if (result == start)
    {
        snprintf(result, MAXLEN, "%d", drops);
    }
}
