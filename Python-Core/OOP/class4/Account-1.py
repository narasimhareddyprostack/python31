class Account:
    def __init__(self,id,name,amount):
        self.acc_Id=id
        self.acc_Name=name
        self.acc_Bal = amount

    def set_Email(self,email):
        self.acc_Email=email


a1=Account(101,'Rahul',5000)
a2=Account(102,'Priyanka',50000)
print(a1.__dict__)
print(a2.__dict__)
a1.set_Email('rahul@pm.com')
a2.set_Email('priyanka@gmail.com')
print(a1.__dict__)
print(a2.__dict__)

a1.loc="Wayanad"

print(a1.__dict__)
print(a2.__dict__)

#how to initilize object values - usign constrctpr
