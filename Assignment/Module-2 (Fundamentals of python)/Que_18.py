<<<<<<< HEAD:Python 12_Sep/Assignment/Module-2 (Fundamentals of python)/Que_18.py
""" Write a Python program to add 'ing' at the end of a given string (length 
should be at least 3). If the given string already ends with 'ing' then add 
'ly' instead if the string length of the given string is less than 3, leave it 
unchanged. """

str = input('Enter the String :')

if len(str) < 3:
    print(str)
elif str[-3:] == 'ing':
    print(str + 'ly')
else:
=======
""" Write a Python program to add 'ing' at the end of a given string (length 
should be at least 3). If the given string already ends with 'ing' then add 
'ly' instead if the string length of the given string is less than 3, leave it 
unchanged. """

str = input('Enter the String :')

if len(str) < 3:
    print(str)
elif str[-3:] == 'ing':
    print(str + 'ly')
else:
>>>>>>> 80c6c9d626d696772149a7b8dda5a88e926ca214:Assignment/Module-2 (Fundamentals of python)/Que_18.py
    print(str + 'ing')