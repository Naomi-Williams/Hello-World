#Naomi Williams
#2/6/2025
#Sales Tax Program
#Get the amount of the purchase from user
amount_of_purchase = float(input("Enter the amount of purchase:$"))

#Assign the state and county sales tax
state_sales_tax_percent = 0.05
county_sales_tax_percent = 0.025

#Calculate the state & county sales tax
state_sales_tax = amount_of_purchase * state_sales_tax_percent
county_sales_tax = amount_of_purchase * county_sales_tax_percent

#Calculate the total sales tax
total_sales_tax = state_sales_tax + county_sales_tax

#Calculate the total sale
total_sale = amount_of_purchase + total_sales_tax

#Display the results of calculations
print(f"Amount of purchase: {amount_of_purchase:.2f}")
print(f"State sales tax: {state_sales_tax:.2f}")
print(f"County sales tax: {county_sales_tax:.2f}")
print(f"Total sales tax: {total_sales_tax:.2f}")
print(f"Total sale: {total_sale:.2f}")