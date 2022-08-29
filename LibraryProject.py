import projectlibrary
import liberary
class Library():
#     This class is used to keep record of books library.

    def __init__(self,list_of_book,library_name):
        self.list_of_book = "List_of_book.txt"
        self.library_name = library_name
        self.books_dict = {}
        Id = 101
        with open(self.list_of_books) as book:
            content = book.readlines()
        for line in content:
            self.books_dict.update({str(ID):{"books_title  : line replace"("\n", ""),
                                             "lender_name" : "",
                                             "Issue_date" :  "",
                                             "Status" : ""}})
        Id = Id + 1
        
        
#         """   It has total five module: "Display Book", "Search Book", "Add Book ", "Issue Book", "Submmit Book "   """

    def DisplayBook(self):
        print("------------List of Book------------")
        print("Book Id", "/t", "Title")
        for key, value in self.books_dict.items():
            print(key, "/t""/t", value.get("books_title"), value.get("Status"))
    
    
    
#              """ IMPORT projectlibrary AND liberary MODULE IN MY PROJECT"""
    def Importing(self):
        projectlibrary.searchbook(searchbook.book)
        print("Well Come to SearchBook Function:")
        liberary.addBook(addBook.adbk)
         print("Well Come to AddBook Function:")
        liberary.addStudent(addStudent.name,addStudent.roll)
         print("Well Come to AddStudent Function:")
    
    
          

    def Issuebook(self):
        issue = input("Do you want to take book in the library :")
        if issue.lower() == 'yes':
            ibook_name = input("Enter the book name:  ")
            ibook_subject = input("Enter the subject of the book:  ")  
            ibook_author = input("Enter the book author name: ")
            ibook_date = datetime.datetime.now()
            if books_id in self.books_dict.keys():
              if not self.books_dict[books_Id]["Status"] == "Available":
                 print(f"This book is already Issue to{self.books_dict[book_Id]["Lender_name"]}"\
                      on {self.books_dict[book_Id][Issue_date]})
                 return self.Issue_books()
            if self.books_dict[books_Id]["Status"] == "Available":
            name = input("Enter the your name:  ")
            self.books_dict[book_Id]["Lender_name"] =name
            self.books_dict[book_Id]["Issue_date"] =ibook_date
            self.books_dict[book_Id]["Status"] ="Already Issued"
            print("---Book Issued Successfull:---")
    
    
    def Submitbook(self):
        sbook_name = input("Enter the book name:  ")
        sbook_subject = input("Enter the subject of the book:  ")  
        sbook_author = input("Enter the book author name: ")
        sbook_date = input("Enter the date of submmit book: ")
      

obj = Library("List_of_books.txt", "Python's Library")
choice = 1
while choice != 0:
    print("1. Searchbook")
    print("2. Addbook")
    print("3. Issuebook")
    print("4. Submitbook")
    print("5.  DisplayBook")        
    choice = int(input("Enter your choice:  "))
    if choice == "DisplayBook":
        print(obj.DisplayBook())
    elif choice == "SearchBook":
        print(obj.SearchBook())
    elif choice == "Addbook":
        print(obj.Addbook())
    elif choice == "Issuebook":
        print(obj.Issuebook())
    elif choice == "Submitbook":
        print(obj.Submitbook())    
    else:
        print("Invalid choice")    

        
        
        
        
        
