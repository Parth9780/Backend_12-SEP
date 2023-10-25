""" Write a Python program to get the Factorial number of given number. """

num = int(input("Enter the range of factorial: "))  # user input the number

factorial = 1   #initialise factorial variable value..

if num<0:   #check the first condition (true)
    print("The nagative number factorial is does not exist..!!")
elif num == 0:  #check the second condition (true)
    print("The factorial of 0 is 1")
else:   #condition is false
    for i in range(1,num + 1):
        factorial = factorial*i
    
    print("The Factorial is : ",factorial)  # print the output
