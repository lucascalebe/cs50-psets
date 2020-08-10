#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int n;
    do 
    { 
        n = get_int("height: ");
    }
    //GET JUST NUMBERS BETWEEN 1 AND 8.
    while (n < 1 || n > 8);
    //LOOPINGS FOR PYRAMID. I LINES,J COLUMNS.  
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if (j < n - i - 1) 
            {
                printf(" ");
            }
            else
            {
                printf("#");
            }
        }
        //\n TO GO NEXTLINE.
        printf("\n");
    }
}
 
