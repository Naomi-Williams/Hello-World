#Naomi Williams
#4/1/2025
#Average of numbers program
#Function to calculate the average of the numbers in the file
#Parameters - None
#Return - The average of the numbers inside the file
def ReadData():
    #open the file
    myfile = open('c:\\test\\numbers.txt', 'r')                 #Points to where on the hard drive the file is located
    
    #Create a variable to hold the sum and count
    total = 0
    count = 0
    
    #Read and Display the file's content
    print("Numbers in the file: ")                           
    for line in myfile:                                        
        number = int(line.strip())                             #removes the empty spaces
        print(number)                                          #Displays the numbers inside the file
        total += number                                        #Add the numbers in the file together and assign to the variable total
        count += 1                                             #Add 1 to the variable to keep track of the count data
        
    #Close the file
    myfile.close()
    
    if count > 0:                                              #Makes sure that the program dosen't divide by zero
        average = total / count                                #Calculates the average by dividing the total by the count
        print(f"The average of the number is: {average:.2f}")  #Displays the average to the screen
    else:
        print("\nThe file is empty. There are no numbers to calculate the average.")     #In the case that no numbers are inside the file diplay can't calculate the average
        
    return average
    

#Main function to display the average of numbers program
def main():
    #Display the average of the numbers.txt file
    average = ReadData()
    
        
#Call the main function back to display the program
main()
        
    
    