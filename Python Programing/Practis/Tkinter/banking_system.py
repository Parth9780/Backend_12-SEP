import random


random.seed(10)
account_no=random.randrange(1000000000, 9999999999)
account_holder_name=input("enter the your name: ")
type = input("1.saving\n2.current\nplase enter the account type: ")
if type=='saving' :
    Account_type = ('saving')
elif type=='current' :
    Account_type = ('current')

print("Minimum account blance is 2500 compulsory")
Deposit_amount = int(input("How many amount Deposited: "))
account_balance = Deposit_amount

x=input("How can your withdrw amount------ \t yes -- no ")

if x=='yes':
    Withdrwan_amount = int(input("Enter the ammount of withdrw :"))
    if Withdrwan_amount>2500 or 0<Withdrwan_amount:
        account_balance=account_balance-Withdrwan_amount
        print("Withdrw successful")
    else:
        print("Your balance is not avalable...")

print('----------your account Statement------------')
print('Your account number is: ',account_no)
print('account holder name is :',account_holder_name)
print('account type is : ',Account_type)
print("account Balance :",account_balance)
