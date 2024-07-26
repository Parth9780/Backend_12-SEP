import sqlite3

conn =sqlite3.connect("Mydatabase.db")
conn.execute('''
            create table Tution (
                st_id INT AUTO_INCREMENT PRIMARY KEY,
                st_name VARCHAR(50),
                st_cours VARCHAR(30),
                st_city VARCHAR(30)
            )
            
            ''')

conn.close()