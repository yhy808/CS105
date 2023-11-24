#
# discretize_ages.py
#
# The program discretizes the numeric attribute and divides the range of possible 
# values into subranges that are often called bins to prepare a dataset for 
# data mining.
#
# Hongyi Yu


infilename = input('name of input file: ')
name_component = infilename.split('.')
outfilename = name_component[0] + '_disc.' + name_component[-1]
infile = open(infilename, 'r')
outfile = open(outfilename, 'w')

for line in infile:
    line = line[:-1]
    fields = line.split(',')
    age = int(fields[-1])
    if 0 <= age <= 12:
        fields[-1] = 'C'
    elif 13 <= age <= 19:
        fields[-1] = 'T'
    elif 20 <= age <= 35:
        fields[-1] = 'E'
    elif 36 <= age <= 60:
        fields[-1] = 'A'
    else:
        fields[-1] = 'S'
    transformed = ','.join(fields)
    print(transformed, file=outfile)

infile.close()
outfile.close()