import sqlite3 

def connect():
	conn=sqlite3.connect("books.db")
	curr=conn.cursor()
	curr.execute("CREATE TABLE IF NOT EXISTS book (id  INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
	conn.commit()
	conn.close()

def insert(title, author, year, isbn):
	conn=sqlite3.connect("books.db")
	curr=conn.cursor()
	curr.execute("INSERT INTO book VALUES (NULL, ?,?,?,?)", (title, author,year,isbn))
	conn.commit()
	conn.close()

def view():
	conn=sqlite3.connect("books.db")
	curr=conn.cursor()
	curr.execute("SELECT * FROM book")
	rows=curr.fetchall()
	conn.close()
	return rows


def search(title="", author="", year="", isbn=""):
	conn=sqlite3.connect("books.db")
	curr=conn.cursor()
	curr.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?", (title,author,year,isbn))
	rows=curr.fetchall()
	conn.close()
	return rows

def delete(id):
	conn=sqlite3.connect("books.db")
	curr=conn.cursor()
	curr.execute("DELETE FROM book WHERE id=?", (id,))
	conn.commit()
	conn.close()

def update(id, title, author,year,isbn):
	conn=sqlite3.connect("books.db")
	curr=conn.cursor()
	curr.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?", (title,author,year,isbn, id))
	conn.commit()
	conn.close()



connect()
# insert("small","great",1999,323442)
# print(view())
# delete(3)
# print(search(author="great"))
