from secrets import choice


def book_issues():
    user_id=input("enter  user id")
    pswd=input("enter password")
    name =input("enter name ")
    contct_no=input("enter contact number")
    e_mail= input("Enter email address of user")
    address=input("enter addresss")
    gender= input("Enter gender")
    print("id is",user_id)
    print("password is",pswd)
    print("name",name)
    print("contact no is" ,contct_no)
    print("emil of user is",e_mail) 
    print("address of user",address) 
    print("gender of user",gender)
    data=(user_id,pswd,name,contct_no,e_mail,address,gender)
    print("****************************************************************************")
    print("Data Entered Succesfully")
book_issues()    
def infobook():
    bn =input("Enter book name :")
    author= input("Enter book author name :")
    price= int(input("Enter book price :"))
    userbook=int(input("Enter user pick up book by from library :"))
    data =(bn,author,price,userbook)
    print(bn)
    print(author)
    print(price)
    print(userbook)
infobook() 
l ={'ramayan':'valmiki','mahabharat':'vedvyash'}  
book= input                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          = input("Enter book name")
def serchbook():
    if( book in l):
        print("search are available")
    else:
        print("search are not available")
serchbook() 
def showbook():
    print("All book are starting from lettre:",A,Z)
showbook()           
def returnbook():
    choice = 1 
    if choice == 1:
        print("person return book")
    else:
        print("person not returning")
returnbook()        