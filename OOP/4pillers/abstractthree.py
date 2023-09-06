from abc import *
class Bank:
    
    @abstractmethod
    def cal_bal(self):
        pass
    
print(Bank())
