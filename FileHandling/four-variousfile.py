file=open('data2.txt','w')

print("Is Readble:", file.readable())  #False
print("Is writable:", file.writable()) #True

print(file.name)

print("Is File open:", file.closed)
file.close()
print("Is File open:", file.closed)

