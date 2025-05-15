#Naomi Williams
#2/27/2025
#Bug Collector Program
#Initializing the accumulator
total_bugs = 0

#Get the bugs collected on each day
for day in range(1, 8):
    #Prompt the user
    print(f"Enter the bugs collected on day", day)
    
    #input the number of bugs. 
    bugs= int(input())
    
    #Input Validation for the number of bugs
    while bugs < 0:
        print("Error: The number of bugs collected cannot be negative. Please enter a valid number.")
        print(f"\nEnter the bugs collected on day", day)
        bugs = int(input())
        #Add bugs to total_bugs.
    total_bugs += bugs
    
#Display the total bugs
print("You collected a total of", total_bugs, "bugs.")