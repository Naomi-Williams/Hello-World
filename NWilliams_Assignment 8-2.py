#Naomi Williams
#4/22/2025
#Vowels and Consonants Program
#Main Function to display the output of the program
def main():
    #Ask the user to enter a string.
    User_Str = input("Enter a string of characters: ")
    
    numV = num_vowels(User_Str)
    numC = num_constants(User_Str)
    #Display the vowels and constants
    print(f"This string has {numV} vowels, and {numC} constants. ")
    
#Function to collect the number of volwels in the string
#Parameter - the string inputed by the user
#Return - the number of vowels in a string
def num_vowels(User_Str):
    #Define a list for containing vowels.
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    #Inizialize a accumaltor to hold the count for the number of volwels in the string
    vowels_count = 0
    #Count the vowels in the User_Str string
    #For each character in the string
    for v in User_Str:
        #If the specific character is in the list of vowels:
        if v.lower() in vowels:
            #Add one to the accumulator
            vowels_count += 1
            
    return vowels_count

#Function to collect the number of constants in the string
#Parameter - the string inputed by the user, and the list that holds the vowels
#Return - the number of constants in the string
def num_constants(User_Str):
    #Define a list for containing vowels.
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    #Inizialize a accumaltor to hold the count for the number of constants in the string
    constants_count = 0
    
    #For each character in the string
    for c in User_Str:
        #If the character is a letter AND is not in the list of vowels
        if c.isalpha() and c.lower() not in vowels:
            
            constants_count += 1
    #Return the constant count        
    return constants_count
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
main()