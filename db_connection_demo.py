import sqlite3

try:
    # Connection to the datatype
    connection=sqlite3.connect('Praicy_db.db')
    cursor=connection.cursor()

    #select and print data
    cursor.execute("SELECT * FROM book")
    print("Book in the database:" )
    for row in cursor.fetchall():
        print(row)
except sqlite3.Error as e:
    print(f"SQlite error:{e}")
finally:
    if connection:
        connection.close()

        #NEW PROGRAM
        import sqlite3

        try:
            # Connection to the datatype
            connection = sqlite3.connect('Praicy_db.db')
            cursor = connection.cursor()

            # select and print data
            cursor.execute("UPDATE * FROM book")
            print("Book in the database:")
            for row in cursor.fetchall():
                print(row)
        except sqlite3.Error as e:
            print(f"SQlite error:{e}")
        finally:
            if connection:
                connection.close()



