from Account import * 

class SA(Account):
    #static variable
    min_bal  = 500
    def __init__(self,aid,name,amount):
        super().__init__(aid,name)
        self.acc_amount = amount

    def get_min_Bal(self):
        return self.min_bal

    def deposit_amount(self,amount):
        self.acc_amount = self.acc_amount + amount 

    def cal_bal(self):
        return self.acc_amount - self.min_bal

#a1=SA(101,'rahul',50001)
#a1.deposit_amount(10)
#print(a1.__dict__)
#print(a1.cal_bal())
