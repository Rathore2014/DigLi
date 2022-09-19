import sqlite3
db = sqlite3.connect ('liberary.db' )
cr = db.cursor()

class Liberary():
      # CREATING INIT FUNCTION...........
   # def __init__(self,name,roll,father_name,contact_no):
   #    self.name = name
   #    self.roll = roll
   #    self.father_name = father_name
   #    self.contact_no = contact_no


          #...................... ADDING STUDENTS..........................
   def addStudent(self):

      db = sqlite3.connect ('liberary.db' )
      cr = db.cursor()
      # Creating table for student
      # query = 'CREATE TABLE student(ID INT PRIMARY KEY, Name varchar(100), father_name varchar(100), roll_no INT, contact_no int(12));'
      # cr.execute(query)
      # db.commit()

      name = input("Enter student name : ")
      rollNo = int(input("Enter the roll of student :"))
      father_name = input("enter father name :")
      contact_no = int(input("Enter contact number :"))

      idQuery = 'SELECT  ID FROM student ORDER BY ID DESC;'
      cr.execute(idQuery)
      res = cr.fetchone()
      # Query TO Insert Data in student Table 
      print(res)
      newID = res[0]+1
      query = f'INSERT INTO student VALUES({newID},"{name}", "{father_name}" ,{rollNo},{contact_no});' 
      cr.execute(query)
      db.commit()

      idQuery = 'SELECT * FROM student ORDER BY ID DESC;'
      cr.execute(idQuery)
      res = cr.fetchone()
      print('inserted value is ',res )

            #.....................To ISSUE_BOOK from liberary..................

   def issue_book(self):

      db = sqlite3.connect ('liberary.db' )
      cr = db.cursor()

      #creating TABLE for issue_book.........
      # query = 'CREATE TABLE issue_book (ID INT PRIMARY KEY, booknm varchar(50), Issuedate date, Studentnm varchar(50), studentroll int(10));'
      # cr.execute(query)
      # db.commit()
      # query = "DROP TABLE Issue_book"
      
      # cr.execute(query)
      # db.commit()
      
      Booknm = input("Enter the name of book: ")
      Issuedate = input("Enter the date of issue book :")
      Studentnm = input("Enter the name of student :")
      studentroll = int(input("Enter the roll of student :"))

      idQuery = 'SELECT ID FROM issue_book ORDER BY ID DESC;'
      cr.execute(idQuery)
      res = cr.fetchone()

      #Query To Insert Data in issue_book Table[(0,9,8)]
      #try:
      print(res[0])
      newID =res[0]+ 1
      query = f'INSERT INTO issue_book VALUES({newID},"{Booknm}","{Issuedate}","{Studentnm}",{studentroll}); '
      cr.execute(query)
      db.commit()
      print('insert value is ',res)


      idQuery = 'SELECT * FROM issue_book ORDER BY ID DESC;'
      cr.execute(idQuery)
      res = cr.fetchone()
      print('inserted value is ',res) 



            #.......................To SUBMIT_BOOK in liberary.........................

   def submitbook(self):
      db = sqlite3.connect ('liberary.db' )
      cr = db.cursor()
   #creating TABLE for submitbook
      # query = 'CREATE TABLE submitbook(ID INT PRIMARY KEY ,DOS int(20) , bookName varchar(50) , studentNAME varchar(50) , studentRoll int );'
      # cr.execute(query)
      # db.commit()
      # query = "DROP TABLE submitbook"
      # cr.execute(query)
      # db.commit()

      DOS = input("Date of submission : ")
      bookName = input("Enter Book Name : ")
      studentName = input("enter the name of student :")
      studentroll = int(input("Enter the roll of student :"))

      idQuery = 'SELECT  ID FROM submitbook ORDER BY ID DESC;'
      cr.execute(idQuery)
      res = cr.fetchone()
      #Query To Insert Data in submitbook Table
      
      print(res[0])
      newID =res[0]+ 1
      query = f'INSERT INTO submitbook(ID , DOS , bookName , studentName , studentroll) VALUES({newID} , "{DOS}" , "{bookName}" , "{studentName}" , {studentroll});'
      cr.execute(query)
      db.commit()
      print('insert value is ',res)

      idQuery = 'SELECT * FROM submitbook ORDER BY ID DESC;'
      cr.execute(idQuery)
      res = cr.fetchone()
      print('inserted value is ',res)


               #................ to ADD_BOOK in liberary..................

   def addBook(self):

      db = sqlite3.connect ('liberary.db' )
      cr = db.cursor()
   #Creating table for addbook
      # query = 'CREATE TABLE addbook (ID INT PRIMARY KEY, Name varchar(100), bookPub varchar(100), book_id INT, book_status varchar(100));'
      # cr.execute(query)
      # db.commit()

      bookName = input(" Enter Book name : ")
      bookPub = input("Enetr name of publication :")
      book_id = int(input("Enter Book_id :"))
      book_status =int(input("Enter Book_status :")) 

      idQuery = 'SELECT  ID FROM addbook ORDER BY ID DESC;'
      cr.execute(idQuery)
      res = cr.fetchone()
      # Query TO Insert Data in addbook Table 
      print(res)
      newID = res[0]+1
      query = f'INSERT INTO addbook VALUES({newID},"{bookName}", "{bookPub}" ,{book_id},{book_status});' 
      cr.execute(query)
      db.commit()

      idQuery = 'SELECT * FROM addbook ORDER BY ID DESC;'
      cr.execute(idQuery)
      res = cr.fetchone()
      print('inserted value is ',res)

obj = Liberary()

# callFunction()........   
# obj.addStudent()
#obj.issue_book()
obj.submitbook()
obj.addBook()
db.close()