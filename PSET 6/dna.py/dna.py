from sys import argv
from csv import reader, DictReader

#checking if the inputs are right,if the input is different of 3, something is wrong!
if len(argv) < 3:
    print("Usage: python dna.py data.csv sequence.txt")
    exit()

#read the dna sequence (txt)
with open(argv[2]) as dnafile:
    dnareader = reader(dnafile)
    for row in dnareader:
        dnalist = row

#
people, strs, dna = ( [], [], dnalist[0] )

#people = []
#strs = []
#dna = dnalist[0]

#read the dna sequence (.csv)
with open(argv[1]) as peoplefile:
    peoplereader = reader(peoplefile)
    for line in peoplereader:
        #check if the current row is the header and store the data since the position 1.(ignoring the name)
        if line[0] == 'name':
            # a[1:] starts the array since 1 position || a[:-5]
            strs = line[1:]
        else:
            #case the current row is a data row, append to people array
            people.append({ 'name' : line[0], 'values' : line[1:] })

# people = [
#   {
#       name : 'Alice', values : [1, 2, 3]
#   },
#   {
#       name : 'Jon', values : [1, 2, 3] people[1]['values'][2]
#   }
#]

# case it's
flag = False

# Iterate over people array, (run into the rows...)
for person in people:
    #Enumerate function returns a couple of data. 1 - Index 2 - content
    #run into the columns...
    #index = [position], str = content into index,like -> [AGATC]...
    for index, str in enumerate(strs):
        #  int(person['values'][index]) is the max of times that it must repeat. /// int(person['values'][index]) + 1 // after the quantity expected to be repeated...
        n, n2 = ( int(person['values'][index]), int(person['values'][index]) + 1 )

        # if there are the exactly amount expected...
        if (n * str) in dna and not (n2 * str) in dna:

            flag = True
        else:
            flag = False
            break
    # if you arrive here, the 3 flags was true!
    if flag:
        print(person['name'])
        break

# case anybody has matched
if not flag:
    print("No match")