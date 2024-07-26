# Write a Python program to append text to a file and display the text.

with open("MY_File.txt", "a") as fl:
    fl.write("Hello \n")
    fl.write("World \n")
    fl.write("..............!!!")
