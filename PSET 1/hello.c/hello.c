#include <cs50.h>
#include <stdio.h>

int main(void)
{
    //GETTING NAME WITH FUNCTION. 
    string name = get_string("What is your name:\n");
    //PRINTING NAME.
    printf("hello, %s\n", name);
}
