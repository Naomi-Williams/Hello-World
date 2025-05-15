#Naomi williams
#2/28/2025
#Sales Tax Program Refactoring
#Constants for program
STATE_SALES_TAX_PERCENT = 0.05
COUNTY_SALES_TAX_PERCENT = 0.025

#Create function to get the amount of the purchase from user to calculate the sales tax
def main():
    #Ask user to input purchases
    amount_of_purchase = float(input("Enter the amount of purchase:$"))
    
    #Validate that the input is not less than zero
    while amount_of_purchase <= 0:
        amount_of_purchase = float(input("Enter the amount of purchase: $"))
    print(f"Amount of purchase: {amount_of_purchase:.2f}")
    
    #Display state sales tax of amount
    state_sales_tax = calculate_state_tax(amount_of_purchase)
    
    #Display county sales tax of amount
    county_sales_tax = calculate_county_tax(amount_of_purchase)
    
    #Display total sales tax of amount
    total_sales_tax = calculate_total_sales_tax(state_sales_tax, county_sales_tax)
    
    #Display total sale amount including taxes 
    total_sale = Calculate_Total_Sales(amount_of_purchase, total_sales_tax)
    
    #Display the output of all the calculations
    Display_output = display_output(amount_of_purchase, state_sales_tax, county_sales_tax, total_sales_tax, total_sale)
    


#Calculate the state & county sales tax
#Function for calculating state sales tax
def calculate_state_tax(amount_of_purchase):
    state_sales_tax = amount_of_purchase * STATE_SALES_TAX_PERCENT
    return state_sales_tax
#Function for county sales tax
def calculate_county_tax(amount_of_purchase):
    county_sales_tax = amount_of_purchase * COUNTY_SALES_TAX_PERCENT
    return county_sales_tax
#Function for total sales tax
def calculate_total_sales_tax(state_sales_tax, county_sales_tax):
    #Calculate the total sales tax
    total_sales_tax = state_sales_tax + county_sales_tax
    return total_sales_tax
#Function for total sales amount including total tax
def Calculate_Total_Sales(amount_of_purchase, total_sales_tax):
    #Calculate the total sale
    total_sale = amount_of_purchase + total_sales_tax
    return total_sale
#Function to display all the calculate values
def display_output(amount_of_purchase, state_sales_tax, county_sales_tax, total_sales_tax, total_sale):
    print(f"State sales tax: {state_sales_tax:.2f}")
    print(f"County sales tax: {county_sales_tax:.2f}")
    print(f"Total sales tax: {total_sales_tax:.2f}")
    print(f"Total sale: {total_sale:.2f}")
#Calling Back to main()
main()