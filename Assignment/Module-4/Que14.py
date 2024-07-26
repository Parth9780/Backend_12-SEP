# How many except statements can a try-except block have? Name Some built-in exception classes:
"""
--> the alwase a try and except block have at least one except statement.
note: At least one except statement is requerd.

try:
    # Some Code.... 
except:
    # optional block
    # Handling of exception (if required)
else:
    # execute if no exception
finally:
    # Some code .....(always executed)

--> the one of the used the except key word to used else, and finally key word in file handling concept.
"""

def divide(x, y): 
    try: 
        result = x // y 
        print("Yeah ! Your answer is :", result) 
    except ZeroDivisionError: 
        print("Sorry ! You are dividing by zero ")

divide(20,30)