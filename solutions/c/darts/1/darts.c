#include "darts.h"

static const uint8_t scores[] = {10, 5, 1}, sizes_squared[] = {1, 5 * 5, 10 * 10};

uint8_t score(coordinate_t position)
{
    float distance_squared = position.x * position.x + position.y * position.y;

    for (uint8_t i = 0; i < sizeof(scores) / sizeof(scores[0]); i++)
    {
        if (distance_squared <= sizes_squared[i])
            return scores[i];
    }

    return 0;
}
