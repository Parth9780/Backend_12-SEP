import tkinter as tk
from tkinter import *
import sqlite3

r = tk.Tk()
r.title('Counting Seconds')
r.geometry("500x600")
r.config(bg="lightgray")
r.title("TkinterApp")

fvalue=tk.Label(text="First name: ",bg='Lightgray',fg='blue',font='Chiller 15 bold').grid(row=0,column=0)

lvalue=tk.Label(text="Last name: ",bg='Lightgray',fg='blue',font='Chiller 15 bold').grid(row=1,column=0)

city=tk.Label(text="Last name: ",bg='Lightgray',fg='blue',font='Chiller 15 bold').grid(row=1,column=0)


tk.Entry().grid(row=0,column=1)
tk.Entry().grid(row=1,column=1)
tk.Entry().grid(row=3,column=1)

conn = sqlite3.connect("tkinter")
"""conn.execute('''
            create table tkinter_from (
                
                First_name VARCHAR(50),
                Last_name VARCHAR(30),
                city VARCHAR(30)
            )
            
            ''')"""

def Mybutton():
    ins = '''
        insert into tkinter_app (First_name, Last_name, city) VALUES (fvalue,lvalue,city)
    '''
    print("Submit Suceefuly..!!")

tk.Button(text="Submit",font='Chiller 15 bold',command=Mybutton).place(x=200,y=250)

