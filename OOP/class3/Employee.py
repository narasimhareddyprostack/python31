class Employee:
    org_Name = "TCS"
    def __init__(self,id,name):
        print('constrcutor speical method - exec auto')
        self.eId=id
        self.eName=name



e1=Employee(101,"Rahul")
e2=Employee(102,"Sonia")
e3=Employee(103,"Priyanka")
print(e1.__dict__)
print(e2.__dict__)
print(e3.__dict__)

print(Employee.__dict__)