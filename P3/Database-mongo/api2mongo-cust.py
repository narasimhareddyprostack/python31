#invoke api
import requests

resp=requests.get('https://dummyjson.com/products')
data=resp.json()

products = data['products']
new_Products=[]

for product in products:
    new_Products.append({'id':product['id'], 'name':product['title'], 'price':product['price']})

print(new_Products)

#insert into mongodb/mysql


