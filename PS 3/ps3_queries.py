#
# CS 105: Problem Set 3
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
    SELECT Movie.name
    FROM Person, Actor, Movie
    WHERE Person.id = Actor.actor_id
      AND Movie.id =  Actor.movie_id
      AND Person.name = 'Jason Alexander';
"""

#
# Problem 2. Put your SQL command between the triple quotes found below.
#
problem2 = """
    SELECT AVG(earnings_rank)
    FROM Movie
    WHERE name LIKE '%Avengers%';
"""

#
# Problem 3. Put your SQL command between the triple quotes found below.
#
problem3 = """
    SELECT COUNT(DISTINCT name)
    FROM Person, Oscar
    WHERE id = person_id
      AND pob LIKE 'New York%';
"""

#
# Problem 4. Put your SQL command between the triple quotes found below.
#
problem4 = """
    SELECT name, COUNT(movie_id)
    FROM Person, Actor
    WHERE id = actor_id
    GROUP BY name
    HAVING COUNT(movie_id) >= 10;
"""

#
# Problem 5. Put your SQL command between the triple quotes found below.
#
problem5 = """
    SELECT COUNT(id)
    FROM Movie
    WHERE (year = 2020 OR year = 2021)
      AND earnings_rank BETWEEN 1 and 200;
"""

#
# Problem 6. Put your SQL command between the triple quotes found below.
#
problem6 = """
    SELECT name
    FROM  Person
    WHERE pob LIKE 'Boston, Mass%'
      AND id NOT IN (SELECT actor_id
		    FROM Actor);
"""

#
# Problem 7. Put your SQL command between the triple quotes found below.
#
problem7 = """
    SELECT name, COUNT(type)
    FROM Person LEFT OUTER JOIN Oscar
    ON id = person_id
    WHERE pob LIKE '%, Virginia, USA'
    GROUP BY name;
"""

#
# Problem 8. Put your SQL command between the triple quotes found below.
#
problem8 = """
    UPDATE Movie
    SET earnings_rank = 356
    WHERE name LIKE 'Captain America%' AND year = 2011;
"""
