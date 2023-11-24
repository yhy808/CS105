#
# lab8task1.py
#
# Processes a comma-delimited text file containing census data
#
# Computer Science 105
#

infile = open('census.csv', 'r')
state = input('Enter a state abbreviation: ')

count = 0
for line in infile:
    line = line[:-1]     # chop off the newline character
    fields = line.split(',')
    if fields[1] == state:
        count += 1
        print(fields[0], '- from', fields[3], 'to', fields[4])
    
if count == 0:
    print('There are no states in the file with that abbreviation.')
    
infile.close()

