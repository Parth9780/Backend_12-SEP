import sqlite3
from tkinter import *  
base = Tk()  
base.geometry("500x500")  
base.title("registration form")  

lb1= Label(base, text="Enter Name", width=10, font=("arial",12))  
lb1.place(x=20, y=120)  
en1= Entry(base)  
en1.place(x=200, y=120)  

lb3= Label(base, text="Enter Email", width=10, font=("arial",12))  
lb3.place(x=19, y=160)  
en3= Entry(base)  
en3.place(x=200, y=160)  

lb4= Label(base, text="Contact Number", width=13,font=("arial",12))  
lb4.place(x=19, y=200)  
en4= Entry(base)  
en4.place(x=200, y=200)  

lb6= Label(base, text="Enter Password", width=13,font=("arial",12))  
lb6.place(x=5, y=240)  
en6= Entry(base, show='*')  
en6.place(x=200,y=240)  

lb7= Label(base, text="Re-Enter Password", width=15,font=("arial",12))  
lb7.place(x=14,y=280)  
en7 =Entry(base, show='*')  
en7.place(x=200, y=280)  

conn = sqlite3.connect("Tkinter_From")
conn.execute('''
            create table tkinter_from (
                
                Name VARCHAR(50),
                Email VARCHAR(50),
                Number VARCHAR(30),
                Password VARCHAR(30)
            )
            
            ''')

def Mybutton():
    ins = '''
        insert into tkinter_app (Name, Email, Number, Password) VALUES (en1,en3,en4,en6)
    '''
    print("Submit Suceefuly..!!")

Button(base, text="Register", width=10, command=Mybutton).place(x=200,y=400)  
base.mainloop()  