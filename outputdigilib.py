from socket import TIPC_CFG_SRV


class digitallibrary:
    def __init__(self,book_name,authorname,publication_name,pages,price,weight,height,length):
        self.book_name =book_name
        self.authorname =authorname
        self.publication =publication_name
        self.pages = pages
        self.price =price
        self.weight = weight
        self.height =height
        self.length = length
    mylist = []
    def displaybook(self):
        print(f"we have following books in labrary:",{self.book_name})
        print("we have match the author name in ",{self.authorname})
        print("we have {self.publication_name} in a library")
        print("we have pages on book: ",(self.pages))
        print("books price:",{self.price})
        print("we have weighdth of book is:",{self.weight})
        print("we  have hight of book :",{self.height})
        print("we have length of book is:",{self.lentgh})
book_name  =input("enter book name")
authername =input("enter the authorname")
publication_name =input("enter publication name") 
pages =int(input("enter pages of a book"))
price =int(input("enter the price of book"))
weight  =int(input("enter the weight")) 
height =int(input("enter height"))
length =int(input("enter the lenght"))
obj =digitallibrary()
obj.mylist=[]             
obj.displaybook()
