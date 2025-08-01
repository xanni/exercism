#include "isogram.h"

#include <ctype.h>

bool is_isogram(const char phrase[])
{
    if (!phrase)
        return false;

    int letters = 0;

    for (char c; (c = *phrase); phrase++)
        if (isalpha(c))
        {
            c = 1 << (toupper(c) - 'A');
            if (letters & c)
                return false;

            letters |= c;
        }

    return true;
}
