import sqlite3

conn = sqlite3.connect("Mydatabase.db")

conn.execute('''
            update Tution set st_name = 'Ram' where st_id = 3
            
            ''')
conn.commit()
conn.close()
