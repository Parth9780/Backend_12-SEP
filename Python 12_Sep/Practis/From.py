fname = input("Enter First name: ")
lname = input("Enter Last name: ")

if fname.isalpha() and lname.isalpha():
    print("Looks good enter your username...")
    username = input("Enter Username:  ")
    
    if username.isalnum():
        print("Good Set your passworld")
        passworld = input("Enter your passworld: ")
        
        if passworld.isalnum():
            num =input("Enter the mobile number :")
            
            if num.isdigit() and len(num)==10:
                print("SUCCESS..")
            else:
                print("Plse! Enter valib number")
        else:
            print("Plse! Enter valid passworld....")
    else:
        print("Plz! enter valid Username....")
else:
    print("Plz! enter valid firstname and lastname....")
