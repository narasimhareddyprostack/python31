#user defined exception 

class EligibiltyError(Exception):
    def __init__(self, msg):
        self.msg = msg 

e_age = 20
def checkEligibity(user_Age):

    if user_Age> e_age:
        print('Eligible for Marriagge and enjoy')
    else:
        raise EligibiltyError("Your not eligible for Marriage-Wait some time")

     
checkEligibity(17)
print('GM')
