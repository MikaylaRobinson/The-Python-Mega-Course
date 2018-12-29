import psycopg2

# Creating a table in our database
def create_table():
    conn= psycopg2.connect("dbname='database1' user='postgres' password='' host='localhost' port='5432'")
    cursor_object = conn.cursor()
    cursor_object.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()
# Example using this function: create_table()

# Function for inserting data into the table
def insert(item,quantity,price):
    conn= psycopg2.connect("dbname='database1' user='postgres' password='' host='localhost' port='5432'")
    cursor_object = conn.cursor()
    cursor_object.execute("INSERT INTO store VALUES (%s, %s, %s)",(item,quantity,price))
    conn.commit()
    conn.close()
# Example of using this function: insert("Orange",10,5)

# Function for viewing the data from our database
def view():
    conn= psycopg2.connect("dbname='database1' user='postgres' password='' host='localhost' port='5432'")
    cursor_object = conn.cursor()
    cursor_object.execute("SELECT * FROM store")
    rows= cursor_object.fetchall()
    conn.close()
    return rows
#Example using this function: 
print(view())

# Deleting from the SQLite records
def delete(item):
    conn= psycopg2.connect("dbname='database1' user='postgres' password='' host='localhost' port='5432'")
    cursor_object = conn.cursor()
    cursor_object.execute("DELETE FROM store WHERE item=%s",(item,))
    conn.commit()
    conn.close()
# Example of using this function: delete("Orange")

# Updating data
def update(quantity,price,item):
    conn= psycopg2.connect("dbname='database1' user='postgres' password='' host='localhost' port='5432'")
    cursor_object = conn.cursor()
    cursor_object.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s",(quantity,price,item))
    conn.commit()
    conn.close()
# Example of using this function: update(20,15.0,"Apple")