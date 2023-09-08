from Account import *

from SA import * 
from CA import * 

def generate_AccountBal(obj):
    print(obj.cal_bal())

accounts=[SA(103,'Abhilash',80000),CA(104,'Vamsi',90000)]

for account in accounts:
    generate_AccountBal(account)