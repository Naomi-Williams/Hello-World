#Naomi Williams
#2/16/2025
#Restaurant Selector Program
#Getting input from the user about party
Vegatarian = input("Is anyone in your party a vegitarian [yes/no]: ")
Vegan = input("Is anyone in your party a vegan [yes/no]: ")
Gluten_free = input("Is anyone in your party gluten-free [yes/no: ")

#Determing suitable restaurant for specific party
print("Here are your restaurant choices: ")

if Vegatarian == "no" and Vegan == "no" and Gluten_free == "no":
    print("Joe's Gourmet Burgers")
if Vegatarian == "yes" and Vegan == "no" and Gluten_free == "yes":
    print("Main Street Pizza Company")
    print("Corner Cafe")
    print("The Chefs Kitchen")
if Vegatarian == "yes" and Vegan == "yes" and Gluten_free == "yes":
    print("Corner Cafe")
    print("The Chefs Kitchen")
if Vegatarian == "yes" and Vegan == "no" and Gluten_free == "no":
    print("Mama's Fine Italian")
    print("Main Street Pizza Company")
    print("Corner Cafe")
    print("The Chefs Kitchen")
if Vegatarian == "no" and Vegan == "no" and Gluten_free == "yes":
    print("Main Street Pizza Company")
    print("Corner Cafe")
    print("The Chef's Kitchen")
if Vegatarian == "no" and Vegan == "yes" and Gluten_free == "no":
    print("Corner Cafe")
    print("The Chef's Kitchen")