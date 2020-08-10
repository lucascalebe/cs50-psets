from cs50 import SQL
import csv
from sys import argv

#check if the command line arguments is right!
if len(argv) != 2:
    print("Usage error, import.py characters.csv")
    exit()

#Connect to database
db = SQL("sqlite:///students.db")

#Oppening csv file through the command line
with open(argv[1],"r") as filecsv:
    #Putting csv file into a Dictionary
    reader = csv.DictReader(filecsv)

    # Iterate over CSV file
    for row in reader:

        #Splitting the name
        name = row["name"].split()

        #Putting students' data into a table
        if len(name) == 3:
            db.execute("INSERT INTO students (first, middle, last, house, birth) VALUES (?, ?, ?, ?, ?)",name[0], name[1], name[2], row["house"], row["birth"])
        else:
            db.execute("INSERT INTO students (first,middle,last,house,birth) VALUES (?,?,?,?,?)", name[0], None, name[1], row["house"], row["birth"])