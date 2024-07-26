import sqlite3
from datetime import datetime

choice = input('1.add_medicin\n2.view medicin\nEnter your Choice :')

def create_table():
    conn = sqlite3.connect('medicine.db')
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

if choice == '1':
    
    name = input('Enter the medicion name :')
    quantity = input('Enter Quntity :')
    denomination = input('Enter denomination: ')
    added_by =int(input("Enter By added :"))
    price = int(input('Enter Price :'))
    def insert_medicine(name, quantity, denomination, added_by, price):
        conn = sqlite3.connect('medicine.db')
        cursor = conn.cursor()
        added_date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        cursor.execute('''
            INSERT INTO medicine(name, quantity, denomination, added_date, added_by, price) VALUES(?,?,?,?,?,?)
        ''', (name, quantity, denomination, added_date, added_by, price))
        conn.commit()
        
        print("Medicine added successfully")
        conn.close()
    insert_medicine(name, quantity, denomination, added_by, price)
elif choice == '2':
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
    view_medicine()