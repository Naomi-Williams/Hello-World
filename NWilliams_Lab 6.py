#Naomi Williams
#4/3/2025
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
    Zip_Code = int(input("Zip Code: "))
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

def Validate_Quantity_Input(item_name):                                  #Input Validation function
    #Creating a loop flag
    bFlag = True
    while bFlag:                                                         #Catches the exceptions when validating
        try: #Test for right data type
            quantity = int(input(f"{item_name}"))
            if quantity < 0:
                print("Error: The quantity cannot be negative.")
            else:
                bFlag = False                                            #END THE LOOP
        except ValueError:
            print("\nError - this is not an integer number - Please reenter")
    return quantity
    
def Customer_Purchase():                                                               #Function for Calculating Totals of Customer Purchase, AND Validating input of the quantity      
    #Initializing running subtotal
    Running_Subtotal = 0    
    #Input Validation Printer Paper, Total price, & Running Subtotal
    Printer_Ink_Quantity = Validate_Quantity_Input("Printer Ink Quantity: ")
    Total_Printer_Ink = Printer_Ink_Quantity * PRINTER_INK_PRICE
    Running_Subtotal += Total_Printer_Ink
    print(f"Running Subtotal: ${Running_Subtotal:.2f}")
    #Input Validation Backpack, Total price & Running Subtotal
    Backpack_Quantity = Validate_Quantity_Input("Backpack Quantity: ")
    Total_Backpack = Backpack_Quantity * BACKPACK_PRICE    
    if Backpack_Quantity >= BACKPACK_DISCOUNT_QUANTITY:                    #10% Discount when user buys 3 or more backpacks
        Total_Backpack *= BACKPACK_DISCOUNT_PERCENTAGE
    Running_Subtotal += Total_Backpack
    print(f"Running Subtotal: ${Running_Subtotal:.2f}")
    #Input Validation Pens & Running Subtotal
    Pen_Quantity = Validate_Quantity_Input("Pen Quantity: ")
    #Apply discount based on Quantity purchased
    if Pen_Quantity <= 5:
        Total_Pen = Pen_Quantity * PEN_PRICE_FIVE_OR_FEWER
    elif Pen_Quantity <= 10:
        Total_Pen = Pen_Quantity * PEN_PRICE_SIX_TO_TEN
    else:
        Total_Pen = Pen_Quantity * PEN_PRICE_ELEVEN_OR_MORE
    Running_Subtotal += Total_Pen
    print(f"Running Subtotal: ${Running_Subtotal:.2f}")
    #Input Validation Printer Paper & Running Subtotal
    Paper_Type = input("Did you buy the printer paper by ream or case (ream/case): ")
    while Paper_Type not in ["ream", "case"]:                                                          #Validate Input for ream or case
        print("Error - please enter (ream) or (case)")
        Paper_Type = input("Did you buy the printer paper by ream or case (ream/case): ")
        #Input Validation of printer paper
    if Paper_Type == "ream":
        Printer_Paper_Quantity = Validate_Quantity_Input("Enter Quantity of printer paper ream: ")
        Total_Printer_Paper = Printer_Paper_Quantity * PRINTER_PAPER_REAM_PRICE
    else:
        Printer_Paper_Quantity = Validate_Quantity_Input("Enter Quantity of printer paper case: ")
        Total_Printer_Paper = Printer_Paper_Quantity * PRINTER_PAPER_CASE_PRICE
    Running_Subtotal += Total_Printer_Paper
    print(f"Running Subtotal: ${Running_Subtotal:.2f}")    
    Total_count = Printer_Ink_Quantity + Backpack_Quantity + Pen_Quantity + Printer_Paper_Quantity     #Track the number of items purchased
    print(f"Total items purchased: {Total_count}")
    print(f"Final Running Subtotal: ${Running_Subtotal:.2f}")                                          #Display Final Running Subtotal
    
    print("\n")
    print("=" * 45)
    return Running_Subtotal, Total_count, Printer_Ink_Quantity, Total_Printer_Ink, Backpack_Quantity, Total_Backpack, Pen_Quantity, Total_Pen, Printer_Paper_Quantity, Total_Printer_Paper

def Value_Customer_Discount(Running_Subtotal):                       #Calculate Running Subtotal, Applying the Discount
    Discount = 0
    if Running_Subtotal > 499.99:
        Discount = Running_Subtotal * DISCOUNT_VALUE_CUSTOMER        # 5% Discount for valued customers
        Running_Subtotal -= Discount                                 # Subtract the Discount from the Subtotal
    return Running_Subtotal, Discount

def Sales_Tax_Calculations(Running_Subtotal): #Calculate Sales tax
    Tax_Free_Week = input("Is it Maryland's Tax-Free Week? (yes/no): ")           #Ask if its Maryland's Sales Tax Free Week
    #Input validation for customer decision to use Maryland's Tax free week
    while Tax_Free_Week not in ["yes", "no", "y", "n"]:
        print("Error - Please enter (yes) or (no).")
        Tax_Free_Week = input("Is it Maryland's Tax-Free Week? (yes/no): ")
    if Tax_Free_Week in ["yes", "y"]:                                             #If the answer inputed by the user is yes or y then the sales tax will return 0
        print("\nNo sales tax applied to your total. It is Marylands sales tax week. ")
        return 0
    return Running_Subtotal * SALES_TAX_RATE                                      #If the Tax_Free_week is no then multiply the Running subtotal by the Sales tax rate to get taxed amount

def Generate_Receipt(First_Name, Last_Name, Street_Address, City, State, Zip_Code, Purchase_Order_Number, Running_Subtotal, Total_count, Discount, Sales_Tax_Fee, Total_Printer_Ink, Total_Backpack, Total_Pen, Total_Printer_Paper, Total_Charge, Printer_Ink_Quantity, Backpack_Quantity, Pen_Quantity, Printer_Paper_Quantity):       
    #Customer information Citation: https://www.geeksforgeeks.org/how-to-capitalize-first-character-of-string-in-python/
    Generated_Order_Number = f"{Last_Name[0].capitalize()}{First_Name[0].capitalize()}_{Purchase_Order_Number}"
    Customer_Name = f"{Last_Name.capitalize()}, {First_Name.capitalize()}"
    
    Receipt_Content = "\n"
    Receipt_Content += "=" * 45
    Receipt_Content += "\nCustomer information"
    Receipt_Content += f"\nName: {Customer_Name}"
    Receipt_Content += f"\nAddress: {Street_Address}, {City}, {State} {Zip_Code}"
    Receipt_Content += f"\nPO: {Generated_Order_Number}\n"
    Receipt_Content += "-" * 45   
    if Printer_Ink_Quantity > 0:
        Receipt_Content += f"\nPrinter Ink: ${Total_Printer_Ink:.2f}"
    if Backpack_Quantity > 0:
        Receipt_Content += f"\nBackpacks: ${Total_Backpack:.2f}"
    if Pen_Quantity > 0:
        Receipt_Content += f"\nPen: ${Total_Pen:.2f}\n"
    if Printer_Paper_Quantity > 0:
        Receipt_Content += f"Printer Paper: ${Total_Printer_Paper:.2f}\n"
    Receipt_Content += "-" * 45 + "\n"
    Receipt_Content += f"({Total_count}) Total Items Ordered"
    Receipt_Content += f"\nSubtotal: ${Running_Subtotal:.2f}"
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
    Running_Subtotal, Total_count, Printer_Ink_Quantity, Total_Printer_Ink, Backpack_Quantity, Total_Backpack, Pen_Quantity, Total_Pen, Printer_Paper_Quantity, Total_Printer_Paper = Customer_Purchase()
    Running_Subtotal, Discount = Value_Customer_Discount(Running_Subtotal)
    Sales_Tax_Fee = Sales_Tax_Calculations(Running_Subtotal)
    Total_Charge = Running_Subtotal + Sales_Tax_Fee
    Receipt_Content = Generate_Receipt(First_Name, Last_Name, Street_Address, City, State, Zip_Code, Purchase_Order_Number, Running_Subtotal, Total_count, Discount, Sales_Tax_Fee, Total_Printer_Ink, Total_Backpack, Total_Pen, Total_Printer_Paper, Total_Charge, Printer_Ink_Quantity, Backpack_Quantity, Pen_Quantity, Printer_Paper_Quantity)
    print(Receipt_Content)
    SaveReceiptToFile(Receipt_Content)

main()