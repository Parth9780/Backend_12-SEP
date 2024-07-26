import tkinter as tk
# from tkinter import ttk,messagebox

r = tk.Tk()
r.title('Counting Seconds')
r.geometry("500x600")
r.config(bg="lightgray")
r.title("TkinterApp")

fvalue=tk.Label(text="First Value: ",bg='Lightgray',fg='blue',font='Chiller 15 bold')
fvalue.grid(row=0,column=0)
svalue=tk.Label(text="Second value: ",bg='Lightgray',fg='blue',font='Chiller 15 bold')
svalue.grid(row=0,column=0)

tk.Entry().grid(row=0,column=1)
tk.Entry().grid(row=1,column=1)


def add_button():
    messagebox.showinfo("Success",f("{fvalue.get()}+{svalue.get()}"))
    
def sub_button():
    messagebox.showinfo("Success",f("{fvalue.get()}-{svalue.get()}"))
    
def mul_button():
    messagebox.showinfo("Success",f("{fvalue.get()}*{svalue.get()}"))

def div_button():
    messagebox.showinfo("Success",f("{fvalue.get()}/{svalue.get()}"))


tk.Button(text="+",font='Chiller 15 bold',command=add_button).place(x=150,y=200)
tk.Button(text="-",font='Chiller 15 bold',command=sub_button).place(x=180,y=230)
tk.Button(text="*",font='Chiller 15 bold',command=mul_button).place(x=210,y=260)
tk.Button(text="/",font='Chiller 15 bold',command=div_button).place(x=240,y=290)
