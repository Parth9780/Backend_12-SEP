""" Write a Python program to count the number of strings where the string 
length is 2 or more and the first and last character are same from a given 
list of strings. """


def compare(a):
    ctr = 0
    for i in a:
        if len(i) > 2 and i[0] == i[-1]:
            ctr+= 1
    return ctr

a = ['abc', 'xyz', 'aba', '1221', 'aaa', 'asdasdsada']
for i in a:
    z = compare(a)

print(z)