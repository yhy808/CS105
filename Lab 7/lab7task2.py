#
# lab7task2.py
#
# serves as a front-end for our movie database

import sqlite3

db = sqlite3.connect('movie.sqlite')
cursor = db.cursor()

rating = input('Enter a rating: ')
year = input('Enter a year: ')

command = ('''SELECT name, runtime
              FROM Movie
              WHERE rating = ? and year = ?;''')
cursor.execute(command, [rating, year])

print()
count = 0
for row in cursor:
    print(row[0], '(' + str(row[1]), 'minutes)')
    count = count + 1
if count == 0:
    print('There are no movies with that rating in that year.')

db.commit()
db.close()             
        
