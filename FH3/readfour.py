#read json file(one.json) 

import json 
f = open('one.json','r')
emp_dict=json.load(f)
print(emp_dict)
#print emp name 

print(emp_dict['name'])