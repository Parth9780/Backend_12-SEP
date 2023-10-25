""" Write a Python program to find whether a given number is even or odd, 
print out an appropriate message to the user."""

num = int(input("Enter the any number: "))      # user input the number

if num % 2 == 0:       #check the first condition (true)
    print(num,"is a Even number.......")
else:                   #condition is false
    print(num,"is a Odd number.......")
