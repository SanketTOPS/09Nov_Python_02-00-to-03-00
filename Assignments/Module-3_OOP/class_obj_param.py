class studinfo:
    def getdata(self,stid,stnm):
        print("ID:",stid)
        print("Name:",stnm)

st=studinfo()
#st.getdata(101,'Sanket')

id=input("Enter an ID:")
name=input("Enter a Name:")
st.getdata(id,name)
