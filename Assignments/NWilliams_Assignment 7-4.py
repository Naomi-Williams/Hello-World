#Naomi Williams
#4/11/2025
#Rewrite of number analysis program
#Function to get valid input of the Users file
def valFilePath():
    #Declare a list to hold the data from the file
    numbers = [] #Empty list
    
    #Prompt the user to enter file path and name and validate that it can be reached
    bFlag = True
    while bFlag:
        try:  #Test that the file exist and can be read
            #Asking the customer to input the file path and name
            FileName = input("Enter in the name and path of the file: ")
            file = open(FileName, 'r')
            for line in file:
                #Turning the numbers in the file to float and appending them to the list
                numbers.append(int(line.strip())) 
            file.close()
            bFlag = False
        except FileNotFoundError:
            print("Error - Cannot find this file. Please reenter.")
            
    return numbers
#Function to calculate and display the information about the list
#Parameter - information from the list numbers
#Return - Display the results of the calculations
def Display_Data(numbers):
    #Calculate the total of the numbers in the list
    Total_num = sum(numbers)
    #Calculate the total number of negative values in the list
    #loop through the list and create a varaible to count how many are either negative or positive
    #Negative number counter
    Negative_num = 0
    for num in numbers:
        if num < 0:
            Negative_num += 1
    #Calculate the total number of positive values in the list
    Positive_num = 0
    for num in numbers:
        if num > 0:
            Positive_num += 1
    #Calculate the average of the numbers in the list
    Average_num = Total_num / len(numbers)
    
    #Display the highest and lowest value in the list
    Max_num = max(numbers)
    Min_num = min(numbers)
    #Calculate the average of the first 10 numbers in the list using list splicing and the sum and len functions
    First10_num = sum(numbers[0:10]) / len(numbers[0:10])
    #Display the Highest and Lowest Numbers in the list
    First10_MaxNum = max(numbers[0:10])
    First10_MinNum = min(numbers[0:10]) 
    
    #Display the results of the calculations
    print(f"\nTotal of Numbers: {Total_num}")
    print(f"Total of Negative Numbers: {Negative_num}")
    print(f"Total of Positive Numbers: {Positive_num}")
    print(f"Average of Numbers: {Average_num:.2f}")
    print(f"Highest Number: {Max_num}")
    print(f"Lowest Number: {Min_num}")
    #Display the average of the first 10 numbers of the list and the highest and lost numbers in the list
    print(f"Average First 10 Numbers: {First10_num:.2f}")
    print(f"Highest Number of First 10: {First10_MaxNum}")
    print(f"Lowest Number of First 10: {First10_MinNum}")
    
#Function to sort the file, then reverse it and Display the reversed list, output the reverse list to a file and validate the path.
#Parameter - the list numbers
#Return - the output of the list
def Sorted_List(numbers):
    #Declare a list for the sorted acending list of numbers
    numbers2 = []                                                     #empty list
    numbers.sort()                                                    #Sort the list in ascending order or from lowest to highest
    for i in numbers:                                                 #Appending the sorted numbers from the list to a new list 
        numbers2.append(i)    
    numbers2.reverse()                                                #Sort the numbers in the new list from ascending to descending
    print(f"\nReversed Sorted List: {numbers2}")                      #Display the new list to the Display
    #Write the reverse list to a file
    #Ask the User for the file path and name
    bFlag = True
    while bFlag:
        try:
            FileName = input("Enter in the name and path for the output file: ")
            file = open(FileName, 'w')
            for num in numbers2:
                file.write(f"{num}\n")
            file.close()
            bFlag = False
            print(f"\nThe Reverse Sorted List was written to the {FileName} file path.")
        except FileNotFoundError:
            print("Invalid file path and name. Please reenter.")
            FileName = input("Enter in the name and path for the output file: ")
    
    return numbers

#Function Ask the user to enter in the position of a number that they want to change and update the list
#Parameters - The numbers inside the list
#Return - Return and display the updates list
def Updated_List(numbers):
    #Ask the user to choose which position of a number they want to change
    print(f"Original List: {numbers}")
    bFlag = True
    while bFlag:
        try:
            #Validate the input by the user
            ind = int(input("Enter in the position of a number that you want to change (1-25): "))
            if 1 <= ind <= len(numbers): #Validating the range for the input by the user: if input is greater than and equal to 1 and less than and equal to the length of the list
                bFlag = False            #stop the loop if the input is valid
            else: #Ask the user to input a number to change
                print("Error - INVALID input. Please reenter a number that is in range.")
                ind = int(input("Enter in the position of a number that you want to change (1-25): "))
        except ValueError:               #Looks out for invalid input of non-numerical values
            print("Error - Invalid input. Please reenter a numerical value.")
    #Validate the new number being put in by user
    bFlag2 = True
    while bFlag2:
        try:
            newNum = int(input("Enter the new number: "))
            numbers[ind-1] = newNum                                #Accounting for the way a user would count instead of starting at 0 they start at 1 
            bFlag2 = False                                         #Stops the loop if the users input is valid
        except ValueError:
            print("Error - Invalid input. Please reenter a numerical value.")
        
    print(f"Updated list: {numbers}")
    
    return ind, newNum
     
#Main Function to display the program
#Parameters - None
#Return - None
def main():
    #Validate the filename and path
    numbers = valFilePath()
    
    #Display the calculations
    Display_Data(numbers)
    
    #Display the reverse sorted list and output it to a file
    Sorted_List(numbers)
    
    #Display the updated orginal list
    Updated_List(numbers)
    
    #Display the exit messege
    print("\nThank you for using this program")
    
main()
