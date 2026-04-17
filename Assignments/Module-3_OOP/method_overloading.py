class studinfo:
    #Method Overloading
    
    def getdata(self,id):
        print("ID:",id)
        
    def getdata(self,name):
        print("Name:",name)

st=studinfo()
st.getdata("Sanket")
