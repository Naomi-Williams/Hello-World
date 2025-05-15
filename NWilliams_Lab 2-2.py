#Naomi Williams
#2/09/2025
#Bookstore Point of Sale System Program
#Variables For Products
Backpack_Price = 45.95
Pen_Price = 0.78
Printer_Ink_Price = 41.95
Printer_Paper_Price = 6.00

#Get Input about the Users purchase
print("Entry System for Bookstore Supplies")

First_Name = input("Customers First Name: ")
Last_Name = input("Customers Last Name: ")
Purchase_Order_Number = int(input("PO Number: "))
Printer_Ink_Quantity = int(input("Printer Ink Quantity: "))
Backpack_Quantity = int(input("Backpack Quantity: "))
Printer_Paper_Quantity = int(input("Printer Paper Quantity: "))
Pen_Quantity = int(input("Pen Quantity: "))

print("*" * 22)

#Customer Information & Specicial Order Number

Customer_Name = f"{Last_Name.capitalize()}, {First_Name.capitalize()}"
Generated_Order_Number = f"{Last_Name[0].upper()}{First_Name[0].upper()}_{Purchase_Order_Number}"

#Calculate The Customers Purchase

Total_Backpacks = Backpack_Quantity * Backpack_Price
Total_Pen = Pen_Quantity * Pen_Price
Total_Printer_Ink = Printer_Ink_Quantity * Printer_Ink_Price
Total_Printer_Paper = Printer_Paper_Quantity * Printer_Paper_Price
Total_Charge = (Printer_Ink_Quantity * Printer_Ink_Price)\
               + (Backpack_Quantity * Backpack_Price)\
               + (Printer_Paper_Quantity * Printer_Paper_Price)\
               + (Pen_Quantity * Pen_Price)
Sales_Tax_Fee = Total_Charge * 0.06
Total_Invoice = Total_Charge + Sales_Tax_Fee

#Display Order Information

print("PURCHSE ORDER INVOICE")
print(f"Customer Name: {Customer_Name}")
print(f"Original Purchase Order Number: {Purchase_Order_Number}")
print(f"PO: {Generated_Order_Number}")
print(f"Printer Ink: ${Total_Printer_Ink:.2f}")
print(f"Backpacks: ${Total_Backpacks:.2f}")
print(f"Printer Paper: ${Total_Printer_Paper:.2f}")
print(f"Pens: ${Total_Pen:.2f}")
print(f"SubTotal Charge: ${Total_Charge:.2f}")
print(f"Sales Tax: ${Sales_Tax_Fee:.2f}")
print(f"Total: ${Total_Invoice:.2f}")
