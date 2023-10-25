""" Write python program that swap two number with temp variable and without temp variable"""

print("1. Using temp variable...")

a = int(input("Enter the A number: "))
b = int(input("Enter the B number: "))

print("After swap number....")
print("a :",a)
print("b :",b)

temp = a
a = b
b = temp

print("Befor swap number....")
print("a :",a)
print("b :",b)

print("2. Whit out using temp variable...")

print("After swap number....")
print("a :",a)
print("b :",b)

a = a+b
b = a-b
a = a-b

print("Befor swap number....")
print("a :",a)
print("b :",b)