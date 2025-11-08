import sqlite3

try:
    connection = sqlite3.connect("Praicy_db.db")
    cursor = connection.cursor()
    delete_query="DELETE FROM student WHERE rollno=?"
    delete_value =(1,)
    cursor.execute(delete_query,delete_value)
    connection.commit()
    print("Student deleted successfully.")
except sqlite3.Error as error:
        print(error)
finally:
    cursor.close()
    connection.close()



