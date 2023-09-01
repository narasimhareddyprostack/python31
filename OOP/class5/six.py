class Bank:
    min_Bal=0  #static variable
    @classmethod
    def set_Min_Bal(cls):
        cls.min_Bal = 600


#Bank.min_Bal = 500
#print(Bank.min_Bal)
Bank.set_Min_Bal()
print(Bank.min_Bal)


#how to access/update static variable - without creating object
#outside clsss- using class name
