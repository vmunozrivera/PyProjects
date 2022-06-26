# Student DB
#

import sqlite3

db_connection = sqlite3.connect('classroom.db')
db_cursor = db_connection.cursor()

db_cursor.execute("CREATE TABLE Student(Id INT, first_name TEXT, last_name TEXT)")

db_cursor.execute("INSERT INTO Student VALUES(1,'Carlos', 'Santana')")
db_cursor.execute("INSERT INTO Student VALUES(2,'Pedro', 'Santana')")
db_cursor.execute("INSERT INTO Student VALUES(3,'Marcos', 'Santana')")
db_cursor.execute("INSERT INTO Student VALUES(4,'Julian', 'Santana')")
db_cursor.execute("INSERT INTO Student VALUES(5,'Carolina', 'Lopez')")
db_cursor.execute("INSERT INTO Student VALUES(6,'Josefina', 'Lopez')")
db_cursor.execute("INSERT INTO Student VALUES(7,'Martha', 'Lopez')")
db_cursor.execute("INSERT INTO Student VALUES(8,'Perla', 'Lopez')")

db_connection.commit()

db_cursor.execute("SELECT * FROM Student WHERE first_name = 'Carlos'")

resp = db_cursor.fetchall()

print(resp)

db_connection.close()