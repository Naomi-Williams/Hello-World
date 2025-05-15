#Naomi Williams
#4/9/2025
#Number Analysis Program
#Main function to display the program
#Parameter - None
#Return - Display the results of the program
def main():
    #Declare a list to store the sales
    numbers = []
    #Display to user to input 20 Numbers
    print("Please Enter 20 Numbers:")
    for i in range(20):
        num = InputValidation(f"Enter number {i + 1}: ")   #Validates the input and gets the input for the 20 numbers and changes everytime by adding 1 to i
        numbers.append(num)                                #adds the numbers inputed from num to the numbers list
        
    #Calculate the lowest and highest number in the list
    lowest_num = min(numbers)
    highest_num = max(numbers)
    #Calculate the total of the numbers in the list
    total_num = sum(numbers)
    #Calculate the average of the numbers in the list
    average_num = total_num / len(numbers)
    
    #Display the results of the calculations
    print(f"\nLowest Number: {lowest_num:.2f}")
    print(f"Highest Number: {highest_num:.2f}")
    print(f"Total: {total_num:.2f}")
    print(f"Average: {average_num:.2f}")
    
#Function to validte the input of the users 20 numbers
def InputValidation(prompt):
    valid = True
    while valid:
        try:
            num = float(input(prompt))    #Convert the input into a float
            valid = False                 #Input is valid
        except ValueError:
            print("Invalid Input. Please enter a numerical value.")
    return num   
    
#Call the main function to display the program    
main()