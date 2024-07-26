# Write a Python program to read a file line by line and store it into a list

with open("MY_File.txt") as f:
    content_list = f.readlines()

# print the list
print(content_list)

# remove new line characters
content_list = [x.strip() for x in content_list]
print(content_list)