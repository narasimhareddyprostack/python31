#https://jsonplaceholder.typicode.com/users
#invoke api and insert data into user table

import requests
import json 
import mysql.connector


db = mysql.connector.connect(host="localhost",
                             user="root",
                             password="root",
                             database="pro12"
                             )
dbcursor = db.cursor()


res = requests.get('https://jsonplaceholder.typicode.com/users')
user_list = res.json()

sql_st = """
insert into user values(%s,%s)
"""
data = []
for user in user_list:
    data.append((user['id'], user['name']))


dbcursor.executemany(sql_st, data)
db.commit()
dbcursor.close()
db.close()

