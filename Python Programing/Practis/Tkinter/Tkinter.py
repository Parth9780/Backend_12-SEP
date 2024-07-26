import tkinter
from tkinter import *


sc=tkinter.Tk()
sc.geometry("500x600")
sc.config(bg="lightgray")
sc.title("TkinterApp")

tkinter.Label(text="First name: ",bg='Lightgray',fg='blue',font='Chiller 15 bold').grid(row=0,column=0)

tkinter.Label(text="Last name: ",bg='Lightgray',fg='blue',font='Chiller 15 bold').grid(row=1,column=0)

tkinter.Entry().grid(row=0,column=1)
tkinter.Entry().grid(row=1,column=1)

tkinter.Radiobutton(value=0,text='Male',bg='Lightgray',fg='blue',font='Chiller 15 bold').grid(row=2,column=0)
tkinter.Radiobutton(value=1,text='Female',bg='Lightgray',fg='blue',font='Chiller 15 bold').grid(row=2,column=1)

tkinter.Checkbutton(text="Gujrati",bg='Lightgray',fg='blue',font='Chiller 15 bold').grid(row=3,column=0)
tkinter.Checkbutton(text="Hindi",bg='Lightgray',fg='blue',font='Chiller 15 bold').grid(row=4,column=0)
tkinter.Checkbutton(text="English",bg='Lightgray',fg='blue',font='Chiller 15 bold').grid(row=5,column=0)

def Mybutton():
    print("Submit Suceefuly..!!")

tkinter.Button(text="Submit",font='Chiller 15 bold',command=Mybutton).place(x=200,y=250)

