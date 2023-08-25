import csv
file = open('data.csv', 'r')
csv_Obj=csv.reader(file)
data = list(csv_Obj)

for line in data:
    for word in line:
        print(word, end=" ")
    print()