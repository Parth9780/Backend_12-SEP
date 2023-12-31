# from Admin import *
import Admin
from Pharmacy_Manager import *
import sqlite3

conn =sqlite3.connect("Pharmacy_Management.db")
print("___________Wellcome To Pharmacy Management System___________")


choice = input('1.Admin\n2.Manager\nEnter Your Roll :')

if choice == '1':
    if choice == '1':
      pass
    elif choice == '2':
        Admin.register()
    elif choice == '3':
                view_all_manager()
    elif choice == '4':
                view_medicine()
    elif choice == '5':
                break
    else:
        print("Invalid Choice!")

elif choice == '2':
    while True:
        print("\nPharmacy Manager Module")
        print("1. Add Pharmacy Manager")
        print("2. Login Pharmacy Manager")
        print("3. Add Medicine")
        print("4. View Medicine")
        print("5. Delete Medicine")
        print("6. Back to Main Menu")
        choice = input("")