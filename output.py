list = ['ramayan','mhabharat']
book_name = input("enter book name")
authorname =input("enter authorname")
publication_name =input("Enter book publiction name")
search_query =print("Search book are available")
Author_name =print("In this authorname book are available")
Publication_name =print("This publication name of book are available")
firstletter_of_book =print(f"All books of this letter are :",Null, "{}")
if search_query in book_name :
    if authorname in Author_name:
        print("books are available")
    else:
        print("books are not available")
elif publication_name in Publication_name:
    print("The books are available of this publication")        
else:
    print("books are not available of this publication")          
