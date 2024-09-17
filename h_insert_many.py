import mysql.connector as MyConn
mydb=MyConn.connect(host='localhost', user='root', password='admin', database='Learincoding')
db_cursor=mydb.cursor()
db_insert="insert into Emp(Roll,Ename) values(%s,%s)"
db_list=[(30,'Anis'),(40,'Altaf'),(50,'Abdul')]
db_cursor.executemany(db_insert,db_list)
mydb.commit()
print(db_cursor.rowcount,"Record Inserted") 