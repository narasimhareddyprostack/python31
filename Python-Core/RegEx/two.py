import re 
input = '''Python Full Stack - 
       Java Full Developer 
       MERN Stack Developer
       '''
found = re.match("Full", input)
print(found.group())
print(found)

if found:
    print("Match Found")
else:
    print("Match Not Found")
