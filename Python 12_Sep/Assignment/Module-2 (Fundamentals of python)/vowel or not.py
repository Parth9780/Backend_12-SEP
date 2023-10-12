""" Write a Python program to test whether a passed letter is a vowel or not."""

ch = input("Enter the letter :")

if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
    print(ch,"this is vowel")
elif ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U':
    print(ch,"This is VOWEL")
else:
    print(ch,"is the Consonant")
