#
# lab8task3.py
#
# Processes a comma-delimited text file containing census data
#
# Computer Science 105
#

infilename = input('Enter the name of the input file: ')
infile = open(infilename, 'r')
outfilename = input('Enter the name of the output file: ')
outfile = open(outfilename, 'w')

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
        print(fields[1] + ',' + fields[3], file = outfile)
    elif fields[1] == state and year == '2007':
        count += 1
        total += int(fields[4])
        print(fields[1] + ',' + fields[4], file = outfile)
print('The total population of', state, 'in', year, 'was', total)
print('The average population of its counties was', round(total/count, 1))
print('The per-county results are in', outfilename)
    
if count == 0:
    print('There are no states in the file with that abbreviation.')
    
infile.close()

