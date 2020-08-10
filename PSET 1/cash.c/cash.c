#include <cs50.h>
#include <stdio.h>
#include <math.h>

int main(void)
{
    float dollars;
    //DO WHILE FOR GET JUST POSITIVE NUMBERS
    do
    {
        dollars = get_float("Change: ");
    }
    while (dollars < 0);
    //CONVERTING DOLLAR TO CENTS
    int cents = round(dollars * 100);
    //VARIABLE TO COUNT HOW MANY COINS WERE USED.
    int count_coins = 0;
    //WHILE WE CAN USE 25,USE 25.
    while (cents >= 25)
    {
        cents -= 25;
        count_coins++;
    } 
    while (cents >= 10)
    {
        cents -= 10;
        count_coins++;
    }
    while (cents >= 5)
    {
        cents -= 5;
        count_coins++;
    }
    while (cents >= 1)
    {
        cents -= 1;
        count_coins++;
    }

    printf("%i\n", count_coins);
}
