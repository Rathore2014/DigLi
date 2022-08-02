class Library():
    def Book():
        python = {
            "Python Programming" : "John M Zelle",
            "Python Pocket Reference" :"Mark Lutz",
            "Python Cookbook" : "David Beazley"
        }
        c_book = {
            "C Programming Absolute Beginner's" : "Greg Perry and Dean Miller",
            "C Programming Language" : " Brain W. Kernighan ",
            "Head First C " : "Griffiths David"
        }
        java = {
            "Effective Java" : "Joshua Bloch",
            "Spring in Action" : "Craig Walls and Ryan Breidenbach",
            "Thinking in Java " : " Bruce Eckel"
        }
        
    Book()
    def searchbook():
        python = {
            "Python Programming" : "John M Zelle",
            "Python Pocket Reference" :"Mark Lutz",
            "Python Cookbook" : "David Beazley"
        }
        c_book = {
            "C Programming Absolute Beginner's" : "Greg Perry and Dean Miller",
            "C Programming Language" : " Brain W. Kernighan ",
            "Head First C " : "Griffiths David"
        }
        java = {
            "Effective Java" : "Joshua Bloch",
            "Spring in Action" : "Craig Walls and Ryan Breidenbach",
            "Thinking in Java " : " Bruce Eckel"
        sbook  = Input("Enter book name") 
        if book in python:
            print("book is available")
        elif book in java:
            print("book is available")
         elif book in c_book:
            print("book is available")
        else:
            print("book not availble") 
    def Addbook():
        flag = input('Do you want to add library data : ')
        if flag.lower() == 'yes':
            book_name = input("Enter the book name:  ")
            book_code = input("Enter the book code:  ")
            book_author = input("Enter the book author name: ")
            book_publ = input("Enter the Publisher name: ")
            book_subject = input("Enter the subject of the book:  ")   
            book_edit = input("Enter the edition of the book: ") 
    Addbook()

    def Issuebook():
        issue = input("Do you want to take book in the library :")
        if issue.lower() == 'yes':
            ibook_name = input("Enter the book name:  ")
            ibook_subject = input("Enter the subject of the book:  ")  
            ibook_author = input("Enter the book author name: ")
            ibook_date = input("Enter the date of issue book: ")
    Issuebook()
    
    def Submitbook():
        sbook_name = input("Enter the book name:  ")
        sbook_subject = input("Enter the subject of the book:  ")  
        sbook_author = input("Enter the book author name: ")
        sbook_date = input("Enter the date of submmit book: ")
    Submitbook()    

obj = Library()
choice = 1
while choice != 0:
    print("1. Book ")
    print("2. Users ")
    print("3. Search")
    print("4. Addbook")
    print("5. Issuebook")
    print("6. Submitbook")
    choice = int(input("Enter your choice:  "))
    if choice == "Book":
        print(obj.Book())
    elif choice == "Addbook":
        print(obj.Addbook())
    elif choice == "Issuebook":
        print(obj.Issuebook())
    elif choice == "Submitbook":
        print(obj.Submitbook())    
    else:
        print("Invalid choice")    
