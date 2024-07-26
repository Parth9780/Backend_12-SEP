import sqlite3

conn = sqlite3.connect("Mydatabase.db")

data=conn.execute("SELECT * FROM Tution")
for n in data:
    print(n)

"""
# limit using for SELECT
data=conn.execute("SELECT * FROM Tution limit 1,3")
for n in data:
    print(n)

"""