acc_bal = 600 
class ISFE(Exception):
    def __init__(self, msg):
        self.msg = msg

def withdrawl(amount):
    if amount>acc_bal:
        try:
            #raise ISFE('Buddy - check your Balance')
            raise ZeroDivisionError("Cant Devide by Zero")

        except ZeroDivisionError as err:
            print(err)

        except ISFE as err:
            print(err)
    else:
        print('withdrawl and enjoy')

withdrawl(1000)
print("GM")
