class InsuffientFundsErr(Exception):
    def __init__(self,msg):
        self.msg = msg
        super().__init__(msg)


acc_bal = 600 

def withdrawl(amount):
    if amount > acc_bal:
        try:
            raise InsuffientFundsErr("Funds not Available")
        except InsuffientFundsErr as err:
            print(err)
    else:
        print("withdraw and enjoy")

withdrawl(100)
print("GM")
