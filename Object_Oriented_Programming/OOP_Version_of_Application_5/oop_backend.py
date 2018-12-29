import sqlite3

class Database:

    def __init__(self, db):
        self.conn=sqlite3.connect("books.db")
        self.cursor_object = self.conn.cursor()
        self.cursor_object.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
        self.conn.commit()

    def view_all(self):
        self.cursor_object.execute("SELECT * FROM book")
        rows = self.cursor_object.fetchall()
        return rows

    def add_entry(self, title, year, author, isbn):
        self.cursor_object.execute("INSERT INTO book VALUES (NULL, ?, ?, ?, ?)",(title, year, author, isbn))
        self.conn.commit()

    def search_entry(self, title="", year="", author="", isbn=""):
        self.cursor_object.execute("SELECT * FROM book WHERE title=? OR year=? OR author=? OR isbn=?", (title, author, year, isbn))
        rows = self.cursor_object.fetchall()
        return rows

    def update_entry(self, id, title, author, year, isbn):
        self.cursor_object.execute("UPDATE book SET title=?,author=?,year=?,isbn=? WHERE id=?",(title, author, year, isbn, id))
        self.conn.commit()

    def delete_entry(self, id):
        self.cursor_object.execute("DELETE FROM book WHERE id=?",(id,))
        self.conn.commit()

    def __del__(self):
        self.conn.close()