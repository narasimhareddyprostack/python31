import json
emp_json_string='''{"id": 101, "name": "Rahul", "salary": null, "avail": true}'''
#conver into json string to pyton dict

print(emp_json_string)
emp_dict=json.loads(emp_json_string)
print(emp_dict)