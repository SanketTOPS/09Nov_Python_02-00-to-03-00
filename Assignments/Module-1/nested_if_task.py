a=int(input("Enter Number1:"))
b=int(input("Enter Number2:"))

if a!=0 and b!=0:
    if a>b:
        print("Sum:",a+b)
    else:
        print("Mul:",a*b)
else:
    print("Error!Invalid number...")