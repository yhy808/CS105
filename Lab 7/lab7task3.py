#
# lab7task3.py


import sqlite3

db = sqlite3.connect('movie.sqlite')
cursor = db.cursor()

rating = input('Enter a rating: ')
year = input('Enter a year: ')
filename = input('Enter the name of the results file: ')
f = open(filename, 'w')

command = ('''SELECT name, runtime
              FROM Movie
              WHERE rating = ? and year = ?;''')
cursor.execute(command, [rating, year])

print()
count = 0
for row in cursor:
    print(row[0], '(' + str(row[1]), 'minutes)', file=f)
    count = count + 1
if count == 0:
    print('There are no movies with that rating in that year.', file=f)
print('There are', count, rating, 'movies from', year, 'in the database.')
print('The results are in', filename)

f.close()

db.commit()
db.close() 