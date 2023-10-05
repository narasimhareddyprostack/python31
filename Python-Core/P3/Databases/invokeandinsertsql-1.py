#https://jsonplaceholder.typicode.com/users
#invoke api and insert data into user table

import requests
import json 
import mysql.connector

res=requests.get('https://jsonplaceholder.typicode.com/users')
user_list=res.json()

#prepare data

""" 
print(type(user_list))
print(user_list) """

""" for user in user_list:
    print(user['id'],":", user['name']) """

data = []

for user in user_list:
    data.append((user['id'], user['name']))


print(data)
