#Naomi Williams
#2/27/2025
#Budget Analysis program
#Ask the user to input their budget for the month
budget_amount = float(input("Enter the amount you have budgeted for the month: "))

#Validate that the input is greater than zero
while budget_amount <= 0:
    print("Error - please enter a number greater than 0")
    budget_amount = float(input("Enter the amount you have budgeted for the month: "))
    
#Initializing the accumulator
total_expenses = 0.00

#Variable for the loop
more_expenses = "yes"

#Loop to get the expenses for the month
while more_expenses == "yes":
    #Ask user for each of their expenses
    expense = float(input("Enter an expense: "))
    #Validate that the input is greater than zero
    while expense <= 0:
        print("Error - please enter a number greater than 0")
        expense = float(input("Enter an expense: "))
    #Add the expense to the total
    total_expenses += expense
    
    #Ask if they have more expenses
    more_expenses = input("Do you have more expenses? (yes/no): ")
    while more_expenses not in ["yes", "no"]:
        print("Error - please enter (yes) or (no)")
        more_expenses = input("Do you have more expenses? (yes/no): ")

#Calculate how much someone has used of budget and total expenses
spent = (budget_amount - total_expenses)

#Display the result to the user
if spent > 0:
    print(f"You are under budget by ${spent:.2f}")
elif spent < 0:
    print(f"You are over budget by ${-spent:.2f}")
else:
    print("You have exactly met your budget.")


