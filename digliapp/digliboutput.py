import sqlite3

class output_book:
  def __init__(self):
    self.db_con = sqlite3.connect('digli.db')
    self.cur_obj = self.db_con.cursor()

  def getdata(self):
    self.cur_obj.execute("select * from books")
    return self.cur_obj.fetchall()
def getdata(self):
    self.cur_obj.execute("select * from books")
    return self.cur_obj.fetchall()
  def searchbook(self):
    db_con = sqlite3.connect('digli.db')
    cur_obj =db_con.cursor()
    self.cur_obj.execute('CREATE TABLE IF NOT EXISTS books(books_isbn INT ,books_author TEXT ,BOOK_TITTLE TEXT);')
    
    """self.query = 'ALTER TABLE books ADD books_author VARCHAR (50);'
    self.cur_obj.execute(self.query)
    self.db_con.commit()"""
    cur_obj.execute("select * from books")
    print(self.cur_obj.fetchall())  
    for i in cur_obj:
      i = list(i)
    print("""
                1: book_isbn
                2: book_title 
                3: book_Author_name 
                please Enter your choice""")
    choice = int(input(" please Enter your choice")) 
    if choice == 1:
      a = input("Enter the book isbn ") 
      if  i[0] == a:
        b = "Select * from library where book_isbn= '{}'".format(a) 
        cur_obj.execute(b)
        r= cur_obj.execute.fetchall()
        print(r)
      else :
        print("Wrong ID //ID not found")
    elif choice == 2:
        a =input("Enter book name  ")
        if  i[1] == a:
          b = "Select * from library where book_title = '{}'".format(a) 
          cur_obj.execute(b)
          r= cur_obj.execute.fetchall()
          print(r)
        else:
          print("That book name is not found") 
    elif choice == 3:
        a = input("Enter Author name for search")
        if  i[2] == a:
          b = "Select * from library where book_Author_name = '{}'".format(a) 
          cur_obj.execute(b)
          r= cur_obj.execute.fetchall()
          print(r)
        else:
          print("That Authrs name book is not found")        
def searchmenu():  
  while True:                 
    searchmenu()
