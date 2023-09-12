#read text JSON(one.json) file using python
#https://jsonlint.com/  -- validate json data
import json

f= open('one.json','r')

emp_dict=json.load(f)
print(emp_dict)
print(type(emp_dict))

#print dict object key,values

for key,value in emp_dict.items():
    print(key)