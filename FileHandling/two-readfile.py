file=open('data.txt','r')

#print(file.read()) #return all data from file 
#print(file.read(5)) #return first 5 char
#print(file.readline()) #return first line of text file
print(file.readlines())#return file content in the form of list

file.close()
