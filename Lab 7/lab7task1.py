#
# lab7task1.py
#
# A simple front-end for our movie database in SQLite.
#
# This program only works if you put the movie database
# (movie.sqlite) in the same folder as the program.
#
# Computer Science 105
#

import sqlite3

# Connect to the database and create a cursor for it.
db = sqlite3.connect('movie.sqlite')
cursor = db.cursor()

pob = input('Which place of birth? ')
pob = '%' + pob + '%'

# Execute the query.
command = '''SELECT name, pob 
             FROM Person 
             WHERE pob LIKE ?;'''
cursor.execute(command, [pob])

# Print the results.
print()
count = 0
for row in cursor:
    print(row[0], 'was born in', row[1])
    count = count + 1
if count == 0:
    print('No one in the database was born there.')
    
db.commit()
db.close()
