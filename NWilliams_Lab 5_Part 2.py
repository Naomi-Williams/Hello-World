#Naomi Williams
#3/23/2025
#Receieve Estimates for building a deck Program
#Constants for the program
PI = 3.14
WOOD_COST_PER_SQUARE_FOOT = 7.45
SALES_TAX_RATE = 0.06

#Step #1: Welcome Function beginning defined
def welcome():                                         #Parameter - None
    print("\tNaomi's Deck Builders")                   #Return - None
    print("\tA Student Propritor")
#Step #2: Function to gain Customer information
def getinfo():                                         #Parameter - None
    name = input("Enter your Full Name: ")             #Return - None
    cell = input("Enter your cellphone number: ")
    email = input("Enter your email address: ")
    return name, cell, email
#Step #4 #Menu Function to select a Shape
def selectShape():                                     #Parameter - None
    print("\t1. Rectangular")                    
    print("\t2. Circular")
    print("\t3. Trapezoidal")
    Selection = input("Enter menu choice here: (1/2/3): ")
    while Selection not in ["1", "2", "3"]:
        print("Error: please enter a valid selection (1, 2, 3).")
        Selection = input("Enter menu choice here: (1/2/3): ")
    return int(Selection)                              #Return - the selection of the shape
#Step #5: Function to Validate input for dimensions
def valInput(str):                                     #Parameter - string for the dimensions
    dimensions = float(input(f"{str}"))
    while dimensions <= 0:
        print("Error: The dimensions must be greater than zero.")
        dimensions = float(input(f"{str}"))
    return dimensions                                  #Return - the validated interger dimensions
#Step #6: Functions to input rectangular length and width of deck
def getRecDim():                                       #Parameter - None
    length = valInput("Enter the length of the rectangular deck: ")
    width = valInput("Enter the width of the rectangular deck: ")
    return length, width                               #Return - the length and width the users inputed
#Function to calculate the area of the rectangular deck
def calcRecArea(length, width):                        #Parameter - float length, and width
    area = length * width
    return area                                        #Return - float for the area of the rectangular area

#Function to calculated the radius of the circular deck
def getCirDim():                                       #Parameter - None
    diameter = valInput("Enter the diameter of the circular deck: ")
    radius = diameter / 2
    return radius                                      #Return - float for the radius
#Function to calculate the area of the circular deck
def calcCirArea(radius):                               #Parameter - float for the radius of the deck
    area = PI * radius * radius
    return area                                        #Return - the area of the circular deck
#Function for trapezodial deck
def getTrapDim():                                      #Parameter - None
    slen = valInput("Enter the short length of the trapezodial deck: ")
    llen = valInput("Enter the long length of the trapezodial deck: ")
    height = valInput("Enter the height of the trapezodial deck: ")
    return slen, llen, height                          #Return - float for the short length, long length, and height of trapezoidal deck
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
def main():                                                         #Paramter - None
    welcome()                                                       #Return - None
    name, cell, email = getinfo()
    another_estimate = "y"
    while another_estimate in ["y", "Y"]:
        shape = selectShape()
        if shape == 1:
            length, width = getRecDim()
            area = calcRecArea(length, width)
        elif shape == 2:
            radius = getCirDim()
            area = calcCirArea(radius)
        elif shape == 3:
            slen, llen, height = getTrapDim()
            area = calcTrapArea(slen, llen, height)
        
        price = calcTotalPrice(area)
        displayEstimate(name, cell, email, area, price)
        
        another_estimate = input("\nWould you like another estimate? (y/n): ")
        while another_estimate not in ["y", "Y", "n", "N"]:
            print("Error - Please enter y or n. ")
            another_estimate = input("\nWould you like another estimate? (y/n): ")
            
    goodBye()

main()