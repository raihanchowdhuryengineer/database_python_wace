import mysql.connector as MyConn
mydb=MyConn.connect(host='localhost', user='root', password='admin', database='Learincoding')
db_cursor=mydb.cursor()
db_cursor.execute("insert into Emp(Roll,Ename) values(%s,%s)", 
                (20,"Raihan"))
mydb.commit()
print(db_cursor.rowcount,"Record Inserted") 