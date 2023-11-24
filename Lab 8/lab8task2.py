#
# lab8task1.py
#
# Processes a comma-delimited text file containing census data
#
# Computer Science 105
#

infile = open('census.csv', 'r')
state = input('Enter a state abbreviation: ')
year = input('Enter a year (1990 or 2007): ')
print()

count = 0
total = 0
for line in infile:
    line = line[:-1]     # chop off the newline character
    fields = line.split(',')
    if fields[1] == state and year == '1990':
        count += 1
        total += int(fields[3])
        print(fields[0], '-', fields[3])
    elif fields[1] == state and year == '2007':
        count += 1
        total += int(fields[4])
        print(fields[0], '-', fields[4])
print('The total population of', state, 'in', year, 'was', total)
    
if count == 0:
    print('There are no states in the file with that abbreviation.')
    
infile.close()

