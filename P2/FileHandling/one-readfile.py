#read file and print file data

file = open('data.txt','r')
data=file.read()
print(data)
file.close()