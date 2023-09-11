filename=input("Enter File Name:")

try:
    fp=open(filename,'r')
    data=fp.read()
    print(data)
except FileNotFoundError as fnf:
    print(fnf)
    
print("GM")