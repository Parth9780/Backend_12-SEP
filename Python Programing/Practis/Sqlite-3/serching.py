import sqlite3

conn = sqlite3.connect("Mydatabase.db")

data=conn.execute("SELECT * FROM Tution where st_name = 'PARTH'")
for n in data:
    print(n)