#
# Lab 9, Task 3
#
# Transforming a data file
#
# Reads in a CSV file and transforms it to deal with missing data.
#
# In order for the program to work, the file cpw.csv must be in the
# same folder as the program.
#

infile = open('cpw.csv', 'r')
outfile = open('cpw_transformed.csv', 'w')

# YOUR CODE HERE: Read in the header from the input file
# and write it to the output file.
header = infile.readline()

for line in infile:
    line = line[:-1]   # removes the newline at the end of the line
    
    # YOUR CODE HERE: Split up the line into a list of fields.
    fields = line.split(',')
    # YOUR CODE HERE: Handle the four cases.
    if fields[1] == '' and fields[2] == '':
        line = infile.readline()
    elif fields[1] == '':
        print(fields[0] + ',' + str(fields[2]) + ',' + str(fields[2]), file = outfile)
    elif fields[2] == '':
        print(fields[0] + ',' + str(fields[1]) + ',' + str(fields[1]), file = outfile)
    else:
        print(fields[0] + ',' + str(fields[1]) + ',' + str(fields[2]), file = outfile)

infile.close()
outfile.close()
