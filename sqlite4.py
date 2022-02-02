import sqlite3

#connect to database
conn = sqlite3.connect('customer.db')

# create a cursor
c = conn.cursor()

# query the database
c.execute9("SELECT * FROM customers")
c#.fetchone()
#c.fetchmany(3)
print(c.fetchall())

print("command successfully executed...")

conn.commit()

conn.close()