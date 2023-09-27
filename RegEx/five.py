import re 

input ="Pro Stack Academy"

result=re.sub("[a-z | A-Z]","9",input)
print(result)