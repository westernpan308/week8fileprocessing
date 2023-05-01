def main():
  
  while True:
    input("Please enter a File name: ")
    name = (input("\nPlease enter your First and last name: "))
    street = (input("\nPlease enter your street name: "))
    phone = (input("\nPlease enter your phone number including your area code: "))
    #empty line (line 6 for a cleaner look)
    print ()
    print(""+name+", "+street+", "+phone+"")
    
    print("\nwould you like to add another File")
    option = input("y/n > ")
      
    if option == "y" or option == "Y":
      continue
        
    elif option == "n" or option == "N":
      print("\nThank you and have a great day")
      break
    else:
      input("\nError invalid entry please try again with Y or N\n ")
    main