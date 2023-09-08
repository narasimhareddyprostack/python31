class Account:
    
    #instance method
    def cal_bal(self):
        print("cal_bal method -0 arg")
    def cal_bal(self,a):
        print("cal_bal method -1 arg")

    def cal_bal(self,a,b):
        print("cal_bal method -2 arg")


a1= Account()
a1.cal_bal()
