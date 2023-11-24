#
# CS 105: Lab 2, Task 2
#

#
# Query 1. 
#
query1 = """
    SELECT *
    FROM Enrolled;
"""

#
# Query 2. 
#
query2 = """
    SELECT name, start_time
    FROM Course;
"""

#
# Query 3. Put your SQL command between the triple quotes found below.
# Follow the same format as the queries shown above.
#
query3 = """
    SELECT name
    FROM Department; 
"""

#
# Query 4. 
#
query4 = """
    SELECT *
    FROM MajorsIn
    WHERE dept_name = 'computer science';
"""

#
# Query 5. Put your SQL command between the triple quotes found below.
#
query5 = """
    SELECT name, capacity
    FROM Room
    WHERE id = '0005';          
"""

#
# Query 6. 
#
query6 = """
    SELECT name, capacity
    FROM Room
    WHERE capacity >= 100
      AND capacity <= 150;            
"""

#
# Query 7. Put your SQL command between the triple quotes found below.
#
query7 = """
    SELECT name, capacity
    FROM Room
    WHERE capacity BETWEEN 100 AND 150;
"""

#
# Query 8. Put your SQL command between the triple quotes found below.
#
query8 = """
    SELECT student_id
    FROM MajorsIn
    WHERE dept_name = 'mathematics' OR dept_name = 'computer science';
"""

#
# Query 9. 
#
query9 = """
    SELECT *
    FROM Course
    WHERE name LIKE 'CS 1%';
"""

#
# Query 10. Put your SQL command between the triple quotes found below.
#
query10 = """
    SELECT *
    FROM Course
    WHERE name LIKE 'CS 1__';
"""

#
# Query 11. Put your SQL command between the triple quotes found below.
#
query11 = """
    SELECT id, name
    FROM Room
    WHERE NOT ( name LIKE 'CAS%' );           
"""

#
# Query 12.
#
query12 = """
    SELECT name
    FROM Course
    WHERE room_id IS NULL;        
"""

#
# Query 13. 
#
query13 = """
    SELECT name
    FROM Course
    WHERE room_id = NULL;
"""

#
# Query 14. 
#
query14 = """
    SELECT COUNT(DISTINCT course_name)
    FROM Enrolled
    WHERE credit_status = 'ugrad';        
"""

#
# Query 15. 
#
query15 = """
    SELECT COUNT(course_name)
    FROM Enrolled
    WHERE credit_status = 'ugrad';        
"""

#
# Query 16. Put your SQL command between the triple quotes found below.
#
query16 = """
    SELECT MIN (id)
    FROM Room
    WHERE name LIKE 'CAS%';            
"""
