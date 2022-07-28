
# call this function for get required input for issuing book
# Adding student.......
def addStudent():
   name = input("Enter student name : ")
   rollNo = int(input("Enter the roll of student :"))
   father_name = input("enter father name :")
   contect_no = int(input("Enter contect number :"))

# To issue a book from liberary.....
def issue_book():
   
   Booknm = input("Enter the name of book: ")
   Issuedate = input("Enter the date of issue book :")
   Studentnm = input("enter the name of student :")
   studentroll = int(input("Enter the roll of student :"))

# to submit a book in liberary.....
def submitBook():
   DOS = input("Date of submission : ")
   bookName = input("Enter Book Name : ")
   studentName = input("enter the name of student :")
   studentroll = int(input("Enter the roll of student :"))

   # to add the books in liberary......
def addBook():
   bookName = input(" Enter Book name : ")
   bookPub = input("Enetr name of publication :")
   book_id = int(input("Enter Book_id :"))
   book_status =int(input("Enter Book_status :")) 


def callFunction():
   functionname = input("Enter Operation name : ")
   if functionname == "addStudent":
      addStudent()
   elif functionname =="issue_book":
      issue_book()
   elif functionname =="submitBook":
      submitBook()
   elif functionname =="addBook":
      addBook()
   else:
      print('This operation is not available')
callFunction()   


