import pymongo

client = pymongo.MongoClient()
db=client['pro16']
col=db['user']

#col.delete_one({'eid':11})
col.delete_many({})