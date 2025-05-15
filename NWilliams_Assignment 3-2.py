#Naomi Williams
#2/16/2025
#Hot Dog Cookout Calculator
#Constants for packages
HOT_DOGS_PER_PACKAGE = 10
BUNS_PER_PACKAGE = 8

#Get the Input from the Users
number_of_people = int(input("Enter the number of people attending the cookout: "))
hot_dogs_per_person = int(input("Enter the number of hot dogs each person will receive: "))

#Calculate how many Hot Dogs and Packages are needed
total_hot_dogs = number_of_people * hot_dogs_per_person
hotdog_packages_needed = total_hot_dogs // HOT_DOGS_PER_PACKAGE
if total_hot_dogs % HOT_DOGS_PER_PACKAGE != 0:
    hotdog_packages_needed += 1
bun_packages_needed = total_hot_dogs // BUNS_PER_PACKAGE
if total_hot_dogs % BUNS_PER_PACKAGE != 0:
    bun_packages_needed += 1

#Calculate leftovers
hotdogs_leftover = (hotdog_packages_needed * HOT_DOGS_PER_PACKAGE) - total_hot_dogs
buns_leftover = (bun_packages_needed * BUNS_PER_PACKAGE) - total_hot_dogs

#Display results of calculations
print(f"Minimum packages of Hot dogs required: {hotdog_packages_needed}")
print(f"Minimum packages of Hot dog Buns required: {bun_packages_needed}")
print(f"Hot dogs leftover: {hotdogs_leftover}")
print(f"Hot dog buns leftover: {buns_leftover}")