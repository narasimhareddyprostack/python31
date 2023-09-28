import mysql.connector

db =mysql.connector.connect(host="localhost", user='root', password='root', database='pro12')
dbcursor=db.cursor()

sql_insert=""" 
    insert into employee values(102,'Sonia',55000.00);
"""
dbcursor.execute(sql_insert)
db.commit()

dbcursor.close()
db.close()

