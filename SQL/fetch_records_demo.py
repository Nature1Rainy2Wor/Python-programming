import sqlite3

try:
    connection = sqlite3.connect("Praicy_db.db")
    cursor = connection.cursor()
    select_all_query="SELECT name,email,course,cgpa FROM student"
    cursor.execute(select_all_query)
    result=cursor.fetchall()
    for row in result:
        print(row)
    select_names_query="SELECT name FROM student"
    cursor.execute(select_names_query)
    names=cursor.fetchall()
    for name in names:
        print(name)
except sqlite3.Error as error:
        print(error)
finally:
    cursor.close()
    connection.close()



