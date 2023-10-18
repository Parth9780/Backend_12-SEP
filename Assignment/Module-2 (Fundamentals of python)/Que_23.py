""" Write a Python function to insert a string in the middle of a string """

def middle(text1, text2):
    data = text1[:len(text1) // 2] + text2 + text1[(len(text1) // 2):]
    return data


string1 = input("Enter First String : ")
string2 = input("Enter Second String : ")

result_string = middle(string1, string2)
print(result_string)