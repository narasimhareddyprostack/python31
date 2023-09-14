#https://dummyjson.com/
#https://jsonplaceholder.typicode.com/

import requests 
import json
res=requests.get('https://jsonplaceholder.typicode.com/users')

user_json=res.json()

for user in user_json:
    print(user['name'])
print(type(user_json))

#user_dict = json.loads(user_json)

#print(user_dict)
#print(user_json)

#invokie Rest api and print user names 
#invoke Rest api and store data in new json file
#invoke Rest api and store data in mongodb
#invoke Rest api and store data in mysql

