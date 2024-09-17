import mysql.connector as MyConn

my_db=MyConn.connect(host='localhost',
                     user='root',
                     password='admin', 
                     database='Learincoding')

db_curor=my_db.cursor()

db_curor.execute("select * from Learincoding.emp")

for db_data in db_curor.fetchall():
    print(db_data)