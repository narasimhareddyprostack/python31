class Employee:
    org_Name = "TCS"  #static variable

    @classmethod
    def cal_Age(cls):
        print(cls.__dict__)
    
    def get_Details(self):
        print(cls.org_Name)
        print(self.org_Name)
        print(Employee.org_Name)


e1=Employee()
e2=Employee()

Employee.cal_Age()
""" 
print(e1.__dict__)  #{}
print(e2.__dict__)  #{}
print(Employee.__dict__)  #{ org_Name:'TCS} """