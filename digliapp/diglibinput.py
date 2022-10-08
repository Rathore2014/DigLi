import sqlite3
from diglib import book
import json

def checkavailbility(isbn, name):
  db_con = sqlite3.connect('digli.db')
  cur_obj = db_con.cursor()
  j = f'SELECT * FROM books WHERE isbn ={isbn} '
  cur_obj.execute(j)
  check =cur_obj.fetchall()
  length = len(check)
  if length > 0 :
    
    return True
  else:
    return False

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
 
    
    if checkavailbility(isbn = isbn, name = name):
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
      
      if checkavailbility(isbn = i["isbn"], name = i["book_name"]):
        print("This book is already exist!!!!")
        
      else:
        q = f'INSERT INTO books VALUES ("{i["book_name"]}",{i["isbn"]},"{i["author"]}")'
        self.cur_obj.execute(q)
        self.db_con.commit()
    query = 'SELECT * FROM books'
    self.cur_obj.execute(query)
    res = self.cur_obj.fetchall()
    return res
 #obj = input_book()
# obj.inputcli()
# print(obj.inputfromjson())