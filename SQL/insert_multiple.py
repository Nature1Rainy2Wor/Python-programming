import sqlite3

try:
    connection = sqlite3.connect("Praicy_db.db")
    cursor = connection.cursor()
    insert_data_query="""
        INSERT INTO student(name,email,course,cgpa) VALUES (?,?,?,?)
        """
    student_records=[
        ("Praicy","praicysam1@gmail.com","MCA",8.9),
        ("Akshsya","akshaya@gmail.com","B.sc Nursing",9.56),
        ("Virushma","virushma@gmail.com","NEET Training",10.0),
        ]
    cursor.executemany(insert_data_query, student_records)
    connection.commit()
    print("All Student Records Inserted Successfully.")
except sqlite3.Error as error:
    print(error)
finally:
    cursor.close()
    connection.close()