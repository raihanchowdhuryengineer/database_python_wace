import mysql.connector as MyConn
from mysql.connector import Error


# Establish the database connection
my_db = MyConn.connect(
        host='localhost',
        user='root',
        password='admin',
        database='Learincoding'
    )

db_cursor = my_db.cursor()

db_updatedata = 'UPDATE emp SET roll = %s WHERE Ename = %s'
db_value = (30,"Aydian")
    
db_cursor.execute(db_updatedata, db_value)


print(f"Rows affected: {db_cursor.rowcount}")


my_db.commit()

print("Data Updated")

