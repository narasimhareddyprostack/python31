import os 

#how to find current file name 
print(__file__)

#how to print current file path
print(os.path.abspath(__file__))
print(os.path.dirname(os.path.abspath(__file__)))
print(os.path.join("com","hdfc","user"))