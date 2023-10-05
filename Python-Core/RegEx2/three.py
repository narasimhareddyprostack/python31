#Password Pattern
# min 5, max 8    {5,8}
# specail char    [^a-zA-Z0-9]+
# 1-Uppercase     [A-Z]+
# \w{5,8}

import re 
pwd = input("Enter Password:::::")
result = re.fullmatch("[^a-zA-Z0-9]+\w{5,8}", pwd)
if result:
    print("Valid")
else:
    print("Not Valid")
