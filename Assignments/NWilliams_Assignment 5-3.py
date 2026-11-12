#Naomi Williams
#3/1/2025
#Feet to inches program
#Constants inside of problem
INCHES_IN_FOOT = 12
#Create fuction to ask user to input a number a feet so that it can be converted to inches
def main():
    #Ask user to input amount of feet
    feet = int(input("Enter the amount of feet: "))
    
    #Validate that the input is greater than zero
    while feet <= 0:
        print("Error - Enter a number greater than zero")
        feet = int(input("Enter the amount of feet: "))
    
    #Display the converted feet to inches
    print(feet, "feet equals", feet_to_inches(feet), "in inches")
    
#Function to convert feet to inches
def feet_to_inches(feet):
    return feet * INCHES_IN_FOOT
 

#Calling the main function
main()
