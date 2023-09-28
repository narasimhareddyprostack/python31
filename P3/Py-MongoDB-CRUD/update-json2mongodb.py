#read json data  and write into mongodb collection 
#mongodb - database name: pro16
#mongodb - collection name:user

import json 
import pymongo 

file= open('user.json','r')
data=json.load(file)
print(data)

client = pymongo.MongoClient()

db= client['pro16']
col = db['user']
col.insert_many(data)