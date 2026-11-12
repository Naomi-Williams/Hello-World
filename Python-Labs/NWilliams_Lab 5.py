#Naomi Williams
#3/10/2025
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
    #Input Validation PO Number
    Purchase_Order_Number = int(input("PO Number: "))
    while Purchase_Order_Number <= 0:
        #Validate that Order number is greater than zero
        print("Error: The Order Number must be greater than zero.")
        Purchase_Order_Number = int(input("PO Number: "))
    return First_Name, Last_Name, Purchase_Order_Number

def Validate_Quantity_Input(item_name):                                  #Input Validation function
    quantity = int(input(f"{item_name}"))
    while quantity < 0:
        print("Error: The quantity cannot be negative.")
        quantity = int(input(f"{item_name}"))
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

def Sales_Tax_Calculations(Running_Subtotal):                        #Calculate Sales tax
    return Running_Subtotal * SALES_TAX_RATE

def Generate_Receipt(First_Name, Last_Name, Purchase_Order_Number, Running_Subtotal, Total_count, Discount, Sales_Tax_Fee, Total_Printer_Ink, Total_Backpack, Total_Pen, Total_Printer_Paper, Total_Charge, Printer_Ink_Quantity, Backpack_Quantity, Pen_Quantity, Printer_Paper_Quantity):       
    #Customer information Citation: https://www.geeksforgeeks.org/how-to-capitalize-first-character-of-string-in-python/
    Generated_Order_Number = f"{Last_Name[0].capitalize()}{First_Name[0].capitalize()}_{Purchase_Order_Number}"
    Customer_Name = f"{Last_Name.capitalize()}, {First_Name.capitalize()}"    
    print("\n")                                                        
    print("Customer informaton")
    print(f"Name: {Customer_Name}")
    print(f"PO: {Generated_Order_Number}")
    print("-" * 45)    
    if Printer_Ink_Quantity > 0:
        print(f"Printer Ink: ${Total_Printer_Ink:.2f}")
    if Backpack_Quantity > 0:
        print(f"Backpacks: ${Total_Backpack:.2f}")
    if Pen_Quantity > 0:
        print(f"Pen: ${Total_Pen:.2f}")
    if Printer_Paper_Quantity > 0:
        print(f"Printer Paper: ${Total_Printer_Paper:.2f}")
    print("-" * 45)
    print(f"({Total_count}) Total Items Ordered")
    print(f"Subtotal: ${Running_Subtotal:.2f}")
    if Discount > 0:
        print(f"Discount (5.0%): -${Discount:.2f}")
    print(f"Sales Tax (6.0%): ${Sales_Tax_Fee:.2f}")
    print("=" * 45)
    print(f"Total Charge: ${Total_Charge:.2f}")
    print("=" * 45)
    print(f"\tThank you for your business!")
    print("=" * 45)
    
def invoice():
    DispProducts()
    First_Name, Last_Name, Purchase_Order_Number = Customer_Management()
    Running_Subtotal, Total_count, Printer_Ink_Quantity, Total_Printer_Ink, Backpack_Quantity, Total_Backpack, Pen_Quantity, Total_Pen, Printer_Paper_Quantity, Total_Printer_Paper = Customer_Purchase()
    Running_Subtotal, Discount = Value_Customer_Discount(Running_Subtotal)
    Sales_Tax_Fee = Sales_Tax_Calculations(Running_Subtotal)
    Total_Charge = Running_Subtotal + Sales_Tax_Fee
    Generate_Receipt(First_Name, Last_Name, Purchase_Order_Number, Running_Subtotal, Total_count, Discount, Sales_Tax_Fee, Total_Printer_Ink, Total_Backpack, Total_Pen, Total_Printer_Paper, Total_Charge, Printer_Ink_Quantity, Backpack_Quantity, Pen_Quantity, Printer_Paper_Quantity)

main()
