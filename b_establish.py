import mysql.connector as MyConn
    # Establish the connection
mydb = MyConn.connect(
        host='localhost',
        user='root',
        password='admin')
print(mydb,"Established")
