import random

print("Welcome to python authantication system...")


def signup():
    try:
        name = input('Enter your name: ')
        city = input('Enter your city: ')
        mobile = int(input('Enter your mobile number: '))
        id = int(input('Enter your id: '))
        
    except:
        print('Error..')
    print('Your id is: ',id)
    
    fl = open('UserData.txt','a') 
    fl.write(f"ID: {id}\nName: {name}\nCity: {city}\n Mobile No: {mobile}")

def login():
    try:
        x = int(input('Enter your id :'))
        y = input('Enter your name: ')
    except:
        print('Error')
    
    with open('UserData.txt', 'r') as fl:
        data = fl.read()
        
    if x or y in data:
        print('Login sucessfuly...')
    else:
        print('Your id and name is not match..!')

n = 'y'

while n == 'y':
    ch = int(input('1) Signup\n2) Login\n3) Exit\nEnter your choice: '))

    if ch == 1:
        signup()
    elif ch == 2:
        login()
    else:
        print('Thankyou')
        
    
    n = input('Do You Perform any operation y = yes and n = no: ')
