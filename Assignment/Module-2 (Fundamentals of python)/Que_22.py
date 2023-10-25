<<<<<<< HEAD:Python 12_Sep/Assignment/Module-2 (Fundamentals of python)/Que_22.py
""" Write a Python program to get a string made of the first 2 and the last 
2 chars from a given a string. If the string length is less than 2, return 
instead of the empty string. """

string=input("Enter string:")
count=0
for i in string:
    count=count+1
new=string[0:2]+string[count-2:count]
print("Newly formed string is:")
=======
""" Write a Python program to get a string made of the first 2 and the last 
2 chars from a given a string. If the string length is less than 2, return 
instead of the empty string. """

string=input("Enter string:")
count=0
for i in string:
    count=count+1
new=string[0:2]+string[count-2:count]
print("Newly formed string is:")
>>>>>>> 80c6c9d626d696772149a7b8dda5a88e926ca214:Assignment/Module-2 (Fundamentals of python)/Que_22.py
print(new)