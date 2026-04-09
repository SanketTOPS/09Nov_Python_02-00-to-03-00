file=open('test.txt','w')

id=input("Enter an ID:")
name=input("Enter a Name:")
city=input("Enter a City:")

"""file.write(id)
file.write(name)
file.write(city)"""

file.write(f"ID:{id}\nName:{name}\nCity:{city}")