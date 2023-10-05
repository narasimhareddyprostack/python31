#Static variable
class Account:
    bank_Name='SBI'  #static variable
    def __init__(self,id,name):
        self.acc_Id=id 
        self.acc_Name=name 
        Account.branch_Code=5657



a1=Account(101,'Rahul')
a2=Account(102,'Priyanka')
print(a1.__dict__)
print(a2.__dict__)

print(Account.__dict__)