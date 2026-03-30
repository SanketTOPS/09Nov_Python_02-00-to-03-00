def getdata(id,name,city):
    print("ID:",id)
    print("Name:",name)
    print("City:",city)

n=int(input("HOw many students you want:"))
for i in range(n):
    stid=input("Enter your ID:")
    stnm=input("Enter your name:")
    stct=input("Enter your city:")
    
    getdata(stid,stnm,stct)