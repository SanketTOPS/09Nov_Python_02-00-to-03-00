class studinfo:
    stid=12
    stnm="Sanket"
    
    def getdata(self):
        print("This is getdata!")
    
    def getsum(self,a,b):
        print("Sum:",a+b)

#Object of class
st=studinfo()
print("ID:",st.stid)
print("Name:",st.stnm)
st.getdata()
st.getsum(12,45)
