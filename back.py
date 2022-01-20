import sqlite3 

class Database: 

	def __init__(self, db):
		self.conn=sqlite3.connect(db)
		self.curr=self.conn.cursor()
		self.curr.execute("CREATE TABLE IF NOT EXISTS book (id  INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
		self.conn.commit()

	def insert(self,title, author, year, isbn):
		curr.execute("INSERT INTO book VALUES (NULL, ?,?,?,?)", (title, author,year,isbn))
		conn.commit()
		conn.close()

	def view(self):
		self.curr.execute("SELECT * FROM book")
		rows=self.curr.fetchall()
		self.conn.close()
		return rows


	def search(self, title="", author="", year="", isbn=""):
		curr.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?", (title,author,year,isbn))
		rows=curr.fetchall()
		conn.close()
		return rows

	def delete(self, id):
		curr.execute("DELETE FROM book WHERE id=?", (id,))
		conn.commit()
		conn.close()

	def update(self, id, title, author,year,isbn):
		curr.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?", (title,author,year,isbn, id))
		conn.commit()
		conn.close()



#Database()
# insert("small","great",1999,323442)
# print(view())
# delete(3)
# print(search(author="great"))
