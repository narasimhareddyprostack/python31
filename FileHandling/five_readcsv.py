import csv
file = open('data.csv','r')
data=csv.reader(file)
print(type(list(data)))
#print(data)
