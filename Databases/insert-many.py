import mysql.connector

db=mysql.connector.connect(host="localhost",
                        user="root",
                        password="root",
                        database="pro12"
)
dbcursor=db.cursor()
sql_st = """
            insert into employee values(%s,%s,%s)
        """
data = [ (103, 'priyanka', 65000.00), 
         (103, 'amith',75000.00), 
         (105, 'modi', 85000.00)]
dbcursor.executemany(sql_st,data)

db.commit()
dbcursor.close()
db.close()
