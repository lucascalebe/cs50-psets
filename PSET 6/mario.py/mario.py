from cs50 import get_int

height = get_int("Height: ")

# Get just numbers between 1 and 8
while height < 1 or height > 8:
    height = get_int("Height: ")

#Printing
for i in range(1,height + 1):
    print(" " * (height - i), end='')
    print("#" * (i))