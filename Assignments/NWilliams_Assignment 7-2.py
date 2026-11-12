#Naomi Williams
#4/9/2025
#Rainfall Statistics Program
#Main function to Display the entire output of the program
#Parameter - None
#Return - None
def main():
    #declare a list for the amount of rainfall
    Rainfall = [] #Empty list
    #A list of the names of the 12 months in a year
    Months_In_Year = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November",
                      "December"]
    
    #Loop to get amount of rainfall input for each month
    for month in Months_In_Year:
        Rain_Month = InputValidation(month)
        Rainfall.append(Rain_Month)
        
    #Calculate total Rainfall
    Total_Rainfall = sum(Rainfall)
    
    #Calculate average monthly rainfall
    Average_Rainfall = Total_Rainfall / len(Rainfall)                     #Uses the len function to calculate the number of items inside the list
    
    #Identifying the months with the highest and lowest amounts of rainfall
    Max_Rainfall = max(Rainfall)
    Min_Rainfall = min(Rainfall)
    Max_Month = Months_In_Year[Rainfall.index(Max_Rainfall)]
    Min_Month = Months_In_Year[Rainfall.index(Max_Rainfall)]
    
    #Display the results of the calculation
    print(f"\nTotal Rainfall for the year: {Total_Rainfall:.2f} inches.")
    print(f"Average Monthly Rainfall: {Average_Rainfall:.2f} inches.")
    print(f"Months with Highest amount of Rainfall: {Max_Month} {Max_Rainfall:.2f} inches.")
    print(f"Months with lowest amount of Rainfall: {Min_Month} {Min_Rainfall:.2f} inches.")
        
    
   
#Function to get valid input of the amount of rainfall each month
#Parameter - The name of the month
#Return - the input of the rain_float variable
def InputValidation(month):
    #Ask the user for the amount of rainfall for each month
    Rain_Month = input(f"Enter the total rainfall for {month}: ")
    valid = True
    while valid:
        try:
            #turn the input into a float using the variable Rain_Month
            rain_float = float(Rain_Month)
            if rain_float < 0:
                print("The amount of Rainfall cannot be negative. Please reenter.")
                Rain_Month = input(f"Enter the total rainfall for {month}: ")
            else:
                valid = False                                                         #Set to false if input is valid
        except ValueError:                                                            #Make sure that the input is a numerical value and doesn't cause a crash
            print("Invalid input. Please enter a numerical value.")
            Rain_Month = input(f"Enter the total rainfall for {month}: ")
    return rain_float     #Return valid rainfall amount
              
#Call the main function to get the output of the program
main() 
