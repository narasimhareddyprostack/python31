from Account import *

class SA(Account):
    min_bal = 500
    def __init__(self,id,name,amount):
        super().__init__(id,name)
        print('SA - class Constructor')
        self.acc_bal = amount
        
    def cal_bal(self):
        #print("Your Account Balance:")
        return self.acc_bal - self.min_bal



a1=SA(101,'Rahul',5001)
#print(a1.__dict__)
#print(SA.__dict__)
print("Your Account Balance:",a1.cal_bal())
