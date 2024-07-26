""" Write a Python program to check if a number is positive, negative or zero. """

n = int(input("Enter the any number: "))    # user input the number

if n>0: #check the first condition (true)
    print(n,"This is Positive number...")
elif n<0:   #check the second condition (true)
    print(n,"this is negative number...")
else: #condition is false
    print(n,"This is Zero...!")
