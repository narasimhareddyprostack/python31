from abc import *
class Bank(ABC):
    
    @abstractmethod
    def cal_bal(self):
        pass
    
class Account(Bank):
    def cal_bal(self):
        print("Bal is low")
    

a1=Account()
a1.cal_bal()