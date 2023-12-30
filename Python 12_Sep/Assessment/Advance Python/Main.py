# from Admin import *
import Admin
from Pharmacy_Manager import *
import sqlite3

conn =sqlite3.connect("Pharmacy_Management.db")
print("___________Wellcome To Pharmacy Management System___________")


ch = input('1.Admin\n2.Manager\nEnter Your Roll :')

if ch == '1':
    list = print('1.Can Register\n2.Can Login\n3.Can View all manager\n4.Can View Medicine')
    Achoice = int(input('Enter Your Choice :'))
    if Achoice == '1':
        Admin.register()
        print("Register")
        pass
    elif Achoice == '2':
        Admin.Login()
        pass
    elif Achoice == '3':
        Admin.View_manager()
        pass
    elif Achoice == '4':
        Admin.View_Medicine()
        pass
    else:
        print('Invalid Choice...')
        
elif ch == '2':
    list = print('1.Can Register\n2.Can Login\n3.Can Add Medicien\n4.Can View Medicine\n5.Can Delete Medicine')
    choice = int(input('Enter Your Choice :'))