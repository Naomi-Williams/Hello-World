#Naomi Williams
#4/22/2025
#Sum of Digits in a String Program
#Function to display what happens in the program
#Parameter - None
#Return - None
def main():
    #Defining the start of the loop
    bFlag = True
    #Initialize variable to hold the sum
    total_sum = 0
    while bFlag:
        try:
            #Ask the user to input a series of single-digit numbers
            SumNum = input("Enter a series of single-digit numbers with no seperators: ")
            #Going over all the numbers in the string and converting them to intergers to add to the accumalator total_sum
            for digits in SumNum:
                total_sum += int(digits)
            print(f"The sum of the digits is: {total_sum}")
            #End the loop
            bFlag = False
        #Catches exception of the user entering a string that doesn't have numerical values
        except ValueError:
            print("Error - Please input a numerical-value. Please reenter.")
    

#Calling main function
main()
