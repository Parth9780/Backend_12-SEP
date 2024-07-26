
def new_file():

    k=open('new.txt','a')
    n = int(input("Enter the number of student :"))
    for i in range(n):
        id=input("Enter your id: ")
        name = input("Enter your name: ")

    k.write(f"ID:{id}\nNAME:{name}\n")

new_file()