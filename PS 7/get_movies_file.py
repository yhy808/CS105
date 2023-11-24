#
# get_movies_screen.py
#
# a program that finds movies with a specified rating that have an earnings rank 
# that is less than or equal to a specified cutoff value.


import sqlite3
filename = input('Enter the name of the database file: ')
db = sqlite3.connect(filename)
cursor = db.cursor()

rating = input('Enter the rating: ')
cutoff_value = input('Enter the earnings-rank cutoff: ')

result_filename = input('Enter the name of the results file: ')
outfile = open(result_filename, 'w')

command = '''SELECT earnings_rank, name, year
             FROM Movie
             WHERE rating = ? AND earnings_rank <= ?
             ORDER BY earnings_rank;'''
cursor.execute(command, [rating, cutoff_value])

count = 0
for row in cursor:
    print(str(row[0]) + ',' + row[1] + ',' + str(row[2]), file = outfile)
    count += 1
    
if count == 0:
    print('There are no movies in the database that match your criteria.')
else:
    print('Wrote', count, 'lines of results to the file.')

outfile.close()
db.commit()
db.close()

