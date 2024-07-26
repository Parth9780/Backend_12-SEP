import sqlite3

conn = sqlite3.connect("Mydatabase.db")
ins = '''
    insert into tution (st_name, st_cours, st_city) VALUES ('ROHIT', 'PHP', 'GONDAL')
'''

conn.execute(ins)
conn.commit()
conn.close()