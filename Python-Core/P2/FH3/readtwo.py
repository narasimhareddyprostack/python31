#read text CSV(one.csv) using python

import csv
f = open('one.csv', 'r')
cp = csv.reader(f)
print(cp)
print(type(cp))


for line in list(cp):
    #print(line)
    for word in line:
        print(word,end=" ")
    print()


f.close()