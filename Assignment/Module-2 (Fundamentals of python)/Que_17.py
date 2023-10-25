"""Write a Python program to get a single string from two given strings, 
separated by a space and swap the first two characters of each string. """

def swap(string):
    
    # storing the first character
    start = string[0]
    
    # storing the last character
    end = string[-1]
    
    swapped_string = end + string[1:-1] + start
    print(swapped_string)

swap("Tops Tecnology")
