import sqlite3

#connect to database
conn = sqlite3.connect('customer.db')

# create a cursor
c = conn.cursor()


c.execute("INSERT INTO customers VALUES ('Poop', Turd', 'shit@shart.')")

print("command executed successfully...")

conn.commit()

conn.close()