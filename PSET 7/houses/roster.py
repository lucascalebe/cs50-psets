from cs50 import SQL
from sys import argv

#check if the command line arguments is right!
if len(argv) != 2:
    print("Usage error, import.py characters.csv")
    exit()

#Connect to database
db = SQL("sqlite:///students.db")

#Execute a query in SQL
students = db.execute("SELECT first,middle,last,birth FROM students WHERE house = (?) ORDER BY last,first",argv[1])

#Printing, case the student has a middle name, prints just the first and last name
for student in students:
    if (student["middle"] == None):
        print(f"{student['first']} {student['last']}, born {student['birth']}")
    else:
         print(f"{student['first']}  {student['middle']} {student['last']}, born {student['birth']}")

