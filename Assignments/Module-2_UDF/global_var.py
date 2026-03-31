"""id=101
Name='Sanket'

def getdata():
    print("ID:",id)
    print("Name:",Name)

getdata()"""


x=10
print("X:",x)

def getval():
    global x
    x+=10
    print("X:",x)
    
getval()