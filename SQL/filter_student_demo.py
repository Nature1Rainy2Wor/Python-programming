import sqlite3

try:
    connection = sqlite3.connect("Praicy_db.db")
    cursor = connection.cursor()
    filter_query="SELECT name,email,course,cgpa FROM student where course=?"
    filter_value =('B.sc Nursing',)
    cursor.execute(filter_query, filter_value)
    result=cursor.fetchall()
    for row in result:
        print(row)
except sqlite3.Error as error:
        print(error)
finally:
    cursor.close()
    connection.close()



