#Naomi Williams
#4/24/2025
#Word Seperator Program
#Main function to display the program
#Parameter - None
#Return - None
def main():
    #Ask the user to input a sentence with no spaces and to capitalize the first letter of each word
    sentence = input("Enter a sentence in which all the words run together and the first character of each word is uppercase: ")
    
    #Call the word seperator list by assigning it to a variable
    newSentence = word_seperator(sentence)
    #Display the newly formatted list
    print(f"Formatted sentence: {newSentence}")

    
#Function to seperate the words in a sentence based on the captitalization of a new word
#Parameter - The sentence input by the user
#Return - the formatted list
def word_seperator(sentence):
    #Created an empty list to contain the sentence provided by the user
    result_sentence = ""  #Empty list to contain the newley formatted sentence
    for character in sentence:
        #If the character is uppercase, add a space before it but not if its the first character
        if character.isupper() and result_sentence:
            result_sentence += " " + character.lower()
        else:
            result_sentence += character
            
    #Capitalize the first word and return the result
    return result_sentence[0].upper() + result_sentence[1:]   #Combines the captilized first character in sentence to the lower case characters of the rest of the sentence
    
    
    
main()