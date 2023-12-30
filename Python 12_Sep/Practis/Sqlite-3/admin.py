import sqlite3
conn =sqlite3.connect("Advance_Python.db")

create_table_query = """
CREATE TABLE IF NOT EXISTS admin (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    password TEXT
);
"""
conn.execute(create_table_query)
print("\nAdmin Module")
print("1. Add Admin")
print("2. Login Admin")
print("3. View All Managers")
print("4. View All Medicine")
print("5. Exit")
choice = input("Enter your choice: ")

if choice == '1':
    username = input("Enter the username: ")
    password = input("Enter the password: ")

    add_admin_query = """
    INSERT INTO admin (username, password) VALUES (?, ?);
    """
    conn.execute(add_admin_query, (username, password))
    conn.commit()

    print("\nAdmin added successfully!")

elif choice == '2':
    # Implement login admin logic here
    username = input("Enter the username: ")
    password = input("Enter the password: ")

    login_admin_query = """
    SELECT * FROM admin WHERE username = ? AND password = ?;
    """
    result = conn.execute(login_admin_query, (username, password))

    if result.fetchone():
        print("\nLogin successful!")
    else:
        print("\nInvalid username or password!")
    pass

elif choice == '3':
    # Implement view all managers logic here
    view_all_managers_query = """
        SELECT * FROM admin;
        """
    result = conn.execute(view_all_managers_query)
    all_managers = result.fetchall()

    print("\nAll Managers:")
    for manager in all_managers:
            print(f"ID: {manager[0]}, Name: {manager[1]}, password: {manager[2]}")
    pass

elif choice == '4':
    # Implement view all medicine logic here
    view_all_medicine_query = """
        SELECT * FROM medicine;
        """
    result = conn.execute(view_all_medicine_query)
    all_medicine = result.fetchall()

    print("\nAll Medicine:")
    for medicine in all_medicine:
        print(f"ID: {medicine[0]}, Name: {medicine[1]}, Quantity: {medicine[2]}, Expiry Date: {medicine[3]}")
    pass

elif choice == '5':
    print("Exiting...")

else:
    print("Invalid Choice!")
    
conn.close()