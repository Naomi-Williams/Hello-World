#Naomi Williams
#2/17/2025
#Bookstore Point Of Sale System Program Updated
#Constants For Products
BACKPACK_PRICE = 45.95
PEN_PRICE_FIVE_OR_FEWER = 0.78
PEN_PRICE_SIX_TO_TEN = 0.68
PEN_PRICE_ELEVEN_OR_MORE = 0.58
PRINTER_INK_PRICE = 41.95
PRINTER_PAPER_REAM_PRICE = 6.00
PRINTER_PAPER_CASE_PRICE = 25.00
SALES_TAX_RATE = 0.06

#Purchase Options For Customers
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

#Get Input about the Users purchse
First_Name = input("\nCustomers First Name: ")
Last_Name = input("Customers Last Name: ")
Purchase_Order_Number = int(input("PO Number: "))
Printer_Ink_Quantity = int(input("Printer Ink Quantity: "))
Backpack_Quantity = int(input("Backpack Quantity: "))
Pen_Quantity = int(input("Pen Quantity: "))
Paper_Type = input("Did you buy the printer paper by ream or case (ream/case): ")
if Paper_Type == "ream":
    Printer_Paper_Quantity = int(input("Enter Quantity of printer paper ream: "))
else:
    Printer_Paper_Quantity = int(input("Enter Quantity of printer paper case: "))
print("\n")
print("=" * 45)

#Calculate cost for products purchased
Total_Printer_Ink = Printer_Ink_Quantity * PRINTER_INK_PRICE
Total_Backpack = Backpack_Quantity * BACKPACK_PRICE
if Backpack_Quantity >= 3:
    Total_Backpack *= 0.9                     #10% Discount when user buys 3 or more backpacks
if Paper_Type == "ream":
    Total_Printer_Paper = Printer_Paper_Quantity * PRINTER_PAPER_REAM_PRICE
else:
    Total_Printer_Paper = Printer_Paper_Quantity * PRINTER_PAPER_CASE_PRICE
if Pen_Quantity <= 5:
    Total_Pen = Pen_Quantity * PEN_PRICE_FIVE_OR_FEWER
elif Pen_Quantity <= 10:
    Total_Pen = Pen_Quantity * PEN_PRICE_SIX_TO_TEN
else:
    Total_Pen = Pen_Quantity * PEN_PRICE_ELEVEN_OR_MORE
    
#Calculate total cost, subtotal, and sales tax
Subtotal = Total_Printer_Ink + Total_Backpack + Total_Printer_Paper + Total_Pen
Sales_Tax_Fee = Subtotal * SALES_TAX_RATE
Total_Charge = Subtotal + Sales_Tax_Fee

#Customer information Citation: https://www.geeksforgeeks.org/how-to-capitalize-first-character-of-string-in-python/  
Generated_Order_Number = f"{Last_Name[0].capitalize()}{First_Name[0].capitalize()}_{Purchase_Order_Number}"
Customer_Name = f"{Last_Name.capitalize()}, {First_Name.capitalize()}" 

#Generate Receipt
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

print(f"Subtotal: ${Subtotal:.2f}")
print(f"Sales Tax (6.0%): ${Sales_Tax_Fee:.2f}")
print("=" * 45)

print(f"Total Charge: ${Total_Charge:.2f}")
print("=" * 45)




