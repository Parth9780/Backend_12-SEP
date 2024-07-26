# Can one block of except statements handle multiple exception?

# Yes, a single block of except statements in Python can handle multiple exceptions. This feature allows you to handle different types of exceptions using a single block of code.

try:
    k = 5//0 # raises divide by zero exception.
    print(k)

# handles zerodivision exception    
except ZeroDivisionError:   
    print("Can't divide by zero")
    
