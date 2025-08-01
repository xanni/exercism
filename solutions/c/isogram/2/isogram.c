#include "isogram.h"

#include <ctype.h>

bool is_isogram(const char phrase[])
{
    if (!phrase)
        return false;

    for (int letters = 0; *phrase; phrase++)
        if (isalpha(*phrase))
        {
            int match = 1 << (toupper(*phrase) - 'A');
            if (letters & match)
                return false;

            letters |= match;
        }

    return true;
}
