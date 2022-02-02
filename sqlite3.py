import sqlite3

#connect to database
conn = sqlite3.connect('customer.db')

# create a cursor
c = conn.cursor()

many_customers = [
					('wes', 'brown', 'wesbrown@mail.com'), 
					('brian', 'laundrie', 'conspiraxy@hoax.com'), 
					('ronald', 'reagan', 'well@rnc.biz')
				  ]

# create a table
c.executemany("INSERT INTO customer VALUES (?,?,?)", many_customers)

print("command successfully executed...")

conn.commit()

conn.close()