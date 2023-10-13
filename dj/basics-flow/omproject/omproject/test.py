import os 

BASE_DIR_ONE = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR= os.path.join(BASE_DIR_ONE,'templates')

print(BASE_DIR_ONE)
print(TEMPLATE_DIR)

print(os.path.dirname(os.path.abspath(__file__)))
print(os.path.join(os.path.dirname(os.path.abspath(__file__)),"templates"))
