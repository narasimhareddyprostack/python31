import re 

email = input("Enter Email id::::")
pattern = "[a-zA-Z0-9._-]{3,}@[a-zA-Z0-9.-]{3,}\.[a-zA-Z]{2,4}"
pattern1 = "^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-]+)(\.[a-zA-Z]{2,5}){1,2}$"
result=re.fullmatch(pattern1,email)

if result:
    print("Valid Email Id")
else:
    print("Not Valid")
