import sqlite3

# Creating a table in our database
def create_table():
    conn= sqlite3.connect("lite.db")
    cursor_object = conn.cursor()
    cursor_object.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

# Function for inserting data into the table
def insert(item,quantity,price):
    conn= sqlite3.connect("lite.db")
    cursor_object = conn.cursor()
    cursor_object.execute("INSERT INTO store VALUES (?,?,?)",(item,quantity,price))
    conn.commit()
    conn.close()
# Example of using this function: insert("Coffee Cup",10,5)

# Function for viewing the data from our database
def view():
    conn= sqlite3.connect("lite.db")
    cursor_object = conn.cursor()
    cursor_object.execute("SELECT * FROM store")
    rows= cursor_object.fetchall()
    conn.close()
    return rows

# Deleting from the SQLite records
def delete(item):
    conn= sqlite3.connect("lite.db")
    cursor_object = conn.cursor()
    cursor_object.execute("DELETE FROM store WHERE item=?",(item,))
    conn.commit()
    conn.close()
# Example of using this function: delete("Wine Glass")

# Updating data
def update(quantity,price,item):
    conn= sqlite3.connect("lite.db")
    cursor_object = conn.cursor()
    cursor_object.execute("UPDATE store SET quantity=?, price=? WHERE item=?",(quantity,price,item))
    conn.commit()
    conn.close()
# Example of using this function: update(11,6,"Water Glass")

print(view())