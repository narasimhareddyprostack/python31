import json
emp_dict={
    "id":101,
    "name":"Rahul",
    "salary":None,
    "avail":True
}
print(emp_dict)
print(type(emp_dict))

emp_json= json.dumps(emp_dict)
print(emp_json)
print(type(emp_json))