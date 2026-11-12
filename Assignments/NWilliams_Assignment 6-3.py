#Naomi Williams
#4/1/2025
#Exception Handling
#Main Function to display the program
def ReadData():
    try:
        #Open the file
        myfile = open('c:\\test\\numbers.txt', 'r')
    except IOError:
        print("Error - Unable to open or read the file. Please ensure the file exsits and is accessible ")
        
    #Create a variable to hold the sum and the count
    total = 0
    count = 0 
    try: 
        #Read and Display the file's content
        print("Numbers in the file:")
        for line in myfile:
            try:
                number = int(line.strip())
                print(number)
                total += number
                count += 1
            except ValueError:
                print(f"Non-numeric value found and skipped: '{line.strip()}'")
    finally:                       #This will always execute even if an exception is raised
        #close the file
        myfile.close()
    
    #Calculte and display the average of the numbers in the file
    if count > 0:                                              #Makes sure that the program dosen't divide by zero
        average = total / count                                #Calculates the average by dividing the total by the count
        print(f"The average of the number is: {average:.2f}")  #Displays the average to the screen
    else:
        print("\nThe file is empty. There are no numbers to calculate the average.")     #In the case that no numbers are inside the file diplay can't calculate the average
        
    return average
            
#Call the main function back to display the program
def main():
    #Call the ReadData function to display its contents
    average = ReadData()
    
#Call the main function back    
main()
