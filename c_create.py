import mysql.connector as MyConn
    # Establish the connection
mydb = MyConn.connect(
        host='localhost',
        user='root',
        password='admin')

db_cursor=mydb.cursor()
db_cursor.execute("Create Database Learincoding")
print("Database created Succesfully")
