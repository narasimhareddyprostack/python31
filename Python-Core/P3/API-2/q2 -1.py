#invoke rest api and write into new json file
import requests
import json 

resp=requests.get('https://jsonplaceholder.typicode.com/users')
users=resp.json()




""" print(users)
print(type(users))

 """

#write into new json file
""" 
fp=open('user.json','w')
json.dump(fp,users)
fp.close()
 """
