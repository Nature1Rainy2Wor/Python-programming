import sqlite3

try:
    connection = sqlite3.connect("Praicy_db.db")
    cursor = connection.cursor()
    create_table_query = """
        CREATE TABLE student(
        rollno INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(40),
        email VARCHAR(40),
        course VARCHAR(10),
        cgpa DECIMAL(10,2))
        """
    cursor.execute(create_table_query)
    connection.commit()
    print("Table created successfully.")
except sqlite3.Error as error:
    print(error)
finally:
    cursor.close()
    connection.close()