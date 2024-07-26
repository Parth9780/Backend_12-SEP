import sqlite3
from sqlite3 import Error


class Admin:
    conn =sqlite3.connect("Pharmacy_Management.db")

    def create_connection(self):
        try:
            conn =sqlite3.connect("Pharmacy_Management.db")

            create_table_query = """
                                CREATE TABLE IF NOT EXISTS admin (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    username TEXT,
                                    password TEXT
                                );
                                """
                                
            if self.conn is not None:
                self.conn.execute(create_table_query)
            else:
                print("Error! cannot create the database connection.")
        except Error as e:
                print(e)

    def register(self):
        conn =sqlite3.connect("Pharmacy_Management.db")
        
        username = input("Enter the username: ")
        password = input("Enter the password: ")

        add_admin_query = """
        INSERT INTO admin (username, password) VALUES (?, ?);
        """
        conn.execute(add_admin_query, (username, password))
        conn.commit()

        print("\nAdmin added successfully!")
    
    def Login(self):
        conn =sqlite3.connect("Pharmacy_Management.db")
        
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
        
    def View_manager(self):
        conn =sqlite3.connect("Pharmacy_Management.db")
        
        view_all_managers_query = """
            SELECT * FROM admin;
            """
        result = conn.execute(view_all_managers_query)
        all_managers = result.fetchall()

        print("\nAll Managers:")
        for manager in all_managers:
                print(f"ID: {manager[0]}, Name: {manager[1]}, Pharmacy_name: {manager[2]}")

    def View_Medicine(self):
        conn =sqlite3.connect("Pharmacy_Management.db")
    
        conn = sqlite3.connect('medicine.db')
        cursor = conn.cursor()
        cursor.execute('''
            SELECT * FROM medicine
        ''')
        rows = cursor.fetchall()
        for row in rows:
            print(row)
            conn.close()


ad = Admin()
