filename= input("Enter file Name:")

fp=open(filename,'r')
data = fp.read()
print(data)

print("GM")
#FileNotFoundError