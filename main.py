import sqlite_lib

sqlite_lib.connect('hw17.db')

answer: list[tuple] = sqlite_lib.run_query_select('''
        SELECT c.course_id, c.course_name, l.*
	        FROM courses c
	        INNER JOIN lecturers l
		        ON c.lecturer_id  = l.lecturer_id;
    ''')
print(f"All courses and it's lecturer: {answer}")


answer: list[tuple] = sqlite_lib.run_query_select('''
        SELECT c.course_id, c.course_name
	        FROM courses c
	        LEFT JOIN lecturers l
		        ON c.lecturer_id = l.lecturer_id
	        WHERE c.lecturer_id IS NULL
    ''')
print(f"All courses that has no lecturer: {answer}")


answer: list[tuple] = sqlite_lib.run_query_select('''
        SELECT *
	        FROM courses c
	        LEFT JOIN lecturers l
		        ON c.lecturer_id = l.lecturer_id;

    ''')
print(f"All courses with their lecturer + NULL: {answer}")


answer: list[tuple] = sqlite_lib.run_query_select('''
        SELECT l.first_name, l.last_name, c.course_name
	        FROM courses c
	        INNER JOIN lecturers l
		        ON c.lecturer_id  = l.lecturer_id;
    ''')
print(f"All lecturer and it's courses (no NULL): {answer}")


answer: list[tuple] = sqlite_lib.run_query_select('''
        SELECT l.first_name, l.last_name
	        FROM lecturers l
	        LEFT JOIN courses c
		        ON c.lecturer_id = l.lecturer_id
	        WHERE c.lecturer_id IS NULL
    ''')
print(f"All lecturers that are not assigned to any course: {answer}")



answer: list[tuple] = sqlite_lib.run_query_select('''
        SELECT l.first_name, l.last_name, c.course_name
	        FROM courses c
	        RIGHT JOIN lecturers l
		        ON c.lecturer_id  = l.lecturer_id;
    ''')
print(f"All lecturers and their assigned course, no course = NULL on the course name: {answer}")



answer: list[tuple] = sqlite_lib.run_query_select('''
        SELECT c.course_id, c.course_name, l.first_name, l.last_name, l.email
	        FROM courses c
	        FULL OUTER JOIN lecturers l
	    	    ON c.lecturer_id = l.lecturer_id;
    ''')
print(f"All lecturers and their assigned course, no course to the lecturer = NULL, "
      f"All courses with no lecturer: {answer}")



answer: list[tuple] = sqlite_lib.run_query_select('''
        SELECT l.lecturer_id, l.first_name, l.last_name, c.course_id, c.course_name
            FROM lecturers l
            CROSS JOIN courses c;
    ''')
print(f"All possible outcomes: {answer}")
