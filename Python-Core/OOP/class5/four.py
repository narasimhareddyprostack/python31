class Utility:
    

    @staticmethod
    def add(a,b):
        print(a+b)
    
    @staticmethod
    def sub(a,b):
        return a-b

    @staticmethod
    def multi(a,b):
        return a*b



obj = Utility()

obj.add(10,20)
print(obj.sub(200,100))
print(obj.multi(5,10))
