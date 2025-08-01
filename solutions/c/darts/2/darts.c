#include "darts.h"

typedef struct
{
    uint8_t radius_squared, score;
} score_t;

// Array mapping the squares of the radiuses of the target regions to their respective scores
static const score_t SCORES[] = {{1, 10}, {5 * 5, 5}, {10 * 10, 1}};

uint8_t score(coordinate_t position)
{
    float distance_squared = position.x * position.x + position.y * position.y;

    for (uint8_t i = 0; i < sizeof(SCORES) / sizeof(SCORES[0]); i++)
    {
        score_t s = SCORES[i];
        if (distance_squared <= s.radius_squared)
            return s.score;
    }

    return 0;
}
