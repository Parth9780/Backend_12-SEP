import sqlite3
from datetime import datetime

conn =sqlite3.connect("Pharmacy_Management.db")

create_table_query = """
CREATE TABLE IF NOT EXISTS Manager (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    Pharmacy_name TEXT
);
"""
conn.execute(create_table_query)


cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS medicine(
        id INTEGER PRIMARY KEY,
        name TEXT,
        quantity TEXT,
        added_date TEXT,
        added_by TEXT,
        price REAL
    )
''')
print("Table created successfully")
conn.close()

# Pharmacy Manager
#  Can Register 
#  Can Login 
#  Can Add Medicine
#  Can View Medicine 
#  Can Delete Medicine

def insert_medicine(name, quantity, added_by, price):
            conn = sqlite3.connect('Pharmacy_Management.db')
            cursor = conn.cursor()
            added_date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            cursor.execute('''
                INSERT INTO medicine(name, quantity, denomination, added_date, added_by, price) VALUES(?,?,?,?,?,?)
            ''', (name, quantity, added_date, added_by, price))
            conn.commit()
            
            print("Medicine added successfully")
            conn.close()


class Pharmacy_manager():
        
    def register():
        name = input("Enter the name: ")
        Pharmacy_name = input("Enter the Pharmacy_name: ")

        add_menager_query = """
        INSERT INTO menager (name, Pharmacy_name) VALUES (?, ?);
        """
        conn.execute(add_menager_query, (name, Pharmacy_name))
        conn.commit()

        print("\nManager added successfully!")
        
    def Login():
        name = input("Enter the name: ")
        Pharmacy_name = input("Enter the Pharmacy_name: ")

        login_menager_query = """
        SELECT * FROM menager WHERE name = ? AND Pharmacy_name = ?;
        """
        result = conn.execute(login_menager_query, (name, Pharmacy_name))

        if result.fetchone():
            print("\nLogin successful!")
        else:
            print("\nInvalid name or Pharmacy_name!")

    def Add_Medicine():
        name = input('Enter the medicion name :')
        quantity = input('Enter Quntity :')
        added_by =int(input("Enter By added :"))
        price = int(input('Enter Price :'))
        insert_medicine()
    
    def view_medicine():
            conn = sqlite3.connect('medicine.db')
            cursor = conn.cursor()
            cursor.execute('''
                SELECT * FROM medicine
            ''')
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            conn.close()

    def Delete_Medicine():
        conn = sqlite3.connect('Pharmacy_Management.db')
        cursor = conn.cursor()
        cursor.execute('''
            DELETE FROM medicine WHERE id=?
        ''', (id,))
        conn.commit()
        print("Medicine deleted successfully")
        conn.close()
    
