#Naomi Williams
#2/27/2025
#Tuition Increase Program
#Initializing the accumulator
INITIAL_TUITION_PRICE = 8000.0

#Increase Rate
INCREASE_RATE = 0.03

print("Year\tTuition")

#Loop for the next 5 years
for year in range(1, 6):
    #Calculate the tuition for the specific year
    tuition = INITIAL_TUITION_PRICE * (1 + INCREASE_RATE) ** year
    
    #Display the year and the tuition amount for that year
    print(f"{year}\t${tuition:,.2f}")
