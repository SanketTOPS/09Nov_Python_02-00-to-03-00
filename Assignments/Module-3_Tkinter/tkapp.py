import tkinter
from tkinter import ttk,messagebox

tk=tkinter.Tk()
tk.title("MyApp")
tk.config(background="lightblue")
tk.geometry("400x500")

"""l1=tkinter.Label(text="Firstname")
l1.pack()
l2=tkinter.Label(text="Lastname")
l2.pack()"""

"""l1=tkinter.Label(text="Firstname")
l1.place(x=0,y=0)

l2=tkinter.Label(text="Lastname")
l2.place(x=0,y=30)"""

l1=tkinter.Label(text="Firstname",bg='lightblue',fg='red',font='Elephant 15 bold')
l1.grid(row=0,column=0,sticky='w')

l2=tkinter.Label(text="Lastname",bg='lightblue',fg='red',font='Elephant 15 bold')
l2.grid(row=1,column=0,sticky='w')

t1=tkinter.Entry()
t1.grid(row=0,column=1,sticky='w')

t2=tkinter.Entry()
t2.grid(row=1,column=1,sticky='w')

m=tkinter.Radiobutton(value=0, text="Male",bg='lightblue',fg='red',font='Elephant 15 bold')
f=tkinter.Radiobutton(value=1,text="Female",bg='lightblue',fg='red',font='Elephant 15 bold')
m.grid(row=2,column=0,sticky='w')
f.grid(row=2,column=1,sticky='w')

c1=tkinter.Checkbutton(text="Gujarati",bg='lightblue',fg='red',font='Elephant 15 bold')
c2=tkinter.Checkbutton(text="Hindi",bg='lightblue',fg='red',font='Elephant 15 bold')
c3=tkinter.Checkbutton(text="English",bg='lightblue',fg='red',font='Elephant 15 bold')
c1.grid(row=3,column=0,sticky='w')
c2.grid(row=4,column=0,sticky='w')
c3.grid(row=5,column=0,sticky='w')

city=['Rajkot','Ahmedabad','Surat','Gandhinagar','Baroda']

dd=ttk.Combobox(values=city)
dd.grid(row=6,column=0,sticky='w')

def btnclick():
    #print("Button clicked!")
    #messagebox.showerror("Error","Something went wrong...")
    #messagebox.showinfo("Success","Login Success!")
    messagebox.showwarning("Warning","Disk is full")

btn=tkinter.Button(text="Submit",fg='red',font='Elephant 15 bold',command=btnclick)

btn.place(x=150,y=280)
tk.mainloop()