import random

class bank():
    def __init__(self,acno):
        print("A/c Number:",acno)


acno=random.randint(111111,999999)
bn=bank(acno)