#
# CS 105: Lab 3, Tasks 2 and 3
#

#
# For each problem, use a text editor to add the appropriate SQL
# command between the triple quotes provided for that problem's variable.
#
# For example, here is how you would include a query that finds the
# names of all CS courses:
#
sample = """
    SELECT name
    FROM Course
    WHERE name LIKE 'CS%';
"""

#
# Query 1. Put your SQL command between the triple quotes found below.
# Follow the same format as the model query shown above.
#
query1 = """
    SELECT name, dept_name
    FROM Student, MajorsIn
    WHERE id =  student_id;
"""

#
# Query 2. Put your SQL command between the triple quotes found below.
#
query2 = """
    SELECT name, dept_name
    FROM Student LEFT OUTER JOIN MajorsIn
    On id =  student_id;
"""

#
# Query 3. Put your SQL command between the triple quotes found below.
#
query3 = """
    SELECT name, dept_name
    FROM Student LEFT OUTER JOIN MajorsIn
    On id =  student_id
    WHERE name LIKE 'C%' OR name LIKE 'S%';
"""

#
# Query 4. Put your SQL command between the triple quotes found below.
#
query4 = """
    SELECT name, capacity
    FROM Room
    WHERE capacity = (SELECT MIN(capacity)
		     FROM Room);
"""

#
# Query 5. Put your SQL command between the triple quotes found below.
#
query5 = """
    SELECT dept_name, COUNT(*)
    FROM MajorsIn
    GROUP BY dept_name
    ORDER BY COUNT(*) DESC;           
"""

#
# Query 6. Put your SQL command between the triple quotes found below.
#
query6 = """
    SELECT dept_name, COUNT(dept_name)
    FROM MajorsIn  LEFT OUTER JOIN Student
    ON student_id = id
    GROUP BY dept_name
    ORDER BY COUNT(*) DESC;            
"""

#
# Query 7. Put your SQL command between the triple quotes found below.
# Follow the same format as the model query shown above.
#
query7 = """
    SELECT dept_name, COUNT(dept_name)
    FROM MajorsIn LEFT OUTER JOIN Student
    ON student_id = id
    GROUP BY dept_name
    HAVING COUNT(dept_name) < 2
    ORDER BY COUNT(*) DESC;
"""

#
# Query 8. Put your SQL command between the triple quotes found below.
#
query8 = """
    SELECT Room. name, Room. capacity
    FROM Room, Course
    WHERE Course. room_id = Room. id
	  AND Course. name = 'CS 105';
"""

#
# Query 9. Put your SQL command between the triple quotes found below.
#
query9 = """
    SELECT name
    FROM Department
    WHERE name LIKE '% %';
"""

#
# Query 10. Put your SQL command between the triple quotes found below.
#
query10 = """
    SELECT name, capacity
    FROM Room
    WHERE capacity BETWEEN 50 AND 250 OR  NOT(name LIKE 'C%');
"""

#
# Query 11. Put your SQL command between the triple quotes found below.
#
query11 = """
    SELECT Count(*)
    FROM MajorsIn
    WHERE dept_name = 'computer science';       
"""

#
# Query 12. Put your SQL command between the triple quotes found below.
#
query12 = """
    SELECT Student. name, Course. name, start_time, Room. name
    FROM Student, Enrolled, Course, Room
    WHERE Student. id = student_id
          AND course_name = Course. name
	 AND Room. id = room_id
	 AND credit_status = 'ugrad';            
"""

#
# Query 13. Put your SQL command between the triple quotes found below.
    SELECT name
    FROM Student, Enrolled
    WHERE id = student_id
          AND student_id != (SELECT student_id				 
      	                    FROM Student, Enrolled
			   WHERE id = student_id						  
                            AND course_name = 'CS 105');
"""
