#Naomi Williams
#2/13/2025
#Areas Of Rectangles Program
#Get the Lengths of rectangle 1
length_1 = float(input("Enter the length of rectangle 1: "))
width_1 = float(input("Enter the width of rectangle 1: "))

#Get the Lengths of retangle 2
length_2 = float(input("Enter the length of rectangle 2: "))
width_2 = float(input("Enter the width of rectangle 2: "))

#Calculate the areas of the two rectangles
Area_1 = length_1 * width_1
Area_2 = length_2 * width_2

#Which Rectangle has the greater area
if Area_1 > Area_2:
    print("Rectangle 1 has the greater area.")
elif Area_2 > Area_1:
    print("Rectangle 2 has the greater area.")
else:
    print("Both have the same area.")

