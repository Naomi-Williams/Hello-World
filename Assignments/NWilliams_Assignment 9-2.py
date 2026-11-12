#Naomi Williams
#4/28/2025
#The Capital Quiz Problem Program
#Constant for the number of questions in the quiz
NUM_STATES = 5
#Main funcntion to display the program
#Parameter - None
#Retrun - None
def main():
    #Calling the capital_quiz function to quiz the users
    Capital_Quiz()
    
#Function to create a dictionary that contains all the states in the U.S and their Capital
#Also to loop through the dictionary to quiz the user on what the capitals are for each state
#Parameter - None
#Retun - The number of correct answers and incorrect answers
def States_And_Capitals_Dict():
    #Dictionary of U.S states and capitals
    States_And_Capitals = { #Give the dictionary a name
        "Alabama" : "Montgomery",
        "Alaska" : "Juneau",
        "Arizona" : "Phoenix",
        "Arkansas" : "Little Rock",
        "California" : "Sacramento",
        "Colorado" : "Denver",
        "Connecticut" : "Hartford",
        "Delaware" : "Dover",
        "Florida" : "Tallahassee",
        "Georgia" : "Atlanta",
        "Hawaii" : "Honolulu",
        "Idaho" : "Boise",
        "Illinois" : "Springfield",
        "Indiana" : "Indianapolis",
        "Iowa" : "Des Moines",
        "Kansas" : "Topeka",
        "Kentucky" : "Frankfort",
        "Louisiana" : "Baton Rouge",
        "Maine" : "Augusta",
        "Maryland" : "Annapolis",
        "Massachusetts" : "Boston",
        "Michigan" : "Lansing",
        "Minnesota" : "St. Paul",
        "Mississippi" : "Jackson",
        "Missouri" : "Jefferson City",
        "Montana" : "Helena",
        "Nebraska" : "Lincoln",
        "Nevada" : "Carson City",
        "New Hampshire" : "Concord",
        "New Jersey" : "Trenton",
        "New Mexico" : "Santa Fe",
        "New York" : "Albany",
        "North Carolina" : "Raleigh",
        "North Dakota" : "Bismarck",
        "Ohio" : "Columbus",
        "Oklahoma" : "Oklahoma City",
        "Oregon" : "Salem",
        "Pennsylvania" : "Harrisburg",
        "Rhode Island" : "Providence",
        "South Carolina" : "Columbia",
        "South Dakota" : "Pierre",
        "Tennessee" : "Nashville",
        "Texas" : "Austin",
        "Utah" : "Salt Lake City",
        "Vermont" : "Montpelier",
        "Virginia" : "Richmond",
        "Washington" : "Olympia",
        "West Virginia" : "Charleston",
        "Wisconsin" : "Madison",
        "Wyoming" :  "Cheyenne"
    }
    
    return States_And_Capitals
    
def Capital_Quiz():
    #Initialize the dictionary
    State_Caps = States_And_Capitals_Dict()
    #Initialize counter for incorrect answers
    Incorrect_Answers = 0
    #Initialize counter for correct answers
    Correct_Answers = 0
    for count in range(NUM_STATES):
        #Get a random entry from the dictionary
        state, capital = State_Caps.popitem()
        #Quiz the user
        print(f"What is the capital of {state}? ")
        UserAnswer = input("Enter your answer: ")
        
        if UserAnswer.lower() == capital.lower():
            print("Correct!")
            Correct_Answers += 1
        else:
            print("Incorrect")
            Incorrect_Answers += 1
                    
    print("\nQuiz complete")
    print(f"Correct Answers: {Correct_Answers} ")
    print(f"Incorrect Answers: {Incorrect_Answers} ")
     
#Call the main function to display the program   
main()
