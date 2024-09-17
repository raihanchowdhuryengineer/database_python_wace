import mysql.connector as MyConn

my_db = MyConn.connect(
        host='localhost',
        user='root',
        password='admin',
        database='recordlist')
db_cursor = my_db.cursor()

db_deletedata ='truncate table Learincoding.emp'

db_cursor.execute(db_deletedata)

my_db.commit()

print("All Information Deleted")