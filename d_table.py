import mysql.connector as MyConn
mydb=MyConn.connect(host='localhost', user='root', password='admin', database='Learincoding')
db_cursor=mydb.cursor()
db_cursor.execute('create table Emp(Roll int, Ename varchar(20))')
print('table created')