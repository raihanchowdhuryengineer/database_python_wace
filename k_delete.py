import mysql.connector as MyConn

my_db = MyConn.connect(
        host='localhost',
        user='root',
        password='admin',
        database='Learincoding')
db_cursor = my_db.cursor()

db_deletedata = 'DELETE FROM Learincoding.emp WHERE Ename = %s'

db_value = ('Raihan',)
db_cursor.execute(db_deletedata, db_value)
my_db.commit()

print(db_cursor.rowcount, "Record(s) Deleted")
