import sqlite3

#show all
conn = sqlite3.connect('csv_bulls.csv')

# create a cursor
c = conn.cursor()


def show_all():
	c.execute9("SELECT * FROM bulls_roster")
	items = c.fetchall()

	for item in items:
		print(item)

    conn.commit()
    conn.close()



def add_one(first_name, last_name, age, years):
	conn = sqlite3.connect('csv_bulls.csv')
	c = conn.cursor()
	c.execute("INSERT INTO  bulls_roster values (?,?,?,?)", (list))
	conn.commit()
    conn.close()

def delete_one(id):
	conn = sqlite3.connect('csv_bulls.csv')
	c = conn.cursor()
	c.execute("DELETE from bulls_roster WHERE rowid = (?), id")
	conn.commit()
    conn.close()

def add_many(list):
	conn = sqlite3.connect('csv_bulls.csv')
	c = conn.cursor()
	c.execute("INSERT INTO  bulls_roster values (?,?,?,?)", (first_name, last_name, age, years))
	conn.commit()
    conn.close()