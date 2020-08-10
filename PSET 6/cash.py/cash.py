from cs50 import get_float

dollars = get_float("Change owed: ")

# get just positive numbers
while dollars <= 0:
    dollars = get_float("Change owed: ")

count = 0;
#converting dollar to cents
cents = round(dollars * 100)

while cents > 0:
    if cents >= 25:
        cents -= 25
        count += 1

    elif cents >= 10:
        cents -= 10
        count += 1

    elif cents >= 5:
        cents -= 5
        count += 1

    else:
        cents -= 1
        count += 1

print(count)
