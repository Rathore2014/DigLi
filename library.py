from sqlite3 import connect
import  pymysql
conn =  pymysql.connect(user='sql5502206',db='sql5502206',passwd='AvZuqMITRP',host='sql5.freesqldatabase.com')
cur = conn.cursor()

flag = input('Do you want to add library data : ')
if flag.lower() == 'yes':
    name = input("Enter the name:  ")
    id = input("Enter the id:  ")
    issuedate = input("Enter the issue book date:  ")
    submitdate = input("Enter the book submitdate:   ")
    stock = int(input("Enter the stock of book:  "))
    book = input("Enter the book name:  ")
    author = input("Enter the auther name of the book:  ")
    address = input("Enter the address of Student:  ")
    query = 'INSERT INTO `Library` (`Name`, `Id`, `IssueDate`, `SubmitDate`, `Stock`, `Book`, `Author`, `Address`) VALUES ("{}", NULL, "{}", "{}", {}, "{}", "{}", "{}")'.format(name,id,issuedate,submitdate,stock,book,author,address)
    cur.execute(query)
    conn.commit()

sQuer = 'SELECT * from Library'
cur.execute(sQuer)
res = cur.fetchall()
print(res)

# class Library():
def Addbook():
  book_name = input("Enter the book name:  ")
  book_code = input("Enter the book code:  ")
  book_total = int(input("Enter the total book:  "))
  book_subject = input("Enter the subject of the book:  ")
  data = (book_name,book_code,book_total,book_subject)
  add_query = 'INSERT INTO addbook ("book name", "book id", "book code", "book total", "book subject") VALUES ("{}", NULL, "{}", {}, "{}")'.format(book_name, book_code, book_total, book_subject)
  cur = conn.cursor()
  cur.execute(data,add_query)
  conn.commit()
  print("Enter the book data SUCCESSFULLY:")
Addbook()
sQuery = 'SELECT * from addbook'
cur.execute(sQuery)
resu = cur.fetchall()
print(resu)

# def issuebook():
