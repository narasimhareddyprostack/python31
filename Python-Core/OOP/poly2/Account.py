from Bank import * 

class Account(Bank):
    
    def __init__(self,aid,name):
        self.acc_id  = aid 
        self.acc_name = name
    #setter and getter - instance method

    def open_account(self):
        print('account opened successfully')
    
    def deposit_amount(self):
        pass

    def cal_bal(self):
        print('account class - cal_Bal')


#Account()