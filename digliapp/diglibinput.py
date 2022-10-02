import sqlite3
from diglib import book
import json

class input_book:
  def __init__(self):
    self.db_con = sqlite3.connect('digli.db')
    self.cur_obj = self.db_con.cursor()
    self.cur_obj.execute("CREATE TABLE IF NOT EXISTS books (book_name text, isbn INT ,author VARCHAR(100));")
    # self.query = 'ALTER TABLE books ADD isbn ,author VARCHAR(100);'
    # self.cur_obj.execute(self.query)
    # self.db_con.commit()

  def inputcli(self):
    name = input("Enter book name : ")
    isbn = int(input("Enter ISBN number : "))
    author = input("Enter Author Name : ")
 
    j = f'SELECT * FROM books WHERE isbn ={isbn}'
    self .cur_obj.execute(j)
    check =self.cur_obj.fetchall()
    length = len(check)
    if length>0:
      print("This book is already exist!")
      
    else:

      q = f"INSERT INTO books VALUES ('{name}', {isbn},'{author}')"
      self.cur_obj.execute(q)
      self.db_con.commit()

  def inputfromjson(self):

    with open("data.json","r") as f:
      data = json.loads(f.read())
    print(data["book_info"][1]["book_name"])
   
    for i in data["book_info"]:
      print(i["isbn"], {i["book_name"]})
      w = f'SELECT * FROM books WHERE isbn = {i["isbn"]}'
      self .cur_obj.execute(w)
      check =self.cur_obj.fetchall()
      length = len(check)
      if length>0:
        print("This book is already exist!!!!")
        
      else:
        q = f'INSERT INTO books VALUES ("{i["book_name"]}",{i["isbn"]},"{i["author"]}")'
        self.cur_obj.execute(q)
        self.db_con.commit()
    query = 'SELECT * FROM books'
    self.cur_obj.execute(query)
    res = self.cur_obj.fetchall()
    return res
