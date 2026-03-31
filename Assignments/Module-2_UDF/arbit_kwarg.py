def getdata(id,*data,**kwarg):
    print("ID:",id)
    print("Name:",data[0])
    print("City:",data[1])
    print("Subject1:",kwarg["s1"])
    print("Subject2:",kwarg["s2"])
    print("Subject3:",kwarg["s3"])

getdata(101,"Sanket","City",s1="HTML",s2="Python",s3="JAVA")