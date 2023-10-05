import pymongo

client=pymongo.MongoClient()
db=client['pro15']
col=db['user']

col.insert_one({"id":103, "name":"Priyanka"})
