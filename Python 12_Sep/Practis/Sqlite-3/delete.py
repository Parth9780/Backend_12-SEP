import sqlite3

conn = sqlite3.connect("Mydatabase.db")

st_id = input("Enter the ID: ")
conn.execute("DELETE FROM Tution where st_id = "+st_id)
conn.commit()
conn.close()