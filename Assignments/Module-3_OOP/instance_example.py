class studeinfo:
    stid=101
    stnm='Sanket'
    
    def getdata(self):
        print("ID:",self.stid)
        print("Name:",self.stnm)
    
    def getsum(self,a,b):
        return a+b
        
#Calling via Object
"""st=studeinfo()
st.getdata()
st.stid=102
st.stnm='Nirav'
st.getdata()"""

#Calling via Instance
studeinfo().getdata()
studeinfo().stid=102
studeinfo().stnm='Ashok'
studeinfo().getdata()
x=studeinfo().getsum()
    
    