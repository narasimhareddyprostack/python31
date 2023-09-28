#invoke rest api and write into new json file
import requests
import json 

resp=requests.get('https://jsonplaceholder.typicode.com/users')
users=resp.json()



#user_json=json.dumps(users)

fp=open('user.json','w')
json.dump(users, fp)
fp.close()
