#
# classify_location&Tuition.py
#
# a program that classifies the locations of the universities into north, south, 
# west and east; and also discretizes the tuition into ranges

infile = open('National-Universities-Rankings.txt', 'r')
outfile = open('National-Universities-Rankings_Classified.txt', 'w')

header = infile.readline()
for line in infile:
    line = line[:-1]
    fields = line.split(',')
    state = fields[0][-2:]
    if state == 'MT' or state == 'WY' or state == 'ND' or state == 'SD' or state == 'NE' or state == 'MN' or state == 'IA' or state == 'WI' or state == 'IL' or state == 'MI' or state == 'IN' or state == 'WV' or state =='PA' or state == 'AK' or state == 'OH':
        fields[0] = 'North'
    elif state == 'NM' or state == 'TX' or state == 'LA' or state == 'MS' or state == 'AL' or state == 'FL' or state == 'GA' or state == 'SC' or state == 'NC' or state == 'VA' or state == 'TN' or state == 'MO' or state == 'KS' or state == 'KY' or state == 'CO' or state == 'OK' or state == 'AR':
        fields[0] = 'South'
    elif state == 'ME' or state == 'VT' or state == 'NH' or state == 'MA' or state == 'CT' or state == 'NJ' or state == 'DE' or state == 'MD' or state == 'NY' or state == 'RI' or state == 'DC':
        fields[0] = 'East'
    elif state == 'WA' or state == 'OR' or state == 'CA' or state == 'AZ' or state == 'ID' or state == 'NV' or state == 'UT' or state == 'HI':
        fields[0] = 'West'  
    tuition = int(fields[-1])
    if tuition <= 25000:
        fields[-1] = '25000_and_lower'
    elif tuition > 25000 and tuition <= 35000:
        fields[-1] = '25000_to_35000'
    elif tuition > 35000 and tuition <= 45000:
        fields[-1] = '35000_to_45000'
    elif tuition >= 45000:
        fields[-1] = '45000_and_up'
    print(fields[0], fields[1], fields[2], fields[3], fields[4], fields[5], file = outfile)
    
infile.close()
outfile.close()