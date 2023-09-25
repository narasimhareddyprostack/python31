import pymongo

client = pymongo.MongoClient()
db   = client['pro16']
col =  db['user']
data = col.find() 
print(data)

for user in data:
    print(user['eid'])