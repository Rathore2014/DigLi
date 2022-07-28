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
    def Users():
        name = input("Enter the name:  ")
        id = input("Enter the id:  ")
        address = input("Enter the address of Student:  ")
        mobile = int(input("Enter the mobile number of user: "))
        email = input("Enter the email id of user: ")
    Users()

    def Search():
        take = input("If you want to take book in the library: ")
        if take.lower() == 'yes':
            print("Three types of book available in the library:")
            blist = ["Python","C_book","Java"]
            print(blist)
            # print(random.choice(blist))
            # choice = 1
            # while choice != 0:
            #     print("1.")
            #     print("2.")
            #     print("3.")
            #     choice = int(input("Enter your choice:  "))
            #     if choice == 1:
            #         print("Python")
            #         for book,author in python.items():
            #             print(book,author)
            #     elif choice == 2:
            #         print("C_book")
            #         for cbook,cauthor in c_book.items():
            #             print(cbook,cauthor)
            #     elif choice == 3:
            #         print("Java")
            #         for jbook,jauthor in java.items():
            #             print(jbook,jauthor)
            #     else:
            #         print("Invalid choice")   
            print("Enter the book name you want: ")
            print("Thank you!" "\n" "Study well")     
    Search()
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
    elif choice == "Users":
        print(obj.Users())
    elif choice == "Search":
        print(obj.Search())    
    elif choice == "Addbook":
        print(obj.Addbook())
    elif choice == "Issuebook":
        print(obj.Issuebook())
    elif choice == "Submitbook":
        print(obj.Submitbook())    
    else:
        print("Invalid choice")    