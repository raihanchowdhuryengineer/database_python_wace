import mysql.connector as MyConn
from mysql.connector import Error

# Establish the database connection
my_db = MyConn.connect(
    host='localhost',
    user='root',
    password='jojosiwa',
    database='practice'
)

try:
    db_cursor = my_db.cursor()

    # Check current data
    db_cursor.execute("SELECT * FROM emp WHERE Ename = '30'")
    results = db_cursor.fetchall()
    print("Current Data:", results)

    # Update the name from 'Aydian' to 'Ariyan' based on roll number
    db_updatedata = 'UPDATE emp SET Ename = %s WHERE roll = %s'
    db_value = ("Abdullah", 30)

    db_cursor.execute(db_updatedata, db_value)

    print(f"Rows affected: {db_cursor.rowcount}")

    # Commit the changes to the database
    my_db.commit()
    print("Data Updated")

except Error as e:
    print(f"Error: {e}")
finally:
    if my_db.is_connected():
        db_cursor.close()
        my_db.close()
