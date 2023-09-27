import re
input = '''Python Full Stack - Java Full Developer MERN Stack Developer'''
#          0123456789101112
match=re.search("Stack", input)

print(match)  #Match Object
print(match.start())
print(match.end())
print(match.group())
