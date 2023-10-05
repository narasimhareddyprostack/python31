from Account import * 

class  CA(Account):
    
    #static variable 
    min_bal = 5000
    def __init__(self,aid,name,amount):
        super().__init__(aid,name)
        self.acc_amount = amount
    def get_min_Bal(self):
        return self.min_bal 
    
    def deposit_amount(self,amount):
        self.acc_amount = self.acc_amount + amount 
    
    def cal_bal(self):
        return self.acc_amount - self.min_bal 



#a2=CA(102,'sonia',70001)
#a2.deposit_amount(60)
#print(a2.cal_bal())
