from diglibinput import input_book
from diglibsearch import search
from digliboutput import output_book
import sys

def menu():
  print()
  choice = int(input("""
                      1: Enter new book record
                      2: Search if book exist
                      3: Get all books in library
                      4: Delete - delete
                      5: Exit
                      Please enter your choice: """))

  if choice == 1:
    inpobj = input_book()
    input_type = input("1: Enter  from CLI Input \n2: Enter  from Json Input : ")
    if input_type == "1":
      inpobj.inputcli()
    elif input_type == "2":
      inpobj.inputfromjson()
    else:
      print("Wrong value entered. Please Try again...")
      retry = input("1: Retry \n2: Exit....")
      if retry == "1":
        menu()
      else:
        ("thanks We are terminating process ... ")
  elif choice == 2:
    s_obj = search()
    print(s_obj.name())
  elif choice == 3:
    o_obj = output_book()
    print(o_obj.getdata())
  elif choice == 4:
    delete()
  elif choice == 5:
    sys.exit()
  else:
    print("Invalide choice, You must select between 1 and 5")
    print("Please try again")
    menu()

if __name__ == "__main__":
  while True:
    menu()
