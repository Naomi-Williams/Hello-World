#Naomi Williams
#4/19/2025
#Bookstore Point Of Sale System Program Updated
#Constants For Products
BACKPACK_PRICE = 45.95
BACKPACK_DISCOUNT_QUANTITY = 3
BACKPACK_DISCOUNT_PERCENTAGE = 0.9
PEN_PRICE_FIVE_OR_FEWER = 0.78
PEN_PRICE_SIX_TO_TEN = 0.68
PEN_PRICE_ELEVEN_OR_MORE = 0.58
PRINTER_INK_PRICE = 41.95
PRINTER_PAPER_REAM_PRICE = 6.00
PRINTER_PAPER_CASE_PRICE = 25.00
SALES_TAX_RATE = 0.06
DISCOUNT_VALUE_CUSTOMER = 0.05
#main function to display the whole program on the screen
def main():
    Continue_Processing = "y"
    while Continue_Processing == "y":
        invoice()
        #Ask Customer if they want to process an invoice
        Continue_Processing = input("\nWould you like to process an invoice? (y/n): ")
        #Input validation for Continue Processing
        while Continue_Processing not in ["n", "N", "y"]:
            print("Error - Please enter (y) or (n)")
            Continue_Processing = input("\nWould you like to process another invoice? (y/n): ")
    print("THANK YOU FOR USING STEVENSON POINT OF SALES SYSTEM")
    
def DispProducts():                                                              #Purchase Options For Customers
    print("STEVENSON BOOKSTORE POINT OF SALES SYSTEM")
    print("\nAVAILABLE PRODUCTS AND PRICING:")
    print("=" * 45)
    print("\nBackpacks:")
    print("$45.95 each (10% discount for 3 or more)")
    print("\nPrinter Ink:")
    print("$41.95 each")
    print("\nPens:")
    print("$0.78 each for 5 or fewer")
    print("$0.68 each for 6 to 10")
    print("$0.58 each for 11 or more")
    print("\nPrinter Paper:")
    print("$6.00 per Ream / $25.00 per case")
    print("\n")
    print("=" * 45)

def Customer_Management():
    #Get Input about the Users purchse
    First_Name = input("\nCustomers First Name: ")
    Last_Name = input("Customers Last Name: ")
    Street_Address = input("Street Address: ")
    City = input("City: ")
    State = input("State: ")
    bFlag2 = True
    while bFlag2:
        try:
            Zip_Code = int(input("Zip Code: "))
            bFlag2 = False   
        except ValueError:
            print("Error - Invalid input. Please reenter a valid numerical value.")  
    #Input Validation PO Number
    Purchase_Order_Number = int(input("PO Number: "))
    while Purchase_Order_Number <= 0:
        #Validate that Order number is greater than zero
        print("Error: The Order Number must be greater than zero.")
        Purchase_Order_Number = int(input("PO Number: "))
    #File object pointer
    bFlag = True
    while bFlag:
        #Asking Customer to input the path and name of a file
        FileName = input("Enter in the name and path of the file: ")
        try: #Test that I can create the file and write to it
            file = open(FileName, 'a')
            file.write(f"{First_Name} {Last_Name}\n")
            file.write(f"{Street_Address}\n")
            file.write(f"{City}, {State} {Zip_Code}\n")
            file.write("\n")
            #Close the file
            file.close()
            bFlag = False
        except FileNotFoundError:          
            print("Error - Cannot find this file. Please reenter.")
    
    return First_Name, Last_Name, Street_Address, City, State, Zip_Code, Purchase_Order_Number

#Function to ask the user for the name and path to the inventory file and making sure the file has 5 numbers
#Parameters - None
#Return - the output of the inventory file
def inventory():
    #Declaring a list
    Inventory = [] #Empty list
    #Prompt the user to enter a valid file path and name that can be reached
    bFlag = True
    while bFlag:
        try:
            Filepath = input("Enter in the name and path of the input file: ")
            file = open(Filepath, 'r')
            for line in file:
                #Turning numbers in the file to integers and appending them to a file
                Inventory.append(int(line.strip()))
            if len(Inventory) == 5:
                bFlag = False
            else:
                print("Error - The file must contain exactly 5 numbers.")
            file.close()
        except FileNotFoundError:
            print("Error - Cannot find this file. Please reenter.")
    return Inventory
#Function to Display Menu and validate the customers menu choice
#Parameter - prompt from customer purchase
#Return - The customers validated numerical choice
def Val_Menu_Choice(prompt):
    #Creating a loop flag
    Valid_choice = True
    while Valid_choice:
        try:
            choice = int(input(prompt))
            if 0 < choice <= 5:
                Valid_choice = False
            else:
                print(f"Error - Please enter a valid option between (1-5).")
                Display_Menu()
        except ValueError:
            print("Error - Invalid input. Please reenter a valid numerical value.")
    return choice                         
def Validate_Quantity_Input(item_name, max_quantity):                                  #Input Validation function
    #Creating a loop flag
    quantity = 0
    bFlag = True
    while bFlag:                                                         #Catches the exceptions when validating
        try: #Test for right data type
            quantity = int(input(f"{item_name}"))
            if 0 < quantity <= max_quantity:
                bFlag = False                                            #END THE LOOP
            elif quantity > max_quantity:
                print(f"Error: You cannot purchase more than what is available {max_quantity}.")
            else:
                print("Error: The quantity must be greater than 0.")
        except ValueError:
            print("\nError - this is not an integer number - Please reenter")
    return quantity
#Function to display the menu to the customer
def Display_Menu():
    #Display the menu to the Customer
    print("\nPlease select from the menu below: ")
    print("\t1. Printer Ink")
    print("\t2. Backpacks")
    print("\t3. Printer Paper")
    print("\t4. Pens")
    print("\t5. Checkout")
    
def Customer_Purchase(Inventory):                                                         #Function for Calculating Totals of Customer Purchase, AND Validating input of the quantity      
    #Initializing running subtotal, total items, total pen, total backpack, total printer ink, and total printer paper
    Running_Subtotal = 0
    total_items = 0
    Total_Pen = 0
    Total_Backpack = 0
    Total_Printer_Ink = 0
    Total_Printer_Paper_Ream = 0
    Total_Printer_Paper_Case = 0
    Quantity_Pen = 0
    Quantity_Backpack = 0
    Quantity_Printer_Ink = 0
    Quantity_Printer_Paper_Ream = 0
    Quantity_Printer_Paper_Case = 0
    bFlag2 = True
    while bFlag2:
        #Display the menu to the Customer
        Display_Menu()
        
        #Validate Menu Choice
        choice = Val_Menu_Choice("Enter selection here (1-5): ")
        
        if choice == 1:  #Printer ink
            if Inventory[0] == 0:
                print("Sorry - Printer ink is out of stock. Please select another item.")
            else:
                #Input Validation Printer Paper, Total price, & Running Subtotal
                quantity = Validate_Quantity_Input("Printer Ink Quantity: ", Inventory[0])
                Inventory[0] -= quantity
                Quantity_Printer_Ink += quantity
                cost = quantity * PRINTER_INK_PRICE
                Total_Printer_Ink += cost
                total_items += quantity
                print(f"Cost for Printer Ink: ${cost:.2f}")
                
        elif choice == 2:
            if Inventory[1] == 0:
                print("Sorry - Printer ink is out of stock. Please select another item.")
            else:
                #Input Validation Backpack, Total price & Running Subtotal
                quantity = Validate_Quantity_Input("Backpack Quantity: ", Inventory[1])
                Inventory[1] -= quantity
                Quantity_Backpack += quantity
                cost = quantity * BACKPACK_PRICE   
                if quantity >= BACKPACK_DISCOUNT_QUANTITY:                    #10% Discount when user buys 3 or more backpacks
                    cost *= BACKPACK_DISCOUNT_PERCENTAGE
                Total_Backpack += cost
                total_items += quantity
                print(f"Cost for Backpacks: ${cost:.2f}")
                
        elif choice == 3:
            #Input Validation Printer Paper & Running Subtotal
            Paper_Type = Val_Menu_Choice("Enter 1 for Reams or 2 for Case ")
            while Paper_Type not in [1, 2]:                                                          #Validate Input for ream or case
                print("Error - please enter (1) or (2)")
                Paper_Type = Val_Menu_Choice("Enter 1 for Ream or 2 for Case: ")
            #Input Validation of printer paper
            if Paper_Type == 1:
                if Inventory[2] == 0:
                    print("Sorry - Reams of Printer Paper are out of stock. Please select another item.")
                else:
                    quantity = Validate_Quantity_Input("Enter Quantity of printer paper ream: ", Inventory[2])
                    Inventory[2] -= quantity
                    Quantity_Printer_Paper_Ream += quantity
                    cost = quantity * PRINTER_PAPER_REAM_PRICE
                    Total_Printer_Paper_Ream += cost
                    total_items += quantity
                    print(f"Cost for Printer Paper Reams: ${cost:.2f}")
            else:
                if Inventory[3] == 0:
                    print("Sorry - Cases of Printer Paper are out of stock. Please select another item.")
                else:
                    quantity = Validate_Quantity_Input("Enter Quantity of printer paper case: ", Inventory[3])
                    Inventory[3] -= quantity
                    Quantity_Printer_Paper_Case += quantity
                    cost = quantity * PRINTER_PAPER_CASE_PRICE
                    Total_Printer_Paper_Case += cost
                    total_items += quantity
                    print(f"Cost for Printer Paper Cases: ${cost:.2f}")         
        if choice == 4:
            if Inventory[4] == 0:
                print("Sorry - Pens are out of stock. Please select another item.")
            else:
                #Input Validation Pens & Running Subtotal
                quantity = Validate_Quantity_Input("Pen Quantity: ", Inventory[4])
                Inventory[4] -= quantity
                Quantity_Pen += quantity
                #Apply discount based on Quantity purchased
                if quantity <= 5:
                    cost = quantity * PEN_PRICE_FIVE_OR_FEWER
                elif quantity <= 10:
                    cost = quantity * PEN_PRICE_SIX_TO_TEN
                else:
                    cost = quantity * PEN_PRICE_ELEVEN_OR_MORE
                Total_Pen += cost
                total_items += quantity
                print(f"Cost of Pens: ${cost:.2f}")
                
        if choice == 5:
            bFlag2 = False
            
        Subtotal = Total_Printer_Ink + Total_Backpack + Total_Pen + Total_Printer_Paper_Ream + Total_Printer_Paper_Case                              #Display Final Running Subtotal
        
        print("\n")
        print("=" * 45)
    return Subtotal, total_items, Quantity_Printer_Ink, Total_Printer_Ink, Quantity_Backpack, Total_Backpack, Quantity_Pen, Total_Pen, Quantity_Printer_Paper_Ream, Total_Printer_Paper_Ream, Quantity_Printer_Paper_Case, Total_Printer_Paper_Case

def Value_Customer_Discount(Subtotal):                       #Calculate Running Subtotal, Applying the Discount
    Discount = 0
    if Subtotal > 499.99:
        Discount = Subtotal * DISCOUNT_VALUE_CUSTOMER        # 5% Discount for valued customers
        Subtotal -= Discount                                 # Subtract the Discount from the Subtotal
    return Subtotal, Discount

def Sales_Tax_Calculations(Subtotal): #Calculate Sales tax
    Tax_Free_Week = input("Is it Maryland's Tax-Free Week? (yes/no): ")            #Ask if its Maryland's Sales Tax Free Week
    #Input validation for customer decision to use Maryland's Tax free week
    while Tax_Free_Week not in ["yes", "no", "y", "n"]:
        print("Error - Please enter (yes) or (no).")
        Tax_Free_Week = input("Is it Maryland's Tax-Free Week? (yes/no): ")
    if Tax_Free_Week in ["yes", "y"]:                                              #If the answer inputed by the user is yes or y then the sales tax will return 0
        print("\nNo sales tax applied to your total. It is Marylands sales tax week. ")
        return 0
    if Tax_Free_Week in ["no", "n"]:
        Sales_Tax_Fee = Subtotal * SALES_TAX_RATE
        return Sales_Tax_Fee                                                           #If the Tax_Free_week is no then multiply the Running subtotal by the Sales tax rate to get taxed amount

def Generate_Receipt(First_Name, Last_Name, Street_Address, City, State, Zip_Code, Purchase_Order_Number, Quantity_Printer_Ink, Total_Printer_Ink, Quantity_Backpack, Total_Backpack, Quantity_Pen, Total_Pen, Quantity_Printer_Paper_Ream, Total_Printer_Paper_Ream, Quantity_Printer_Paper_Case, Total_Printer_Paper_Case, total_items, Subtotal, Discount, Sales_Tax_Fee, Total_Charge):       
    #Customer information Citation: https://www.geeksforgeeks.org/how-to-capitalize-first-character-of-string-in-python/
    Generated_Order_Number = f"{Last_Name[0].capitalize()}{First_Name[0].capitalize()}_{Purchase_Order_Number}"
    Customer_Name = f"{Last_Name.capitalize()}, {First_Name.capitalize()}"
    Total_Charge = Subtotal + Sales_Tax_Fee

    
    Receipt_Content = "\n"
    Receipt_Content += "=" * 45
    Receipt_Content += "\nCustomer information"
    Receipt_Content += f"\nName: {Customer_Name}"
    Receipt_Content += f"\nAddress: {Street_Address}, {City}, {State} {Zip_Code}"
    Receipt_Content += f"\nPO: {Generated_Order_Number}\n"
    Receipt_Content += "-" * 45   
    if Total_Printer_Ink > 0:
        Receipt_Content += f"\n{Quantity_Printer_Ink} printer ink(s) purchased for ${Total_Printer_Ink:.2f}"
    if Total_Backpack > 0:
        Receipt_Content += f"\n{Quantity_Backpack} Backpack(s) purchased for ${Total_Backpack:.2f}"
    if Total_Pen > 0:
        Receipt_Content += f"\n{Quantity_Pen} Pen(s) purchased for ${Total_Pen:.2f}"
    if Total_Printer_Paper_Ream > 0:
        Receipt_Content += f"\n{Quantity_Printer_Paper_Ream} Printer Paper Ream(s) purchased for ${Total_Printer_Paper_Ream:.2f}"
    if Total_Printer_Paper_Case > 0:
        Receipt_Content += f"\n{Quantity_Printer_Paper_Case} Printer Paper Case(s) purchased for ${Total_Printer_Paper_Case:.2f}\n"
    Receipt_Content += "\n" + "-" * 45
    Receipt_Content += f"\n({total_items}) Total Items Ordered"
    Receipt_Content += f"\nSubtotal: ${Subtotal:.2f}"
    if Discount > 0:
        Receipt_Content += f"\nDiscount (5.0%): -${Discount:.2f}"
    Receipt_Content += f"\nSales Tax (6.0%): ${Sales_Tax_Fee:.2f}"
    Receipt_Content += "\n" + "=" * 45 
    Receipt_Content += f"\nTotal Charge: ${Total_Charge:.2f}\n"
    Receipt_Content += "=" * 45 + "\n"
    Receipt_Content += "\tThank you for your business!\n"
    Receipt_Content += "=" * 45 + "\n"
    
    return Receipt_Content

#Function to Save the content of the Receipt to a file
#Paremeters: Generate_Receipt (string)
#Return: None
def SaveReceiptToFile(Receipt_Content):
    save_receipt = input("\nWould you like to save your receipt to a file? (yes/no): ")
    while save_receipt not in ["yes", "y", "no", "n"]:
        print("Error - Please enter (yes) or (no).")
        save_receipt = input("\nWould you like to save your receipt to a file? (yes/no): ")
    if save_receipt in ["yes", "y"]:
        bFlag = True
        while bFlag:
            file_path = input("Enter the file name and path to save the receipt: ")
            try:
                file = open(file_path, 'a')
                file.write(Receipt_Content)
                #Close the file
                file.close()
                bFlag = False
            except FileNotFoundError:
                print("Error - unable to open file. Please reenter.") 
    
def invoice():
    DispProducts()
    First_Name, Last_Name, Street_Address, City, State, Zip_Code, Purchase_Order_Number = Customer_Management()
    Inventory = inventory()
    Subtotal, total_items, Quantity_Printer_Ink, Total_Printer_Ink, Quantity_Backpack, Total_Backpack, Quantity_Pen, Total_Pen, Quantity_Printer_Paper_Ream, Total_Printer_Paper_Ream, Quantity_Printer_Paper_Case, Total_Printer_Paper_Case = Customer_Purchase(Inventory)
    Subtotal, Discount = Value_Customer_Discount(Subtotal)
    Sales_Tax_Fee = Sales_Tax_Calculations(Subtotal)
    Total_Charge = Subtotal + Sales_Tax_Fee
    Receipt_Content = Generate_Receipt(First_Name, Last_Name, Street_Address, City, State, Zip_Code, Purchase_Order_Number, Quantity_Printer_Ink, Total_Printer_Ink, Quantity_Backpack, Total_Backpack, Quantity_Pen, Total_Pen, Quantity_Printer_Paper_Ream, Total_Printer_Paper_Ream, Quantity_Printer_Paper_Case, Total_Printer_Paper_Case, total_items, Subtotal, Discount, Sales_Tax_Fee, Total_Charge)
    print(Receipt_Content)
    SaveReceiptToFile(Receipt_Content)

main()
