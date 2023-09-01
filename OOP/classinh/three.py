class P1:
    def m1(self):
        print("Parent 1 - m1 method")

class P2:
    def m1(self):
        print("Parent 2 - m1 method")

class C(P2,P1):
    pass

c=C()
c.m1()