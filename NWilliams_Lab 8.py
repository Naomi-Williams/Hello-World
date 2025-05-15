#Naomi Williams
#4/25/2025
#Receieve Estimates for building a deck Program
#Constants for the program
PI = 3.14
WOOD_COST_PER_SQUARE_FOOT = 7.45
SALES_TAX_RATE = 0.06

#Step #1: Welcome Function beginning defined
def welcome():                                         #Parameter - None
    print("\tNaomi's Deck Builders")                   #Return - None
    print("\tA Student Propritor")
    print("\tOwner: Naomi Williams")
#Step #2: Function to read Customer information from file provided by user
#Parameter - None
#Return - Information from the file about the customers
def Read_Data():
    #Initializing a new list
    Customer_Data = [] #Empty list
    #Prompt the user to enter a valid path and name that can be reached
    #Start a loop so that it doesn't stop until the user inputs a valid file name and path
    bFlag = True
    while bFlag:
        try:
            FilePath = input("Enter in the path and the file name containing customer data: ")
            file = open(FilePath, "r")
            for line in file:
                #Append each line to empty list Customer_Data
                Customer_Data.append(line.strip()) 
            #End the loop once the last line is read and put into the list
            bFlag = False
            #Close the file
            file.close() 
            #Sort the list by the last name (first element in the string)
            #Sorts the strings in this by alphabetically
            Customer_Data.sort()
        #If the user inputs a file that can't be locate this catches the exception and alows them to reenter it
        except FileNotFoundError:
            print("Error - Cannot find this file. Please reenter.")
    return Customer_Data
#Function to calculate the area of the rectangular deck
def calcRecArea(length, width):                        #Parameter - float length, and width
    area = length * width
    return area                                        #Return - float for the area of the rectangular area
#Function to calculate the area of the circular deck
def calcCirArea(radius):                               #Parameter - float for the radius of the deck
    area = PI * radius * radius
    return area                                        #Return - the area of the circular deck
#Function for trapezodial deck
def calcTrapArea(slen, llen, height):                  #Parameter - float of slen, llen, and height
    area = (slen + llen) / 2 * height
    return area                                        #Return - the area of the trapezoidal deck
#Step #7: Funtion to Calculate the total price
def calcTotalPrice(area):                              #Parameter - the area of the chosen shape
    Total_Price = area * WOOD_COST_PER_SQUARE_FOOT
    return Total_Price                                 #Return - Result of the calculation(float)
#Step #8: Functions to Display Estimate
def displayEstimate(name, cell, email, area, Total_price):         #Parameter - name, cell, email, area, and Total_price
    tax = Total_price * SALES_TAX_RATE                             #Return - None
    final_price = Total_price + tax
    print("\nWilliams Deck Builders")
    print(f"\nName: \t{name}")
    print(f"Cell: \t{cell}")
    print(f"Email: \t{email}")
    print(f"\nThe area of the deck is {area:.2f} square feet")
    print(f"The cost of the wood is ${WOOD_COST_PER_SQUARE_FOOT} per square foot")
    print(f"\nThe subtotal cost is ${Total_price:,.2f}")
    print(f"The tax is ${tax:,.2f}")
    print(f"The total cost is ${final_price:,.2f}")
    
#Function of goodbye message for end of program    
def goodBye():                                                      #Parameter - None
    print("Thank you for using Naomi's Deck Builders")              #Return - None
    print("\t Please come back next time!!")
   
#Step #3
#Main Function that displays the function
#Parameter - none
#Return - none
def main():                                                  
    welcome()
    #Calling the read_data function an assigning it to the Customer_Data variable that also contains the list
    Customer_Data = Read_Data()
    #Ask the user if they want to see the invoice of another customer if yes they input 'y' if no 'n' the good bye message displays
    another_estimate = "y"
    while another_estimate in ["y", "Y"]:
        #Initialize counter at 1
        counter = 1 
        #Go through all the strings in the Customer_Data list and display a menu for the user to choose from
        for customer in Customer_Data:
            #Split up the strings in the list based on the comma delimeter
            string = customer.split(',')
            #Take the first and second element from the split string and captialize the first letter in the elements then cocatenate them together
            fullname = f"{string[1].capitalize()} {string[0].capitalize()}"
            #Displays the name of the customer based on the split elements
            #Displays:  1.      firstname lastname
            #           2.      firstname lastname
            #           3.      firstname lastname
            #           4.      etc...
            print(f"{counter}. {fullname}")
            #It adds one to the counter until get to the last customer string
            counter += 1
        #Start a loop to ask the user to enter the numerical choice of a customer 
        bFlag2 = True
        while bFlag2:
            try:
                #Ask the user to input their numerical choice of the customer data they want to see but subtract 1 from the input to account 
                #for the way humans count they start at 1 while computers start a zero
                choice = int(input("Select the customer from the list: ")) - 1
                #If the users inputs a number less than zero and greater than the number of strings in the list Customer_Data
                if choice < 0 or choice >= len(Customer_Data):
                    print("Invalid choice. Plese reenter.")
                else:
                    #End the loop if the user inputed a valid choice
                    bFlag2 = False      
            except ValueError:
                print("Invalid input. Please reenter a numerical value.")
        #Display selected customer data
        #This is the index of the list Customer_Data if someone input 1 it really means zero because we substracted one menaing the first string in the list
        Selected_Customer = Customer_Data[choice]
        #Use the variable that holds the selected invoice then split that string based on the comma delimitor
        Component = Selected_Customer.split(',')
        #Check if the split string has 8 components/elements if it doesn't it displays a error
        if len(Component) == 8:
            #Index 0: Last name #Index 1: First name
            name = f"{Component[1].capitalize()} {Component[0].capitalize()}"
            #Index 2: cell phone
            cell = Component[2]
            #Index 3: email
            email = Component[3]
            #Index 4: shape in lowercase
            shape = Component[4].lower()
            #Index 5: change length to a float (rectange), change diameter to a float(circle), change short length to float(trapezoid)
            dimension1 = float(Component[5])
            #Index 6: change width to a float (rectange), Ignored for (circle), change long length to float(trapezoid)
            dimension2 = float(Component[6])
            #Index 7: change height to a float (trapezoid), Ignored for (rectange, and circle)
            dimension3 = float(Component[7])
        
            #Calculate the area based on selected shape
            if shape == "rectangle":
                area = calcRecArea(dimension1, dimension2)
            elif shape == "circle":
                area = calcCirArea(dimension1 / 2)
            elif shape == "trapezoid":
                area = calcTrapArea(dimension1, dimension2, dimension3)
        
            price = calcTotalPrice(area)
            displayEstimate(name, cell, email, area, price)
        else:
            print("Error: String in Customer data does no have 8 elements")
        #Ask the user if they want to see another customers data
        another_estimate = input("\nWould you like another estimate? (y/n): ")
        while another_estimate not in ["y", "Y", "n", "N"]:
            print("Error - Please enter y or n. ")
            another_estimate = input("\nWould you like another estimate? (y/n): ")
    #Calling the goodbye function to display goodbye message        
    goodBye()
#Calling the main function to display the main function information
main()