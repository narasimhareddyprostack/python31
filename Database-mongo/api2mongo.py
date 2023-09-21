#invoke api
import requests
import pymongo
resp=requests.get('https://dummyjson.com/products')
data=resp.json()

products = data['products']
new_Products=[]

for product in products:
    new_Products.append({'id':product['id']})



client = pymongo.MongoClient()
db=client['pro15']
col=db['newproducts']

col.insert_many(products)
