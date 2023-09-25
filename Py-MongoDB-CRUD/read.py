import pymongo

client = pymongo.MongoClient()
db   = client['pro16']
col =  db['user']
#data = col.find({'eid':11}) 
data = col.find() 
print(data)
for user in data:
    print(user)
""" 
for user in data:
    print(user['eid']) """