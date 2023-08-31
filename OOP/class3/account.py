class Account:
    def __init__(self):
        print("constructor method")

    def get_Bal(self):
        print("instance method")

    @classmethod
    def get_Min_Bal(cls):
        print("class method")

    @staticmethod
    def set_Branch():
        print("static metod")

Account()

