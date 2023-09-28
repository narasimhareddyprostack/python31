#veify given Mobile number is indian mobile or not

import re 
mobile = input("Enter Mobile Number:")

result=re.fullmatch("[6-9]\d{9}", mobile)

if result :
    print("Given Number is Valid India Mobile")
else:
    print("Not Valid")