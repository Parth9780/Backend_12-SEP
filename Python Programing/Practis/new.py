import sqlite3
if conn.is_connected():
    print('Successfully Connected to MySQL Database')
    cursor = conn.cursor()
    cursor.execute("USE pharmacy_db")
    
choice = input("1.Admin\n2.Parmacy-manager\nEnter the Choice: ")
if choice == '1':
        while True:
            print("\nAdmin Module")
            print("1. Add Admin")
            print("2. Login Admin")
            print("3. View All Managers")
            print("4. View All Medicine")
            print("5. Back to Main Menu")
            choice = input("Enter your choice: ")

            if choice == '1':
                add_admin()
            elif choice == '2':
                username = input("Enter admin username: ")
                password = input("Enter admin password: ")
                sql_query = """SELECT * FROM admin WHERE username = %s AND password = %s"""
                cursor.execute(sql_query, (username, password))
                records = cursor.fetchall()
                if len(records) > 0:
                    print("Admin Logged In Successfully!")
                else:
                    print("Invalid Username or Password!")
            elif choice == '3':
                view_all_manager()
            elif choice == '4':
                view_medicine()
            elif choice == '5':
                break
            else:
                print("Invalid Choice!")

elif choice == '2':
    while True:
        print("\nPharmacy Manager Module")
        print("1. Add Pharmacy Manager")
        print("2. Login Pharmacy Manager")
        print("3. Add Medicine")
        print("4. View Medicine")
        print("5. Delete Medicine")
        print("6. Back to Main Menu")
        choice = input("")