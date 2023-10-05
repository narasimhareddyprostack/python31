class Parent:
    def m1(self):
        print("Parent class m1() method")

class Child(Parent):
    def m2(self):
        print("Clild class m2() method") 

obj=Child()
obj.m1()
obj.m2()