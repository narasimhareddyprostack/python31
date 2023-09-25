import pymongo 

client = pymongo.MongoClient()
db = client['pro16']
col = db['user']

col.update_one({"eid":11},{"$set":{"ename":"Rahul Gandhi"}})

print("updated successfully")