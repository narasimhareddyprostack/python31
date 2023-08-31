class Account:
    
    def __init__(self):
        self.acc_Id=101
        self.acc_Name="Rahul"

    def open_Account(self):
        print("Account Successfully")
    def despit_Amount(self):
        print("Amount deposited")

a1=Account()


print(a1)
print(a1.__dict__)