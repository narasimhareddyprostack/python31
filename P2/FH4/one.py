f  = open('emp.json','a')

#print file name
print(f.name)
#is readable or not
print(f.readable())  
#is writable or not 
print(f.writable())
#mode of file 

print(f.mode)
print(f.closed)
f.close()
print(f.closed)
