"""Write a Python program to sum of three given integers. However, if 
two values are equal sum will be zero"""

def sum_three(x, y, z):
    if x == y or y == z or x==z:
        sum = 0
    else:
        sum = x + y + z
    return sum

a = int(input("Enter the number: "))
b = int(input("Enter the number: "))
c = int(input("Enter the number: "))

print(sum_three(a,b,c))
