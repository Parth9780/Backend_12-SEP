# Explain Exception handling? What is an Error in Python?

"""
--> An error is an issue in a program that prevents the program from completing its task.
--> In comparison, an exception is a condition that interrupts the normal flow of the program.
--> Both errors and exceptions are a type of runtime error, which means they occur during the execution of a program.
"""

while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")

