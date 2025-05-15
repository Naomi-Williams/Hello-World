#Naomi Williams
#4/9/2025
#Total Sales Program
#main function to calculate total weekly sales
#Parameters - None
#Return - None
def main():
    #Declare a List to store the sales for each day
    Sales_Of_Week = []        #empty list
    Days_Of_Week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    
    #Loop to get the sales input for each day
    for day in Days_Of_Week:
        sale = InputValidation(day)             #Assigned and called the InputValidation function to the main
        Sales_Of_Week.append(sale)              #Append or combing the values inside the list
        
    #Calculate the total sales  of the week by using the sum function on the Sales_Of_Week list
    Total_Sales = sum(Sales_Of_Week)
    
    #Display the results of the program
    print(f"\nTotal Weekly Sales: ${Total_Sales:.2f}")
        
    
#Function to get the valid input of the sales of each day
#Parameter - the days of the week
#Return - None
def InputValidation(day):
    #Ask the user to input the sales of each day of the week
    sale = input(f"Enter the sales for {day}: $")
    valid = True
    while valid:
        try: 
            #turn the input type into a float using the variable sale
            Sale_Float = float(sale)
            if Sale_Float < 0:                                          #Makes sure that the input is not negative
                print("Sales cannot be negative. Please reenter.")
                sale = input(f"Enter the sales for {day}: $")
            else:
                valid = False                                           #Set to False when input is valid
        except ValueError:                                              #Make sure that the input by the user is a numerical value and not a string 
            print("Invalid input. Please enter a numerical value.")
            sale = input(f"Enter the sales for {day}: $")
    return Sale_Float
        
main()
    
        
                     
        
    
    