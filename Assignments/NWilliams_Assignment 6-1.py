#Naomi Williams
#4/1/2025
#File Display Program
#Function to open a file and display the numbers inside of it
#Parameter - none
#Return - The numbers inside the file
#Main Function to display the program
def main():
    #Open the file
    myfile = open('c:\\test\\numbers.txt', 'r')   #Points to where on the hard drive is the numbers.txt file is located
    
    #Read and display the file's contents
    print("Numbers in the file: ")
    for line in myfile:
        number = int(line.strip())                #Removes the empty spaces and turns the strings to integers
        print(number)                             #prints the output of the file
        
    #Close the file
    myfile.close()
        
main()
