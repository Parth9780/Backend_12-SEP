import admin
import Pharmacy_Manager
import sqlite3


print('____________________WELLCOME TO PHARMACY MANAGEMENT SYSTEM____________________')
choice = input("1.Admin\n2.Manager\nEnter Your Roll.. :")

if choice == '1':
    ch = input('1. Can register\n2. Can Login\n3. Can Ciew all manager\n4. Can View all medicine\nEnter the any option: ')
    if ch == '1':
        admin.ad.register()
    elif ch == '2':
        admin.ad.Login()
    elif ch == '3':
        admin.ad.View_manager()
    elif ch == '4':
        admin.ad.View_Medicine()
    else:
        print("Invalide Opstion..")
elif choice == '2':
    ch = input('1. Can register\n2. Can Login\n3. Can Add Medicine\n4. Can View all medicine\n\5. Can Delete Medicinen\nEnter the any option: ')
    if ch == '1':
        Pharmacy_Manager.py.register()
    elif ch == '2':
        Pharmacy_Manager.py.Login()
    elif ch == '3':
        Pharmacy_Manager.py.Add_Medicine()
    elif ch == '4':
        Pharmacy_Manager.py.view_medicine()
    elif ch == '5':
        Pharmacy_Manager.py.Delete_Medicine()
    else:
        print("Invalide Opstion..")