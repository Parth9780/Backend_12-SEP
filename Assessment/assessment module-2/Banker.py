import random
import datetime


customer_name = 'Parth Kavathiya'
customer_account_no = 101
customer_age = 19
Account_type = 'saving'
x = datetime.datetime.now()
opening_date = x
opening_balance = 15000

with open("Customer.txt", 'a') as file:
    file.write('Name: {}\n'.format(customer_name))
    file.write('Account_Number: {}\n'.format(customer_account_no))
    file.write('Age: {}\n'.format(customer_age))
    file.write('Opening Date: {}\n'.format(opening_date))
    file.write('Balance: {}\n'.format(opening_balance))



customer_name1 = 'Yash savaliya'
customer_account_no1 = 102
customer_age1 = 18
Account_type1 = 'saving'
opening_date1 = '2022-09-28 26:26:60.38153'
opening_balance1 = 35000

with open("Customer.txt", 'a') as file:
    file.write('Name: {}\n'.format(customer_name1))
    file.write('Account_Number: {}\n'.format(customer_account_no1))
    file.write('Age: {}\n'.format(customer_age1))
    file.write('Opening Date: {}\n'.format(opening_date1))
    file.write('Balance: {}\n'.format(opening_balance1))


customer_name2 = 'Navil Desai'
customer_account_no2 = 101
customer_age2 = 18
Account_type2 = 'saving'
y = datetime.datetime.now()
opening_date2 = y
opening_balance2 = 26500

with open("Customer.txt", 'a') as file:
    file.write('Name: {}\n'.format(customer_name2))
    file.write('Account_Number: {}\n'.format(customer_account_no2))
    file.write('Age: {}\n'.format(customer_age2))
    file.write('Opening Date: {}\n'.format(opening_date2))
    file.write('Balance: {}\n'.format(opening_balance2))



def banker_input():
    print("1).Add Customer")
    print("2).View Customer")
    print("3).Search Customer")
    print("4).View all Customer")
    print("5).Total Amount in Bank")
    
def Add_customer():
    customer_name3 = input("Enter the Customer Name: ")
    customer_account_no3 = random.randrange(1000000000, 9999999999)
    customer_age3 = input("Enter Customer age: ")
    type = input("Ex 1.saving\n2.current\n Enter Account Type: ")
    if type == 'saving':
            Account_type3 = ('saving')
    elif type == 'current':
            Account_type3 = ('current')
    print("Minimum account blance is 2500 compulsory")
    opening_balance3 = input("Enter the opening blance: ")
    opening_date3 = datetime.datetime.now()
    print("\n\n\n")
    print("Name: ", customer_name3)
    print("Account_no: ", customer_account_no3)
    print("Age: ", customer_age3)
    print("Opening Date: ", opening_date3)
    
    filename = customer_name + '.txt'
    with open("Customer.txt", 'a') as file:
        file.write('Name: {}\n'.format(customer_name3))
        file.write('Account_Number: {}\n'.format(customer_account_no3))
        file.write('Age: {}\n'.format(customer_age3))
        file.write('Opening Date: {}\n'.format(opening_date3))
        file.write('Balance: {}\n'.format(opening_balance3))
        


def View_Customer():
    View = {
        "name" : customer_name,
        "Account_number":customer_account_no,
        "Blance": opening_balance,
        "Opening_date":opening_date,
    }
    print(View)



def Search_Customer():
    account_no = int(input("Enter the Account Number: "))
    account_holder_name = input("Enter the Account Holder Name: ")
    if account_no == customer_account_no or account_holder_name == customer_name:
        View = {
            "name": customer_name,
            "Account_number": customer_account_no,
            "Blance": opening_balance,
            "Opening_date": opening_date,
        }
        print(View)
    else:
        print('This customer are not exist in the banke......')



def View_all_Customer():
    View = {
        "name": customer_name,
        "Account_number": customer_account_no,
        "Blance": opening_balance,
        "Opening_date": opening_date,
    }
    print(View)
    View1 = {
        "name": customer_name1,
        "Account_number": customer_account_no1,
        "Blance": opening_balance1,
        "Opening_date": opening_date1,
    }
    print(View1)
    View2 = {
        "name": customer_name2,
        "Account_number": customer_account_no2,
        "Blance": opening_balance2,
        "Opening_date": opening_date2,
    }
    print(View2)



def Total_Amount_Bank():
    Total_Amount = opening_balance + opening_balance1 + opening_balance2
    print("The Total Blance in Bank is :", Total_Amount)

