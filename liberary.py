
#------------ TABLE CREATION QUERIES -----------#
# query = 'CREATE TABLE student(ID INT PRIMARY KEY, name VARCHAR(50), father_name VARCHAR(100), roll INT, contact VARCHAR(12));'
# cursor.execute(query)
# db.commit()

# query = 'CREATE TABLE add_book(ID INT PRIMARY KEY, book_name VARCHAR(50), publication_name VARCHAR(100), book_id INT, book_status VARCHAR(12));'
# cursor.execute(query)
# db.commit()

# query = 'CREATE TABLE issue_book(ID INT PRIMARY KEY, book_name VARCHAR(50), student_name VARCHAR(100), student_roll INT, issue_date date);'
# cursor.execute(query)
# db.commit()

# query = 'CREATE TABLE submit_book(ID INT PRIMARY KEY, book_name VARCHAR(50), student_name VARCHAR(100), roll INT, dos date);'
# cursor.execute(query)
# db.commit()

#---------END OF TABLE CREATION QUERY -------------------#

""" Input Function start """
# IMPORTIG REQUIRED MODULE
import sqlite3

# DB CONNECTION
db = sqlite3.connect("db.sqlite3")
cursor = db.cursor()

def addStudent():
    name = input("Enter student name : ")
    rollNo = int(input("Enter the roll of student :"))
    father_name = input("enter father name :")
    contact_no = (input("Enter contect number :"))

    query = 'SELECT name, ID from student order by ID ASC;'
    cursor.execute(query)
    curStudent = cursor.fetchall()
    id = curStudent[-1][1] + 1
    for st in curStudent:
        print(' BEfore Insertion Student Name are as ', st[0])
    query = f'INSERT INTO student(ID, name, father_name, roll, contact) VALUES ({id}, "{name}", "{father_name}", {rollNo}, "{contact_no}")'
    cursor.execute(query)
    db.commit()
    query = 'SELECT name from student order by ID ASC;'
    cursor.execute(query)
    curStudent = cursor.fetchall()

    
    print('After insertion Student Name are as ', curStudent[-1][0])


# To issue a book from liberary.....
def issue_book():

    Booknm = input("Enter the name of book: ")
    Issuedate = input("Enter the date of issue book :")
    Studentnm = input("enter the name of student :")
    studentroll = int(input("Enter the roll of student :"))
    
    query = 'SELECT book_name, ID from issue_book order by ID ASC;'
    cursor.execute(query)
    curStudent = cursor.fetchall()
    id = curStudent[-1][1] + 1
    for st in curStudent:
        print(' BEfore Insertion ISsue Book Name are as ', st[0])
    query = f'INSERT INTO issue_book(ID, book_name, student_name, student_roll, issue_date) VALUES ({id}, "{Booknm}", "{Studentnm}", {studentroll}, "{Issuedate}")'
    cursor.execute(query)
    db.commit()
    query = 'SELECT book_name, issue_date from issue_book order by ID ASC;'
    cursor.execute(query)
    curStudent = cursor.fetchall()

    
    print('After insertion ISsue book  Name are as ', curStudent[-1][0], curStudent[-1][1])


# to submit a book in liberary.....
def submitBook():
    DOS = input("Date of submission : ")
    bookName = input("Enter Book Name : ")
    studentName = input("enter the name of student :")
    studentroll = int(input("Enter the roll of student :"))
    query = 'SELECT book_name, ID from submit_book order by ID ASC;'
    cursor.execute(query)
    curStudent = cursor.fetchall()
    id = curStudent[-1][1] + 1
    for st in curStudent:
        print(' BEfore Insertion Submit Book Name are as ', st[0])
    query = f'INSERT INTO submit_book(ID, book_name, student_name, roll, dos) VALUES ({id}, "{bookName}", "{studentName}", {studentroll}, "{DOS}")'
    cursor.execute(query)
    db.commit()
    query = 'SELECT book_name, dos from submit_book order by ID ASC;'
    cursor.execute(query)
    curStudent = cursor.fetchall()

    
    print('After insertion Submit book  Name are as ', curStudent[-1][0], curStudent[-1][1])



    # to add the books in liberary......
def addBook():
    adbk = ["Hindi","English","Math","Sanskrit"]
    bookName = input(" Enter Book name : ")
    bookPub = input("Enetr name of publication :")
    book_id = int(input("Enter Book_id :"))
    book_status =(input("Enter Book_status :")) 
    print("Book detail is enter in library")
    query = 'SELECT book_name, ID from add_book order by ID ASC;'
    cursor.execute(query)
    curStudent = cursor.fetchall()
    id = curStudent[-1][1] + 1
    for st in curStudent:
        print(' BEfore Insertion Book Name are as ', st[0])
    query = f'INSERT INTO add_book(ID, book_name, publication_name, book_id, book_status) VALUES (1, "{bookName}", "{bookPub}", {book_id}, "{book_status}")'
    cursor.execute(query)
    db.commit()
    query = 'SELECT book_name, book_status from add_book order by ID ASC;'
    cursor.execute(query)
    curStudent = cursor.fetchall()

    
    print('After insertion  book  Name are as ', curStudent[-1][0], curStudent[-1][1])


""" End """
addBook()
submitBook()
issue_book()
addStudent()
