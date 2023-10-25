# Write a Python program to convert a tuple to a string. 

def convertTuple(tup):
        # initialize an empty string
    str = ''
    for item in tup:
        str = str + item
    return str

tuple = ('k', 'p', '_', 'p', 'a', 't', 'e', 'l', '9', '5', '_')
str = convertTuple(tuple)
print(str)