import random
import Banker
import datetime

import Customers

print("WELCOME TO PYTHON BANK MANAGMENT SYSTEM")
temp = 'y'

while temp == 'y':
    print()

    print('Select Your Roll : \n1.Banker\n2.Customer\n3.Exit')
    choose = int(input('Enter your Roall :-'))

    if choose == 1:
        print("Operations Menu")


        Banker.banker_input()
        print("Wellcom To banker's App")
        ch = int(input("Enter the operation which you perfrom :"))

        if ch == 1:
            Banker.Add_customer()
        elif ch == 2:
            Banker.View_Customer()
        elif ch == 3:
            Banker.Search_Customer()
        elif ch == 4:
            Banker.View_all_Customer()
        elif ch == 5:
            Banker.Total_Amount_Bank()


    elif choose == 2:
        print('operation Manu:')
        ch = int(input('1) Withdraw Amount\n2) Deposit Amount\n3) View Balance\nEnter your operstion: '))

        if ch == 1:
            Customers.Withdraw_Amount()
        elif ch == 2:
            Customers.Deposit_amount()
        elif ch == 3:
            Customers.View_balance()

    else:
        print('Thanyou For visiting Python Bank...')

    temp = input('Do you want to perform more operation press ''y'' for yes and press ''n'' for no :')
