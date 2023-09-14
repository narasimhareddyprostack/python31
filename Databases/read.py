import mysql.connector
db = mysql.connector.connect(
    host="localhost", user='root', password='root', database='pro12')

dbcursor=db.cursor()
dbcursor.execute('select * from employee')
empdata=dbcursor.fetchall()


for emp in empdata:
    print(emp)

dbcursor.close()
db.close()
