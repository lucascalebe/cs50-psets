#include <stdio.h>
#include <cs50.h>
#include <ctype.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, string argv[])
{
    int key = 0;
    //CHECKING TO SEE IF ARGC ISN'T 2 TO PRINT THE MENSAGE.
    if (argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
    else if (argc == 2)
    {
        int length = strlen(argv[1]);
        //CHECKING EACH CHARACTER
        for (int i = 0; i < length; i++)
        {
            if (isdigit(argv[1][i]) == false)
            {
                printf("Usage: ./caesar key\n");
                return 1;
            }
            else
            {
                //ATOI IS A FUNCTION TO CONVERT A STRING TO INT
                key = atoi(argv[1]);
            }
        }

    }
    // CHECKING IF THE NUMBER IS NEGATIVE
    if (key < 0)
    {
        printf("key must be positive\n");
        return 1;
    }

    string text = get_string("plaintext:  ");

    int textLength = strlen(text);

    printf("ciphertext: ");
    for (int i = 0; i < textLength; i++)
    {
        //IF TO PRINT CASE BE LOWER
        if (islower(text[i]))
        {
            printf("%c", (text[i] - 'a' + key) % 26 + 'a');
        }
        //IF TO PRINT CASE BE UPPER
        else if (isupper(text[i]))
        {
            printf("%c", (text[i] - 'A' + key) % 26 + 'A');

        }

        else
        {
            printf("%c", text[i]);
        }
    }
    printf("\n");
}