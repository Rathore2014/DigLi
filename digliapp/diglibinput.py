import sqlite3
from diglib import book

class input_book:
  def __init__(self):
    self.db_con = sqlite3.connect('digli.db')
    self.cur_obj = self.db_con.cursor()
    self.cur_obj.execute("CREATE TABLE IF NOT EXISTS books (book_name text)");

  def inputcli(self):
    name = input("Enter book name")
    #b_n = book(name)
    q = f"INSERT INTO books VALUES ('{name}')"
    self.cur_obj.execute(q)
    self.db_con.commit()
    self.db_con.close()

  def inputfromjson(self):
    pass