import sqlite3

def connect():
    conn=sqlite3.connect("books.db")
    cursor_object = conn.cursor()
    cursor_object.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
    conn.commit()
    conn.close()

connect()

def view_all():
    conn= sqlite3.connect("books.db")
    cursor_object = conn.cursor()
    cursor_object.execute("SELECT * FROM book")
    rows = cursor_object.fetchall()
    conn.commit()
    conn.close()
    return rows

def add_entry(title,year,author,isbn):
    conn=sqlite3.connect("books.db")
    cursor_object = conn.cursor()
    cursor_object.execute("INSERT INTO book VALUES (NULL, ?, ?, ?, ?)",(title,year,author,isbn))
    conn.commit()
    conn.close()

def search_entry(title="",year="",author="",isbn=""):
    conn=sqlite3.connect("books.db")
    cursor_object = conn.cursor()
    cursor_object.execute("SELECT * FROM book WHERE title=? OR year=? OR author=? OR isbn=?",(title,author,year,isbn))
    rows = cursor_object.fetchall()
    conn.commit()
    conn.close()
    return rows

def update_entry(id,title,author,year,isbn):
    conn=sqlite3.connect("books.db")
    cursor_object = conn.cursor()
    cursor_object.execute("UPDATE book SET title=?,author=?,year=?,isbn=? WHERE id=?",(title,author,year,isbn,id))
    conn.commit()
    conn.close()

def delete_entry(id):
    conn=sqlite3.connect("books.db")
    cursor_object = conn.cursor()
    cursor_object.execute("DELETE FROM book WHERE id=?",(id,))
    conn.commit()
    conn.close()