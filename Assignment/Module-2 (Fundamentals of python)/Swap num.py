""" Write python program that swap two number with temp variable and without temp variable"""

print("1. Using temp variable...")

a = int(input("Enter the A number: "))  # user input the number
b = int(input("Enter the B number: "))  # user input the number

print("After swap number....")
print("a :",a)  #print the statement
print("b :",b)
            # a = 5, b = 8
temp = a    # 0 = 5
a = b       # a = 8
b = temp    # b = 5

print("Befor swap number....")  #print the statement
print("a :",a)
print("b :",b)

print("2. Whit out using temp variable...")

print("After swap number....")  #print the statement
print("a :",a)
print("b :",b)
                # a = 5, b = 8
a = a+b         # a = 5 + 8
b = a-b         # b = 13 - 8
a = a-b         # a = 13 - 5

print("Befor swap number....")  #print the statement
print("a :",a)
print("b :",b)