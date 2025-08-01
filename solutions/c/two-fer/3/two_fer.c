#include "two_fer.h"

#include <assert.h>
#include <stdio.h>
#include <stdlib.h>

void two_fer(char *buffer, const char *name)
{
    int count = snprintf(buffer, MAXLEN, "One for %s, one for me.", (name ? name : "you"));
    assert(count >= 0 && count < MAXLEN);
}
