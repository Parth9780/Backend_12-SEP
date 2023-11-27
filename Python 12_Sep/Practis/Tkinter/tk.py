import tkinter as tk
from tkinter import *

r = tk.Tk()
r.title('Counting Seconds')
r.geometry("500x600")
r.config(bg="lightgray")
r.title("TkinterApp")

fvalue=tk.Label(text="Value: ",bg='Lightgray',fg='blue',font='Calibri 40 bold')
fvalue.grid(row=0,column=0)
svalue=tk.Label(text="Value: ",bg='Lightgray',fg='blue',font='Calibri 40 bold')
svalue.grid(row=1,column=0)

tk.Entry().grid(row=0,column=1)
tk.Entry().grid(row=1,column=1)


def add_button():
    result = fvalue.get()+svalue.get()
    messagebox.showinfo("Success",f("{fvalue.get()}+{svalue.get()}"))
    
def sub_button():
    result = fvalue.get()-svalue.get()
    messagebox.showinfo("Success",f("{fvalue.get()}-{svalue.get()}"))
    
def mul_button():
    result = fvalue.get()*svalue.get()
    messagebox.showinfo("Success",f("{fvalue.get()}*{svalue.get()}"))

def div_button():
    result = fvalue.get()/svalue.get()
    messagebox.showinfo("Success",f("{fvalue.get()}/{svalue.get()}"))


tk.Button(text="Add",font='Calibri 30 bold',command=add_button).place(x=100,y=150)
tk.Button(text="Sub",font='Calibri 30 bold',command=sub_button).place(x=230,y=150)
tk.Button(text="Mul",font='Calibri 30 bold',command=mul_button).place(x=100,y=270)
tk.Button(text="Div",font='Calibri 30 bold',command=div_button).place(x=230,y=270)


intvar = IntVar()
intvar.set(100)
r.mainloop()

