import random
import Banker
import datetime



print("Operations Menu")


Banker.banker_input()
print("Wellcom To banker's App")
ch = int(input("Enter the operation which you perfrom :"))

if ch==1:
    Banker.Add_customer()
elif ch==2:
    Banker.View_Customer()