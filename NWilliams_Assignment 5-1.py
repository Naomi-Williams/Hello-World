#Naomi Williams
#2/27/2025
#Kilometer Converter Program
#constants for program
CONVERSION_FACTOR = 0.6214

def main():
    #Ask user to input a distance in kilometers
    kilometers = float(input("Enter a distance in kilometers: "))
    
    #Validate that the input is greater than zero
    while kilometers <= 0:
        print("Error - Enter a number greater than zero")
        kilometers = float(input("Enter a distance in kilometers: "))
    
    #Display the distance converted to miles.
    show_miles(kilometers)

def show_miles(km):
    #Calculate the amount of miles
    miles = km * CONVERSION_FACTOR
    
    #Display the converted inputed kilometers to miles
    print(km, f"Kilometers equals, {miles:.2f}", "miles.")
    
main()