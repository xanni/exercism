#include "dnd_character.h"

#include <stdlib.h>

#define DICE_COUNT 4
#define DICE_SIDES 6

int ability(void)
{
    int min = DICE_SIDES, total = 0;

    for (int i = 0; i < DICE_COUNT; i++)
    {
        int die = rand() % DICE_SIDES + 1;
        total += die;

        if (die < min)
            min = die;
    }

    return total - min;
}

dnd_character_t make_dnd_character(void)
{
    int con = ability();

    return (dnd_character_t){ability(), ability(), con, ability(), ability(), ability(), modifier(con) + 10};
}

int modifier(int score) { return (score - 10) >> 1; }
