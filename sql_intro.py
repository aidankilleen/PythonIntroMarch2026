# sql_intro.py

# structured query language (SQL)

import sqlite3

filename = "C:\\work\\training\\databases\\userdb.db"

conn = sqlite3.connect(filename)

# Create 
sql = """INSERT INTO users 
            (name, email, active) 
            VALUES('New User','nu@gmail.com',1)"""

conn.execute(sql)
conn.commit()

# Update
sql = """UPDATE users
        SET name = 'changed', email='changed@gmail.com', active=0
        WHERE id = 29"""
conn.execute(sql)
conn.commit()

#Delete
sql = """DELETE FROM users WHERE name = 'New User'"""
conn.execute(sql)
conn.commit()

# Retrieve
sql = "SELECT * FROM users"

cur = conn.execute(sql)

print (f"ID\t{"Name":16}\t{"Email":16}\t{"Active"}")
for rec in cur:
    id, name, email, active = rec
    print (f"{id}\t{name:16}\t{email:16}\t{"Active" if active else "Inactive"}")


# CRUD
# Create
# Retrieve
# Update
# Delete



conn.close()




