import random

class studinfo:
    def __init__(self):
        print("This is default init method!")
        otp=random.randint(1111,9999)
        print("Your OTP:",otp)
    
    

st=studinfo()
