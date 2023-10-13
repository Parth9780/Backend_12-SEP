""" Write a Python program to get the Fibonacci series of given range."""

range = int(input("Enter the range of fibonacci series..: "))   # user input the number
n1 = 0  #initialise variable value..
n2 = 1  #initialise variable value..

count = 0   #initialise variable value..

if range <= 0:  #check the first condition (true)
    print("Plase Enter the valid number........")
else:   #condition is false
    print("...........Fibonacci serice...........")
    
    while count < range:
        print(n1)
        temp = n1 + n2  # 0 = 1 + 2
        n1 = n2         # 1 = 2
        n2 = temp       # 2 = 3
        count += 1
