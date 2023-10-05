class Parent1:
    def m1(self):
        print("Parent1 class m1() method")
class Parent2:
    def m1(self):
        print("Parent2 class m1() method")
    '''    
    def m2(self):
        print("Parent2 class m2() method")
    '''
class Child(Parent2,Parent1):
    def m3(self):
        print("Clild class m3() method") 

obj=Child()
obj.m1()
#obj.m2()
obj.m3()
