#read text JSON(one.json) file using python
#https://jsonlint.com/  -- validate json data
import json
emp_json_string = '''{
    "id":101,
    "name":"Rahul",
    "salary":450000,
    "hike":null,
    "avail":false,
    "loc":["Wayanad","New Delhi"]
    }
    '''
print(emp_json_string)
dict_obj=json.loads(emp_json_string)
print(dict_obj)
