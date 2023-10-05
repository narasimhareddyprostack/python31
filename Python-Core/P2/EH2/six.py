#user defined exception 

class EligibiltyError(Exception):
    def __init__(self, msg):
        self.msg = msg 

e_age = 20
def checkEligibity(user_Age):

    if user_Age> e_age:
        print('Eligible for Marriagge and enjoy')
    else:
        try:
            #raise EligibiltyError("Your not eligible for Marriage-Wait some time")
            #raise ZeroDivisionError('Cant divide')
            raise NameError('checking Exception')
        except ZeroDivisionError as err:
            print(err)
        except EligibiltyError as err:
            print(err)
        except Exception as err:
            print(err)

     
checkEligibity(17)
print('GM')
