<<<<<<< HEAD:Python 12_Sep/Assignment/Module-2 (Fundamentals of python)/Que_10.py
""" Write a Python program that will return true if the two given integer 
values are equal or their sum or difference is 5."""

def test_number5(x, y):
    if x == y or abs(x-y) == 5 or (x+y) == 5:
        return True
    else:
        return False

print(test_number5(7, 2))
print(test_number5(4, 2))
print(test_number5(2, 2))
print(test_number5(7, 3))
=======
""" Write a Python program that will return true if the two given integer 
values are equal or their sum or difference is 5."""

def test_number5(x, y):
    if x == y or abs(x-y) == 5 or (x+y) == 5:
        return True
    else:
        return False

print(test_number5(7, 2))
print(test_number5(4, 2))
print(test_number5(2, 2))
print(test_number5(7, 3))
>>>>>>> 80c6c9d626d696772149a7b8dda5a88e926ca214:Assignment/Module-2 (Fundamentals of python)/Que_10.py
print(test_number5(27, 53))