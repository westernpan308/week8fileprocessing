while True:
  input("Please enter a File name: ")
  name = (input("\nPlease enter your First and last name: "))
  street = (input("\nPlease enter your street name: "))
  phone = (input("\nPlease enter your phone number including your area code: "))
  #empty line (line 6 for a cleaner look)
  print ()
  print(""+name+", "+street+", "+phone+"")

  input("\nwould you like to add another File Y or Yes N for No: ")
  #option = input("y/n > ")
      
  if input == "y" or input == "Y":
    print()
        
  elif input == "n" or input == "N":
    print("\nThank you and have a great day")
    exit()
  else:
    print("\nError invalid entry please try again with Y or N\n ")

      
        
   
