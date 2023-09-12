#user.json
import json 

f = open('user.json','r')
data_list=json.load(f)
#print(data)
print(type(data_list))

for user_dict  in data_list:
    print(user_dict['name'])