file=open('new.txt','a')

id=input("Enter an ID:")
name=input("Enter a Name:")
city=input("Enter a City:")

file.write(f"ID:{id}\nName:{name}\nCity:{city}\n--------\n")