import mysql.connector
# import mysql.connector
#create user 'user'@'%' identified by 'password'
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
mycursor = mydb.cursor()

mycursor.execute("select * from test3.test_table1")
# mycursor.execute("select c1 , c5 from test3.test_table1")   It with take c1 and c5 from this table
for i in mycursor.fetchall():
    print(i)
mydb.close()
