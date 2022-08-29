import sqlite3
import library
print(library.Addbook) 
class digitallibrary():
    def __init__(self,book_name,authorname,publication_name,pages,price,weight,height,length):
        self.con = sqlite3.connect('digitallibrary.db')
        self.cur = self.con.cursor()
        self.book_name =book_name
        self.authorname =authorname
        self.publication_name =publication_name
        self.pages = pages
        self.price =price
        self.weight = weight
        self.height =height
        self.length = length
    def library(self,book_name,authorname,publication_name,pages,price,weight,height,length):
        ob =(book_name,authorname,publication_name,pages,price,weight,height,length) 
        mylist = [] 
        mylist.append(ob)
    def displaybook(self):
        print(f"we have following books in labrary:",{self.book_name})
        print(f"we have match the author name in ",{self.authorname})
        print(f"we have {self.publication_name} in a library")
        print(f"we have pages on book: ",(self.pages))
        print(f"books price:",{self.price})
        print(f"we have weighdth of book is:",{self.weight})
        print(f"we  have hight of book :",{self.height})
        print(f"we have length of book is:",{self.length})
    def searchbook(self):
        book  = input("Enter book name") 
        if book == self.book_name:
            print("book is available")
        else:
            print("book not availble")             
    def submit_book(self):
        choice1 = print("user are submitted book")
        if  choice1:
            print("user are submitted  book")     
        else:
            print("not submmited book")
    def return_book(self):
        print("user retunedbook")  
    def search_in_writer_name(self):
        l = str(input("Enter by users"))
        if self.authorname in l:   
            print(authorname)
    def showbook(self):
        list = input("enter the the letter of book")
        if list in self.book_name :
            check ='a'
            print("the list of book :"+str(list))
            res= [index for index in self.book_name if index[0].lower() == check.lower()]  
obj =digitallibrary('book_name','authorname','publication_name','pages','price','weight','height','length')
obj.mylist[]
obj.library()
obj.displaybook()
obj.searchbook()
obj.submit_book()
obj.return_book()
obj.search_in_writer_name()
obj.showbook() 
