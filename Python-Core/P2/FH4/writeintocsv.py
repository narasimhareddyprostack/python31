import csv
f = open('emp.csv','w', newline="")
#get the csv pointer object
cp=csv.writer(f)
cp.writerow(['id','Name','Salary'])

for i in range(3):
    eid=  input("Enter Employee Id:")
    eName= input("Enter Employee Name:")
    eSal = input("Enter Employee Salary:")
    cp.writerow([eid,eName,eSal])


f.close()