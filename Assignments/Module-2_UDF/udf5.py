data=[]
def getdata(id,name,city):
    stdata={
        "id":id,
        "name":name,
        "city":city
    }
    data.append(stdata)
    
n=int(input("How many students you want:"))
for i in range(n):
    stid=input("Enter your ID:")
    stnm=input("Enter your name:")
    stct=input("Enter your city:")
    
    getdata(stid,stnm,stct)

print(data)