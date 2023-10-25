import random
import datetime



def banker_input():
    print("1).Add Customer")
    print("2).View Customer")
    print("3).Search Customer")
    print("4).View all Customer")
    print("5).Total Amount in Bank")
    
def Add_customer():
    customer_name = input("Enter the Customer Name: ")
    customer_account_no = random.randrange(1000000000, 9999999999)
    customer_age = input("Enter Customer age: ")
    type = input("Ex 1.saving\n2.current\n Enter Account Type: ")
    if type=='saving' :
            Account_type = ('saving')
    elif type=='current' :
            Account_type = ('current')
    print("Minimum account blance is 2500 compulsory")
    opening_balance = input("Enter the opening blance: ")
    opening_date = datetime.datetime.now()
    print("\n\n\n")
    print("Name: ",customer_name)
    print("Account_no: ",customer_account_no)
    print("Age: ",customer_age)
    print("Opening Date: ",opening_date)
    
    filename = customer_name + '.txt'
    with open(filename, 'w') as file:
        file.write('Name: {}\n'.format(customer_name))
        file.write('Account_Number: {}\n'.format(customer_account_no)) 
        file.write('Age: {}\n'.format(customer_age))
        file.write('Opening Date: {}\n'.format(opening_date))
        file.write('Balance: {}\n'.format(opening_balance))
        


def View_Customer():
    View = {
        "name" : customer_name,
        "Account_number":customer_account_no,
        "Blance": opening_balance,
        "Opening_date":opening_date,
    }
    print(View)
