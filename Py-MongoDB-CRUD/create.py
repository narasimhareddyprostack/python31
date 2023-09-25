import pymongo

client=pymongo.MongoClient()

db = client['pro16']
col=db['emp']

col.insert_one({"eid":101, "ename":"rahul","esal":45000})

print('collection successfully')
print('data inserted successfully')