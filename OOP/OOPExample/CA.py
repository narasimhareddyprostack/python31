from Account import *

class CA(Account):
    min_bal = 25000
    def __init__(self,id,name,amount):
        super().__init__(id,name)
        self.acc_bal = amount
    def cal_bal(self):
        return self.acc_bal - self.min_bal

a2=CA(102,'priyanka', 500000)
print("Your Account Balance:",a2.cal_bal())



