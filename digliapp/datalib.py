import sqlite3 
from diglibinput import input_book
from digliboutput import  searchmenu
from diglib import book
class sqdata(object):
  def __init__(self):
      pass     
conn =sqlite3.connect("diliapp")
cur = conn.cursor
query_1= conn.execute(""" CREATE TABLE IF NOT EXISTS books
        (book_isbn INT,book_title TEXT,book_author TEXT, 
        book_publisher TEXT,book_subject TEXT,book_edition TEXT)""")

query_2= conn.execute("""INSERT INTO books VALUES
              ('1234567890123','programming','jhon jelli',
             's chand','programing lanuge' ,'third_edition') """)
conn.commit()

for row in conn.execute("SELECT * FROM books "):
    print(row)
    