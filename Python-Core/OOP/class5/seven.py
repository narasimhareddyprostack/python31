class Account:
    count=0
    def __init__(self):
        Account.count  = Account.count +1
    @classmethod
    def noOfObject(cls):
        print(cls.count)


Account()
Account()
Account()
Account()
Account()
Account()
#print how many object are crate for class
#print(Account.count)
Account.noOfObject()