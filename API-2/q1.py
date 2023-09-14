#invokie Rest api and print user names
import requests 
import json 

response=requests.get('https://jsonplaceholder.typicode.com/users')

users=response.json()
print(type(users))
print(users)

for user in users:
    #print(type(user))
    print(user['name'])
