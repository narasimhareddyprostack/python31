#invoke rest api and write into new json file
import requests
import json 

resp=requests.get('https://jsonplaceholder.typicode.com/users')
users=resp.json()
#print(users)
#convert python list into json - json.dumps()

user_json=json.dumps(users)
#print(user_json)

