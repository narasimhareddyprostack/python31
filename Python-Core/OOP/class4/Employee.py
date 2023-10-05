class Employee:
    org_Name = "TCS"  #static variable

    @classmethod
    def cal_Age(cls):
        print(cls.__dict__)
        print(cls.org_Name)
    
    def get_Details(self):
        #print(cls.org_Name)
        print(self.org_Name)  #TCS
        print(Employee.org_Name) #TCS

e1=Employee()

Employee.cal_Age()  #invoking class method
e1.get_Details()  #invoking instance method
""" 
e1.get_Details()
print(e1.__dict__)
print(Employee.__dict__)

 """
