import re 
input  = "Mobile Number : 95916191"
found=re.subn("[0-9]","*",input)

print(found)