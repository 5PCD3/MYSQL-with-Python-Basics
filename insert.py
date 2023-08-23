import mysql.connector
# import mysql.connector
#create user 'user'@'%' identified by 'password'
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
mycursor = mydb.cursor()
mycursor.execute("insert into test3.test_table1 values(123 , 'pcd')")
mycursor.execute("insert into test3.test_table1 values(234 ,'Jb')")
mydb.commit()
mydb.close()
