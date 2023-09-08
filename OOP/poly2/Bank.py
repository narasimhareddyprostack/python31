from abc import *
class Bank(ABC):
    @abstractmethod
    def cal_bal(self):
        pass


