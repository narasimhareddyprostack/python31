#invoke api
import requests
import pymongo
resp=requests.get('https://dummyjson.com/products')
data=resp.json()

products = data['products']

client = pymongo.MongoClient()
db=client['pro15']
col=db['products']

col.insert_many(products)
