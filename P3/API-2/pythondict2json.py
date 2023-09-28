#python  dict to json 

import json 

emp_dict = { 'id':101, 'name':'rahul', 'avail':None, 'sal':True }
emp_json=json.dumps(emp_dict)
print(emp_dict)
print(emp_json)