#
# CS 105: Problem Set 2
#

#
# For each problem, use a text editor to add the appropriate SQL
# command between the triple quotes provided for that problem's variable.
#
# For example, here is how you would include a query that finds the
# names and years of all movies in the database with an R rating:
#
sample = """
    SELECT name, year
    FROM Movie
    WHERE rating = 'R';
"""

#
# Problem 1. Put your SQL command between the triple quotes found below.
# Follow the same format as the model query shown above.
#
problem1 = """
    SELECT *
    FROM Person
    WHERE name = 'Julianne Moore';
"""

#
# Problem 2. Put your SQL command between the triple quotes found below.
#
problem2 = """
    SELECT name, year
    FROM Movie
    WHERE rating = 'G' AND year >= 2016;
"""

#
# Problem 3. Put your SQL command between the triple quotes found below.
#
problem3 = """
    SELECT name, rating, runtime
    FROM Movie
    WHERE name = 'Good Will Hunting' OR name = 'Mystic River';
"""

#
# Problem 4. Put your SQL command between the triple quotes found below.
#
problem4 = """
    SELECT name, pob
    FROM Person
    WHERE pob LIKE '%China';
"""

#
# Problem 5. Put your SQL command between the triple quotes found below.
#
problem5 = """
    SELECT AVG (earnings_rank)
    FROM Movie
    WHERE rating = 'R' AND earnings_rank BETWEEN 1 AND 100;           
"""

#
# Problem 6. Put your SQL command between the triple quotes found below.
#
problem6 = """
    SELECT Count (*)
    FROM Person
    WHERE dob IS NULL AND pob IS NULL;            
"""

#
# Problem 7. Put your SQL command between the triple quotes found below.
#
problem7 = """
    SELECT name, year
    FROM Movie
    WHERE  rating = 'R'
      AND year = (SELECT MIN(year)
                  FROM Movie
                  WHERE rating = 'R');
"""

#
# Problem 8. Put your SQL command between the triple quotes found below.
#
problem8 = """
    SELECT year, COUNT(*)
    FROM Oscar
    GROUP BY year
    Having COUNT(*) != 6;            
"""
