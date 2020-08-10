#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int n;
    //GETTING JUST NUMBERS BETWEEN 1 AND 8.
    do
    {
        n = get_int("Height: ");
    }
    while (n < 1 || n > 8);
    // FOR TO RUN LINES
    for (int i = 0; i < n; i++)
    {
        //FOR TO RUN COLUMNS
        for (int j = 0; j < n + i + 3; j++)
        {
            if (j < n - i - 1 || j == n || j == n + 1) 
            {
                //PRINTING SPACE
                printf(" ");
            }
            else
            {
                //PRINTING HASHES
                printf("#");
            }
        }
        //\n TO GO NEXTLINE.
        printf("\n");
    }
}
