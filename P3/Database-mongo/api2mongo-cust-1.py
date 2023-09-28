#invoke api
import requests

import pymongo
client = pymongo.MongoClient()
db=client['pro15']
col=db['newProducts']

resp=requests.get('https://dummyjson.com/products')
data=resp.json()

products = data['products']
new_Products=[]

for product in products:
    new_Products.append({'id':product['id'], 'name':product['title'], 'price':product['price']})

print(new_Products)

#insert into mongodb/mysql
col.insert_many(new_Products)
