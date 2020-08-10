#include <stdio.h>
#include <cs50.h>
#include <ctype.h>
#include <string.h>
#include <math.h>

//SHOWING THAT THERE ARE FUNCTIONS
int count_letters(string s);
int count_words(string s);
int count_sentences(string s);

int main(void)
{
    //GETTING TEXT
    string s = get_string("Text: ");

    float L = (float)count_letters(s) / (float)count_words(s) * 100;
    float S = (float)count_sentences(s) / (float)count_words(s) * 100;

    //COLEMAN-LIAU FORMULA
    int index = roundf(0.0588 * L - 0.296 * S - 15.8);

    //PRINTING OVER 16 AND LESS THAN 1
    if (index >= 16)
    {
        printf("Grade 16+\n");
    }
    else if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else
    {
        printf("Grade %i\n", index);
    }

}

//FUNCTIONS TO COUNT LETTERS

int count_letters(string s)
{
    int counter = 0;
    int n = strlen(s);
    for (int i = 0;  i < n; i++)
    {
        //FIRST I MAKE EVERYTHING CAPITOL
        s[i] = toupper(s[i]);
        if (isupper(s[i]))
        {
            counter++;
        }
    }
    return counter;
}

//FUNCTIONS TO COUNT WORDS

int count_words(string s)
{
    int counter = 0;
    int n = strlen(s);
    for (int i = 0; i < n; i++)
    {
        //FIRST I MAKE EVERYTHING CAPITOL
        s[i] = toupper(s[i]);
        if (isspace(s[i]))
        {
            counter++;
        }
    }
    return counter + 1;
}

//FUNCTION TO COUNT SENTENCES

int count_sentences(string s)
{
    int counter = 0;
    int n = strlen(s);
    for (int i = 0; i < n; i++)
    {
        if (s[i] == '.' || s[i] == '!' || s[i] == '?')
        {
            counter++;
        }
    }
    return counter;
}