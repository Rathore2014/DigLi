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
    def searchbook(self):
        lb  ={'python programming':'john M Zelle','let us c':'Yaswant krnetker','fundamental of computer':'E balaguruswami'}
        book  = Input("Enter book name") 
        if book in lb:
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
    def serchbook_in_letter():
       input("Enter letter ")
       print("all book staring from letter ")          
obj =digitallibrary(self,book_name,authorname,publication_name,pages,price,weight,height,length)
obj.mylist=[]             
obj.displaybook()
obj.searchbook()
obj.submit_book()