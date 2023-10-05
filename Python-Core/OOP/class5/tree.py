class Account:

    def get_Details(self):
        print(self) 
    
    @classmethod
    def getNoOfObect(cls):
        print(id(cls))

a1=Account()
""" a1.get_Details() """

print(a1)
print(id(a1))
print(a1.__dict__)

Account.getNoOfObect()