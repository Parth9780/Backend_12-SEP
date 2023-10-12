""" Write a Python program to get the Fibonacci series of given range."""

range = int(input("Enter the range of fibonacci series..: "))
n1 = 0
n2 = 1

count = 0

if range <= 0:
    print("Plase Enter the valid number........")
else:
    print("...........Fibonacci serice...........")
    
    while count < range:
        print(n1)
        temp = n1 + n2
        n1 = n2
        n2 = temp
        count += 1
