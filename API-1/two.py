#https://dummyjson.com/products/1
import requests

data=requests.get('https://dummyjson.com/products/1')

product = data.json()
print(product)