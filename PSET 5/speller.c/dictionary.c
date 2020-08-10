// Implements a dictionary's functionality

#include <stdbool.h>
#include <strings.h>
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <ctype.h>
#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH];
    struct node *next;
}
node;

// Number of buckets in hash table
const unsigned int N = 26;

// Hash table
node *table[N];

// total words
int numWords = 0;

// Returns true if word is in dictionary else false
bool check(const char *word)
{
    node *point = table[hash(word)];

    if (strcasecmp(point->word, word) == 0)
        return true;

    while (point->next != NULL)
    {
        point = point->next;
        if (strcasecmp(point->word, word) == 0)
            return true;
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // couting letters, like a = 0, b = 1, c = 2...
    //cast
    int i = (int) tolower(word[0]) - 97;
    return i;
}

// Loads dictionary into memory, returning true if successful else false
bool load(const char *dictionary)
{

    FILE *file = fopen(dictionary, "r");
    char *dictionaryWord = malloc(LENGTH);
    if (dictionaryWord == NULL)
        return false;

    while (fscanf(file, "%s", dictionaryWord) != EOF)
    {
        node *nod = malloc(sizeof(node));
        if (nod == NULL)
            return false;

        strcpy(nod->word,dictionaryWord);
        numWords++;

        // points to the beginning
        nod->next = table[hash(dictionaryWord)];

        table[hash(dictionaryWord)] = nod;
    }

    fclose(file);
    // clears memory (SUPER IMPORTANT)
    free(dictionaryWord);
    return true;
}

// Returns number of words in dictionary if loaded else 0 if not yet loaded
unsigned int size(void)
{
    return numWords;
}

// Unloads dictionary from memory, returning true if successful else false
bool unload(void)
{
    node *point;
    node *temporary;

    // N = numbers of buckets in hashtable
    for (int i = 0; i < N; i++)
    {
        if (table[i] == NULL)
            continue;

        // changing pointers without losing reference
        point = table[i];
        temporary = point;

        while (point->next != NULL)
        {
            point = point->next;
            free(temporary);
            temporary = point;
        }
        free(point);
    }
    return true;
}
