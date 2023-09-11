filename = input("Enter File Name:")
try:
    fp = open(filename,'r')
    data=fp.read()
    
except :
    print('except block exe')
    fp=open('emp.json','r')
    data=fp.read()
   