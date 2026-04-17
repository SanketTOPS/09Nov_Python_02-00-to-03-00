class studinfo:
    #private
    __stid=12
    __stnm="Sanket"
    
    def __getdata(self): #private
        print("ID:",self.__stid)
        print("Name:",self.__stnm)
    
    def printdata(self):
        self.__getdata()
    

st=studinfo()
"""print(st.stid)
print(st.stnm)"""

#st.getdata()
st.printdata()