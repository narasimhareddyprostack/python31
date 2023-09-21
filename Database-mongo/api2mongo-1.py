#invoke api
import requests

resp=requests.get('https://dummyjson.com/products')
data=resp.json()

products = data['products']

""" print(type(data))
print(type(products))

print(products) """
