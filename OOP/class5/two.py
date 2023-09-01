class Account:
    min_Bal = 500
    def __init__(self,id,name):
        print('constructor is special method-intilize objct value')
        #print(self)
        self.eid=id
        self.name=name



a1=Account(101,'Rahul')
print(id(a1))