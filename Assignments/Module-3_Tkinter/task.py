import tkinter

tk=tkinter.Tk()
tk.title("Calc")
tk.geometry("400x400")
tk.config(bg="lightblue")

t1=tkinter.Entry()
t1.place(x=25,y=25)

t2=tkinter.Entry()
t2.place(x=25,y=75)

def Add():
    n1=t1.get()
    n2=t2.get()
    ans=int(n1)+int(n2)
    print("Sum:",ans)

b1=tkinter.Button(text="+",command=Add)
b1.place(x=25,y=125)

b2=tkinter.Button(text="-")
b2.place(x=125,y=125)

b3=tkinter.Button(text="*")
b3.place(x=225,y=125)

b4=tkinter.Button(text="/")
b4.place(x=325,y=125)



tk.mainloop()