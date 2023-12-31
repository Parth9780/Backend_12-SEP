import Banker


"""print('operation Manu:')
ch = int(input('1) Withdraw Amount\n2) Deposit Amount\n3) View Balance\nEnter your operstion: '))"""

def Withdraw_Amount():
    account_no = int(input('Enter your account number :'))
    account_holder_name = input('Enter your name :')
    if account_no == Banker.customer_account_no or account_no == Banker.customer_name:
        withdraw = int(input('Enter your amount: '))
        withdraw_amount = Banker.opening_balance - withdraw
        if Banker.opening_balance > 2500 :
            print("Successful...")
            print('Account Balance :',withdraw_amount)
        else:
            print('Balance are not Available in your account....')

    elif account_no == Banker.customer_account_no1 or account_no == Banker.customer_name1:
        withdraw = int(input('Enter your amount: '))
        withdraw_amount = Banker.opening_balance1 - withdraw
        if Banker.opening_balance1 > 2500:
            print("Successful...")
            print('Account Balance :', withdraw_amount)
        else:
            print('Balance are not Available in your account....')

    elif account_no == Banker.customer_account_no2 or account_no == Banker.customer_name2:
        withdraw = int(input('Enter your amount: '))
        withdraw_amount = Banker.opening_balance2 - withdraw
        if Banker.opening_balance2 > 2500:
            print("Successful...")
            print('Account Balance :', withdraw_amount)
        else:
            print('Balance are not Available in your account....')

def Deposit_amount():
    account_no = int(input('Enter your account number :'))
    account_holder_name = input('Enter your name :')
    if account_no == Banker.customer_account_no or account_no == Banker.customer_name:
        Deposit = int(input('Enter your amount: '))
        Deposit_amount = Banker.opening_balance + Deposit
        print("Successful...")
        print('Total Amount: ', Deposit_amount)

    elif account_no == Banker.customer_account_no1 or account_no == Banker.customer_name1:
        Deposit = int(input('Enter your amount: '))
        Deposit_amount = Banker.opening_balance1 + Deposit
        print("Successful...")
        print('Total Amount: ', Deposit_amount)

    elif account_no == Banker.customer_account_no2 or account_no == Banker.customer_name2:
        Deposit = int(input('Enter your amount: '))
        Deposit_amount = Banker.opening_balance2 + Deposit
        print("Successful...")
        print('Total Amount: ', Deposit_amount)

def View_balance():
    account_no = int(input('Enter your account number :'))
    account_holder_name = input('Enter your name :')
    if account_no == Banker.customer_account_no or account_no == Banker.customer_name:
        print('Account Number :',account_no)
        print('Account Holder Name :',account_holder_name)
        print('Account Balance: ',Banker.opening_balance)

    elif account_no == Banker.customer_account_no1 or account_no == Banker.customer_name1:
        print('Account Number :', account_no)
        print('Account Holder Name :', account_holder_name)
        print('Account Balance: ', Banker.opening_balance1)

    elif account_no == Banker.customer_account_no2 or account_no == Banker.customer_name2:
        print('Account Number :', account_no)
        print('Account Holder Name :', account_holder_name)
        print('Account Balance: ', Banker.opening_balance2)
