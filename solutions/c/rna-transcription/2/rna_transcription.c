#include "rna_transcription.h"

#include <stdlib.h>
#include <string.h>

char *to_rna(const char *dna)
{
    char *result = malloc(strlen(dna) + 1); // Flawfinder: ignore
    if (!result)
        exit(1);

    char *rna = result;

    for (; *dna; dna++, rna++)
    {
        switch (*dna)
        {
        case 'G':
            *rna = 'C';
            break;
        case 'C':
            *rna = 'G';
            break;
        case 'T':
            *rna = 'A';
            break;
        case 'A':
            *rna = 'U';
            break;
        default:
            free(result);
            return NULL;
        }
    }

    *rna = '\0';

    return result;
}
