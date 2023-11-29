# Import the required libraries
from tkinter import *
from tkinter import messagebox 

# Create an instance of tkinter frame or window
win=Tk()

# Set the size of the tkinter window
win.geometry("700x350")

def cal_sum():
   t1=int(a.get())
   t2=int(b.get())
   sum=t1+t2
   label.config(text=sum)
   # messagebox.showinfo(f("Addition","{t1}+{t2}={sum}"))

def cal_sub():
   t1=int(a.get())
   t2=int(b.get())
   sum=t1-t2
   label.config(text=sum)
   # messagebox.showinfo("Subtriction",f("{t1}-{t2}={sum}"))


def cal_sub():
   t1=int(a.get())
   t2=int(b.get())
   sum=t1*t2
   label.config(text=sum)
   # messagebox.showinfo("multiplication",f("{t1}*{t2}={sum}"))


def cal_div():
   t1=int(a.get())
   t2=int(b.get())
   sum=t1/t2
   label.config(text=sum)
   # messagebox.showinfo("Division",f("{t1}/{t2}={sum}"))


# Create an Entry widget
t1=Label(win, text="Enter First Number", font=('Calibri 20'))
t1.pack()
a=Entry(win, font='Calibri 15', width=35)
a.pack()
t2=Label(win, text="Enter Second Number", font=('Calibri 20'))
t2.pack()
b=Entry(win, font='Calibri 15', width=35)
b.pack()

label=Label(win, text="Total Sum : ", font=('Calibri 20'))
label.pack(pady=20)

# Button(win, text="Calculate Sum", command=cal_sum).pack()
# Button(win, text="Calculate Sub", command=sub_sum).pack()
# Button(win, text="Calculate mul", command=mul_sum).pack()
# Button(win, text="Calculate div", command=div_sum).pack()

Button(win,text="Calculate Sum", font='Calibri 15', command=cal_sum).place(x=200,y=200)
Button(win,text="Calculate Sub", font='Calibri 15', command=sub_sum).place(x=350,y=200)
Button(win,text="Calculate mul", font='Calibri 15', command=mul_sum).place(x=200,y=270)
Button(win,text="Calculate div", font='Calibri 15', command=div_sum).place(x=350,y=270)
win.mainloop()
