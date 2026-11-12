#Naomi Williams
#5/8/2025
#Pet Program
#Define a class called pet
class Pet:
    #Initialize the attributes using __init__
    def __init__(self, name, animal_type, age):
        self._name = name
        self._animal_type = animal_type
        self._age = age
    #Set_name methond assigns value to name field
    def set_name(self, name):
        self._name = name
    #set_animal_type method assigns value to animal_type field
    def set_animal_type(self, animal_type):
        self._animal_type = animal_type
    #set_age method assigns value to age field
    def set_age(self, age):
        self._age = age
    #get_name method returns value to name field
    def get_name(self):
        return self._name
    #get_animal_type method returns value to animal_type field
    def get_animal_type(self):
        return self._animal_type
    #get_age method returns value to age field
    def get_age(self):
        return self._age
    #Display the attribute of the object
    def __str__(self):
        retStr = f"Name: {self._name}\nAnimal Type: {self._animal_type}\nAge: {self._age}\n"
        return retStr
    
#Main funcion to ask the user to input a course number to display the information for that course
#Parameter - None
#Return - None
def main():
    #Get the pet's name, type and age
    name = input("What is the name of your pet? ")
    animal_type = input("What type of animal is your pet? ")
    bflag = True
    while bflag:
        try:
            age = int(input("How old is your pet? "))
            while age <= 0 or age >= 100:
                print("Error - Invalid input. Please reenter a age greater than 0 and less than 100. ")
                age = int(input("How old is your pet? "))
            bflag = False
        except ValueError:
            print("Error - Invalid input. Please enter a numerical value. ")
    #Create an instance of the pet class
    my_pet = Pet(name, animal_type, age)
    
    
    #Display the information
    print("\nPet information: ")
    print(my_pet)
    
    
#Call the main function back to display the program    
main()
