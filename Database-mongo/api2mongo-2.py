#invoke api
import requests

resp=requests.get('https://dummyjson.com/products')
data=resp.json()

products = data['products']

for product in products:
    print(product['title'])
