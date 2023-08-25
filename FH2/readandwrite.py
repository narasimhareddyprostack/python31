file=open('data.txt', 'a+')
file.write('GM')

data = file.read()
print(data)

file.close()

