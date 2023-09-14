import mysql.connector
#provide credential to connect your database
mydb = mysql.connector.connect(host="localhost", user="root", password="root", database="pro12")

cursor=mydb.cursor()
cursor.execute('describe employee')
data = cursor.fetchall()

for value in data:
    print(value)

mydb.close()