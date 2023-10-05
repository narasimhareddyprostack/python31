class Test:
    a = 100 
    def __init__(self):
        Test.b = 200
    def m1(self):
        Test.c = 300
    @classmethod
    def m2(cls):
        cls.d=400
        Test.e=500
    @staticmethod
    def m3():
        Test.f=600


t1=Test()
t1.m1()
t1.m2()
t1.m3()
Test.g = 700
print(t1.__dict__)
print(Test.__dict__)