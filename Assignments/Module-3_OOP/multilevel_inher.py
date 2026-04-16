class ashok:
    aid:int
    atech:str
    
    def a_getdata(self):
        self.aid=input("Enter Ashok's ID:")
        self.atech=input("Enter Ashok's Tech:")
        
class hitesh(ashok):
    hid:int
    htech:str
    
    def h_getdata(self):
        self.hid=input("Enter Hitesh's ID:")
        self.htech=input("Enter Hitesh's Tech:")

class gopal(hitesh):
    gid:int
    gtech:str
    
    def g_getdata(self):
        self.gid=input("Enter Gopal's ID:")
        self.gtech=input("Enter Gopal's Tech:")

class tops(gopal):
    def printdata(self):
        print("------Ashok's Info------")
        print("Ashok's ID:",self.aid)
        print("Ashok's Tech:",self.atech)
        print("------Hitesh's Info------")
        print("Hitesh's ID:",self.hid)
        print("Hitesh's Tech:",self.htech)
        print("------Gopal's Info------")
        print("Gopal's ID:",self.gid)
        print("Gopal's Tech:",self.gtech)
        
tp=tops()
tp.a_getdata()
tp.h_getdata()
tp.g_getdata()
tp.printdata()