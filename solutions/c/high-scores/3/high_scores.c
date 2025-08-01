#include "high_scores.h"

#include <stdlib.h>
#include <string.h>

/// Return the latest score.
int32_t latest(const int32_t *scores, size_t scores_len) { return scores[scores_len - 1]; }

/// Return the highest score.
int32_t personal_best(const int32_t *scores, size_t scores_len)
{
    int32_t best = 0, score = 0;

    while (scores_len)
        score = scores[--scores_len], best = score > best ? score : best;

    return best;
}

static int compare(const void *a, const void *b)
{
    return (*(const int32_t *)b - *(const int32_t *)a);
}

/// Write the highest scores to `output` (in non-ascending order).
/// Return the number of scores written.
size_t personal_top_three(const int32_t *scores, size_t scores_len,
                          int32_t *output)
{
    int32_t sorted[scores_len];

    memcpy(sorted, scores, scores_len * sizeof(sorted[0])); // Flawfinder: ignore
    qsort(sorted, scores_len, sizeof(sorted[0]), compare);

    if (scores_len > 3)
        scores_len = 3;

    memcpy(output, sorted, scores_len * sizeof(sorted[0])); // Flawfinder: ignore

    return scores_len;
}
